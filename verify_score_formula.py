#!/usr/bin/env python3
"""
验证score计算公式
"""
import math

print("=== Score计算公式验证 ===\n")
print("当前公式: score = max(0, min(100, 100 - actual_distance * 5))")
print("\n测试案例：")

test_cases = [
    {"distance_squared": 267.1730, "desc": "向量1"},
    {"distance_squared": 125.6284, "desc": "向量2"},
    {"distance_squared": 0, "desc": "完全匹配"},
    {"distance_squared": 25, "desc": "L2=5的情况"},
    {"distance_squared": 100, "desc": "L2=10的情况"},
    {"distance_squared": 400, "desc": "L2=20的情况"},
]

print(f"\n{'描述':<12} {'L2²':<10} {'L2':<10} {'100-L2*5':<15} {'最终Score':<10}")
print("-" * 65)

for case in test_cases:
    distance_squared = case["distance_squared"]
    actual_distance = math.sqrt(distance_squared) if distance_squared > 0 else 0
    raw_score = 100 - actual_distance * 5
    final_score = max(0, min(100, raw_score))
    
    print(f"{case['desc']:<12} {distance_squared:<10.2f} {actual_distance:<10.2f} {raw_score:<15.2f} {final_score:<10.1f}%")

print("\n=== 分析 ===")
print("问题：100 - 16.3 * 5 = 100 - 81.5 = 18.5%")
print("这个计算是正确的！")
print("\n如果想要16.3的距离得到81.5%的分数，需要不同的公式：")
print("方案1: score = max(0, 100 - actual_distance * 1)  # 系数改为1")
print("方案2: score = max(0, (1 - actual_distance/20) * 100)  # 归一化到0-20范围")
print("方案3: score = exp(-actual_distance/10) * 100  # 指数衰减")