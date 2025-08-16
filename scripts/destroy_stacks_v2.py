#!/usr/bin/env python3
"""
智能栈删除脚本 V2 - 处理导出依赖和删除取消问题
完全通过 CloudFormation API 管理资源删除
"""

import boto3
import sys
import time
import argparse
from typing import List, Dict, Optional, Set
from botocore.exceptions import ClientError


class StackDestroyer:
    """智能栈删除器 - 使用 CloudFormation API"""
    
    def __init__(self, region: str = 'us-east-1', prefix: str = 'RAG-'):
        """
        初始化栈删除器
        
        Args:
            region: AWS 区域
            prefix: 栈名称前缀
        """
        self.cf = boto3.client('cloudformation', region_name=region)
        self.region = region
        self.prefix = prefix
        
    def get_stacks_by_status(self, status_filters: List[str]) -> List[Dict]:
        """
        根据状态获取栈列表
        
        Args:
            status_filters: 状态过滤器列表
            
        Returns:
            栈列表
        """
        try:
            response = self.cf.list_stacks(StackStatusFilter=status_filters)
            stacks = [
                stack for stack in response['StackSummaries']
                if stack['StackName'].startswith(self.prefix)
            ]
            return stacks
        except ClientError as e:
            print(f"❌ 获取栈列表失败: {e}")
            return []
    
    def get_stack_dependencies(self) -> Dict[str, Set[str]]:
        """
        分析栈之间的依赖关系
        
        Returns:
            依赖关系字典 {栈名: {依赖的栈}}
        """
        dependencies = {}
        active_stacks = self.get_stacks_by_status([
            'CREATE_COMPLETE', 'UPDATE_COMPLETE', 'UPDATE_ROLLBACK_COMPLETE'
        ])
        
        for stack in active_stacks:
            stack_name = stack['StackName']
            dependencies[stack_name] = set()
            
            try:
                # 获取栈的详细信息
                stack_detail = self.cf.describe_stacks(StackName=stack_name)
                stack_info = stack_detail['Stacks'][0]
                
                # 分析参数和输出以确定依赖关系
                # 这是一个简化的实现，实际可以更复杂
                if 'Web' in stack_name:
                    # Web栈通常依赖于API栈
                    api_stack = stack_name.replace('Web', 'API')
                    if any(s['StackName'] == api_stack for s in active_stacks):
                        dependencies[stack_name].add(api_stack)
                elif 'API' in stack_name:
                    # API栈通常依赖于Data栈
                    data_stack = stack_name.replace('API', 'Data')
                    if any(s['StackName'] == data_stack for s in active_stacks):
                        dependencies[stack_name].add(data_stack)
                        
            except ClientError:
                pass
                
        return dependencies
    
    def get_deletion_order(self, dependencies: Dict[str, Set[str]]) -> List[str]:
        """
        根据依赖关系确定删除顺序
        
        Args:
            dependencies: 依赖关系字典
            
        Returns:
            按正确顺序排列的栈名列表
        """
        # 拓扑排序
        in_degree = {stack: 0 for stack in dependencies}
        for stack in dependencies:
            for dep in dependencies[stack]:
                if dep in in_degree:
                    in_degree[dep] += 1
        
        queue = [stack for stack, degree in in_degree.items() if degree == 0]
        result = []
        
        while queue:
            stack = queue.pop(0)
            result.append(stack)
            for other_stack in dependencies:
                if stack in dependencies[other_stack]:
                    in_degree[other_stack] -= 1
                    if in_degree[other_stack] == 0:
                        queue.append(other_stack)
        
        return result
    
    def fix_failed_stack(self, stack_name: str) -> bool:
        """
        修复 DELETE_FAILED 状态的栈
        
        Args:
            stack_name: 栈名称
            
        Returns:
            是否成功
        """
        print(f"🔧 修复失败的栈: {stack_name}")
        
        try:
            # 获取失败的资源
            resources = self.cf.describe_stack_resources(StackName=stack_name)
            failed_resources = [
                r['LogicalResourceId'] 
                for r in resources['StackResources']
                if r.get('ResourceStatus') == 'DELETE_FAILED'
            ]
            
            if failed_resources:
                print(f"  发现失败的资源: {', '.join(failed_resources)}")
                print(f"  跳过这些资源并重试删除...")
                
                # 使用 retain 选项跳过失败的资源
                try:
                    self.cf.delete_stack(
                        StackName=stack_name,
                        RetainResources=failed_resources
                    )
                    print(f"  ✅ 栈已标记为删除（保留失败的资源）")
                    return True
                except ClientError as e:
                    if 'ValidationError' in str(e):
                        # 如果 retain 失败，尝试普通删除
                        self.cf.delete_stack(StackName=stack_name)
                        print(f"  ✅ 栈已标记为删除")
                        return True
                    else:
                        print(f"  ❌ 删除失败: {e}")
                        return False
            else:
                # 没有失败的资源，直接删除
                self.cf.delete_stack(StackName=stack_name)
                print(f"  ✅ 栈已标记为删除")
                return True
                
        except ClientError as e:
            print(f"  ❌ 处理失败: {e}")
            return False
    
    def delete_stack_safe(self, stack_name: str, retry_count: int = 3) -> bool:
        """
        安全删除栈，带重试和状态验证
        
        Args:
            stack_name: 栈名称
            retry_count: 重试次数
            
        Returns:
            是否成功
        """
        for attempt in range(retry_count):
            try:
                print(f"🗑️  删除栈: {stack_name} (尝试 {attempt + 1}/{retry_count})")
                
                # 发送删除请求
                self.cf.delete_stack(StackName=stack_name)
                
                # 等待一段时间，让操作生效
                time.sleep(5)
                
                # 验证栈是否进入删除状态
                try:
                    response = self.cf.describe_stacks(StackName=stack_name)
                    stack_status = response['Stacks'][0]['StackStatus']
                    
                    if stack_status == 'DELETE_IN_PROGRESS':
                        print(f"  ✅ 栈已开始删除")
                        return True
                    elif stack_status in ['CREATE_COMPLETE', 'UPDATE_COMPLETE']:
                        # 检查最近的事件，看是否删除被取消
                        events = self.cf.describe_stack_events(StackName=stack_name)
                        recent_event = events['StackEvents'][0]
                        
                        if 'Delete canceled' in recent_event.get('ResourceStatusReason', ''):
                            print(f"  ⚠️  删除被取消: {recent_event['ResourceStatusReason']}")
                            if 'in use by' in recent_event['ResourceStatusReason']:
                                # 导出依赖问题，等待后重试
                                print(f"  ⏳ 等待 30 秒后重试...")
                                time.sleep(50)
                                continue
                        else:
                            print(f"  ⚠️  栈状态: {stack_status}，等待后重试...")
                            time.sleep(10)
                            continue
                    else:
                        print(f"  ℹ️  栈状态: {stack_status}")
                        return True
                        
                except ClientError as e:
                    if 'does not exist' in str(e):
                        print(f"  ✅ 栈已删除或不存在")
                        return True
                    else:
                        print(f"  ❌ 验证失败: {e}")
                        
            except ClientError as e:
                if 'does not exist' in str(e):
                    print(f"  ℹ️  栈不存在")
                    return True
                else:
                    print(f"  ❌ 删除失败: {e}")
                    
        print(f"  ❌ 达到最大重试次数，删除失败")
        return False
    
    def wait_for_deletion(self, stack_names: List[str], timeout: int = 1800) -> bool:
        """
        等待栈删除完成，带智能重试
        
        Args:
            stack_names: 栈名称列表
            timeout: 超时时间（秒），默认30分钟
            
        Returns:
            是否全部删除成功
        """
        print(f"⏳ 等待 {len(stack_names)} 个栈删除（最多等待 {timeout//60} 分钟）...")
        start_time = time.time()
        last_count = len(stack_names)
        no_progress_count = 0
        retry_attempts = {}  # 记录每个栈的重试次数
        
        while time.time() - start_time < timeout:
            remaining = []
            remaining_status = {}
            need_retry = []  # 需要重试删除的栈
            
            for stack_name in stack_names:
                try:
                    response = self.cf.describe_stacks(StackName=stack_name)
                    stack = response['Stacks'][0]
                    status = stack['StackStatus']
                    
                    if status == 'DELETE_COMPLETE':
                        continue  # 已完成，跳过
                    elif status == 'DELETE_IN_PROGRESS':
                        remaining.append(stack_name)
                        remaining_status[stack_name] = status
                    elif status in ['CREATE_COMPLETE', 'UPDATE_COMPLETE']:
                        # 栈仍在完成状态，可能删除被取消了
                        remaining.append(stack_name)
                        remaining_status[stack_name] = status
                        
                        # 检查是否需要重试
                        if stack_name not in retry_attempts:
                            retry_attempts[stack_name] = 0
                            
                        if retry_attempts[stack_name] < 3:
                            # 检查最近的事件
                            events = self.cf.describe_stack_events(StackName=stack_name)
                            if events['StackEvents']:
                                recent_event = events['StackEvents'][0]
                                if 'Delete canceled' in recent_event.get('ResourceStatusReason', ''):
                                    need_retry.append(stack_name)
                                    retry_attempts[stack_name] += 1
                    else:
                        remaining.append(stack_name)
                        remaining_status[stack_name] = status
                        
                except ClientError as e:
                    if 'does not exist' not in str(e):
                        remaining.append(stack_name)
                        remaining_status[stack_name] = 'CHECKING'
            
            # 重试需要重试的栈
            for stack_name in need_retry:
                print(f"\n🔄 重试删除栈: {stack_name} (第 {retry_attempts[stack_name]} 次重试)")
                self.delete_stack_safe(stack_name, retry_count=1)
            
            if not remaining:
                print("✅ 所有栈已删除")
                return True
            
            # 显示进度
            elapsed = int(time.time() - start_time)
            elapsed_min = elapsed // 60
            elapsed_sec = elapsed % 60
            
            # 检查是否有进展
            if len(remaining) < last_count:
                print(f"  ✅ 已删除 {last_count - len(remaining)} 个栈")
                last_count = len(remaining)
                no_progress_count = 0
            else:
                no_progress_count += 1
            
            # 显示剩余栈的状态
            if len(remaining) <= 3:
                status_info = ', '.join([f"{name}[{remaining_status.get(name, 'UNKNOWN')}]" for name in remaining])
                print(f"  还有 {len(remaining)} 个栈正在处理: {status_info} ({elapsed_min}分{elapsed_sec}秒)")
            else:
                print(f"  还有 {len(remaining)} 个栈正在处理... ({elapsed_min}分{elapsed_sec}秒)")
            
            # 如果长时间没有进展，给出提示
            if no_progress_count > 6:  # 超过1分钟没有进展
                print(f"  ⚠️  删除进度缓慢，可能需要更多时间...")
                # 检查是否有栈在 CREATE_COMPLETE 状态
                stuck_stacks = [name for name, status in remaining_status.items() 
                               if status in ['CREATE_COMPLETE', 'UPDATE_COMPLETE']]
                if stuck_stacks:
                    print(f"  ⚠️  以下栈可能需要手动处理: {', '.join(stuck_stacks)}")
                no_progress_count = 0
            
            time.sleep(10)
        
        print(f"⏱️  超时: 仍有 {len(remaining)} 个栈未删除")
        print(f"  未完成的栈: {', '.join(remaining)}")
        print(f"  💡 提示: 可以稍后运行 'make check-stacks' 查看状态，或使用 'make destroy-force' 强制重试")
        return False
    
    def destroy_all(self, force: bool = False) -> bool:
        """
        销毁所有栈
        
        Args:
            force: 是否强制删除
            
        Returns:
            是否成功
        """
        print(f"🚀 开始智能销毁流程 V2 (前缀: {self.prefix})")
        print("=" * 50)
        
        # 1. 获取所有栈状态
        print("\n📊 检查栈状态...")
        active_stacks = self.get_stacks_by_status([
            'CREATE_COMPLETE', 'UPDATE_COMPLETE', 'UPDATE_ROLLBACK_COMPLETE'
        ])
        failed_stacks = self.get_stacks_by_status(['DELETE_FAILED'])
        
        if not active_stacks and not failed_stacks:
            print("✅ 没有需要删除的栈")
            return True
        
        # 显示栈信息
        if active_stacks:
            print(f"\n活动的栈 ({len(active_stacks)}):")
            for stack in active_stacks:
                print(f"  • {stack['StackName']} [{stack['StackStatus']}]")
        
        if failed_stacks:
            print(f"\n失败的栈 ({len(failed_stacks)}):")
            for stack in failed_stacks:
                print(f"  • {stack['StackName']} [{stack['StackStatus']}]")
        
        # 用户确认
        if not force:
            response = input("\n确定要删除这些栈吗？(y/N): ")
            if response.lower() != 'y':
                print("❌ 取消删除")
                return False
        
        # 2. 处理失败的栈
        if failed_stacks:
            print("\n🔧 处理失败的栈...")
            for stack in failed_stacks:
                self.fix_failed_stack(stack['StackName'])
        
        # 3. 获取依赖关系并确定删除顺序
        print("\n🔍 分析栈依赖关系...")
        dependencies = self.get_stack_dependencies()
        deletion_order = self.get_deletion_order(dependencies)
        
        if deletion_order:
            print(f"删除顺序: {' → '.join(deletion_order)}")
        
        # 4. 按顺序删除栈
        print("\n🗑️  开始删除栈...")
        all_stacks_to_delete = []
        
        for stack_name in deletion_order:
            if self.delete_stack_safe(stack_name):
                all_stacks_to_delete.append(stack_name)
        
        # 删除不在依赖图中的栈
        for stack in active_stacks:
            if stack['StackName'] not in deletion_order:
                if self.delete_stack_safe(stack['StackName']):
                    all_stacks_to_delete.append(stack['StackName'])
        
        # 5. 等待删除完成
        if all_stacks_to_delete:
            # 可以通过参数传递超时时间
            import sys
            timeout = 1800  # 默认30分钟
            for arg in sys.argv:
                if arg.startswith('--timeout='):
                    try:
                        timeout = int(arg.split('=')[1])
                    except:
                        pass
            
            success = self.wait_for_deletion(all_stacks_to_delete, timeout=timeout)
            
            if success:
                print("\n🎉 所有栈已成功删除！")
                return True
            else:
                print("\n⚠️  部分栈可能仍在删除中")
                print("  可以使用 --timeout 参数增加等待时间")
                return False
        
        return True


def main():
    """主函数"""
    parser = argparse.ArgumentParser(
        description='智能删除 CloudFormation 栈 V2 - 处理导出依赖'
    )
    parser.add_argument(
        '--region', 
        default='us-east-1',
        help='AWS 区域 (默认: us-east-1)'
    )
    parser.add_argument(
        '--prefix',
        default='RAG-',
        help='栈名称前缀 (默认: RAG-)'
    )
    parser.add_argument(
        '--force',
        action='store_true',
        help='跳过确认提示'
    )
    parser.add_argument(
        '--check-only',
        action='store_true',
        help='仅检查栈状态，不删除'
    )
    parser.add_argument(
        '--timeout',
        type=int,
        default=1800,
        help='等待删除完成的超时时间（秒），默认30分钟'
    )
    
    args = parser.parse_args()
    
    destroyer = StackDestroyer(region=args.region, prefix=args.prefix)
    
    if args.check_only:
        # 仅检查状态
        print("📊 栈状态检查")
        print("=" * 50)
        
        active = destroyer.get_stacks_by_status([
            'CREATE_COMPLETE', 'UPDATE_COMPLETE', 'UPDATE_ROLLBACK_COMPLETE'
        ])
        failed = destroyer.get_stacks_by_status(['DELETE_FAILED'])
        in_progress = destroyer.get_stacks_by_status([
            'CREATE_IN_PROGRESS', 'DELETE_IN_PROGRESS', 'UPDATE_IN_PROGRESS'
        ])
        
        if active:
            print(f"\n✅ 活动的栈 ({len(active)}):")
            for stack in active:
                print(f"  • {stack['StackName']} [{stack['StackStatus']}]")
        
        if failed:
            print(f"\n❌ 失败的栈 ({len(failed)}):")
            for stack in failed:
                print(f"  • {stack['StackName']} [{stack['StackStatus']}]")
        
        if in_progress:
            print(f"\n🔄 处理中的栈 ({len(in_progress)}):")
            for stack in in_progress:
                print(f"  • {stack['StackName']} [{stack['StackStatus']}]")
        
        if not active and not failed and not in_progress:
            print("\n✅ 没有找到任何栈")
    else:
        # 执行删除
        success = destroyer.destroy_all(force=args.force)
        sys.exit(0 if success else 1)


if __name__ == '__main__':
    main()