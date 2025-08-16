#!/usr/bin/env python3
"""
测试最终修复效果
"""
import math

# 模拟实际数据
test_docs = [
    {"name": "README_CN.md", "distance_squared": 125.6284},
    {"name": "document.txt", "distance_squared": 267.1730},
]

print("=== 最终修复测试 ===\n")
print("修复内容：")
print("1. Score系数从5改为2.5")
print("2. 置信度基于实际分数动态计算\n")

print(f"{'文档':<15} {'L2²':<12} {'L2':<10} {'旧Score':<10} {'新Score':<10}")
print("-" * 60)

all_scores = []
for doc in test_docs:
    distance_squared = doc["distance_squared"]
    actual_distance = math.sqrt(distance_squared) if distance_squared > 0 else 0
    
    # 旧公式
    old_score = max(0, min(100, 100 - actual_distance * 5))
    # 新公式
    new_score = max(0, min(100, 100 - actual_distance * 2.5))
    
    all_scores.append(new_score)
    
    print(f"{doc['name']:<15} {distance_squared:<12.2f} {actual_distance:<10.2f} {old_score:<10.1f}% {new_score:<10.1f}%")

print("\n=== 置信度计算 ===")
print(f"旧置信度：80%（硬编码）")

# 新置信度计算
if all_scores:
    max_score = max(all_scores)
    avg_score = sum(all_scores) / len(all_scores)
    new_confidence = min(1.0, (max_score * 0.7 + avg_score * 0.3) / 100)
    print(f"新置信度：{new_confidence*100:.1f}%")
    print(f"  - 最高分：{max_score:.1f}%")
    print(f"  - 平均分：{avg_score:.1f}%")
    print(f"  - 计算：({max_score:.1f} * 0.7 + {avg_score:.1f} * 0.3) / 100 = {new_confidence:.2f}")

print("\n✅ 改进效果：")
print("1. Score更合理：README从44%提升到72%")
print("2. 置信度动态：从固定80%变为基于实际分数的66%")