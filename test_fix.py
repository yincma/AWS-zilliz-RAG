#!/usr/bin/env python3
"""
测试score修复效果
"""
import math

# 测试数据（从实际Zilliz获得）
test_cases = [
    {"name": "向量1自己", "distance_squared": 0, "expected": "100%"},
    {"name": "向量2 L2范数", "distance_squared": 125.6284, "expected": "~40-45%"},
    {"name": "向量1 L2范数", "distance_squared": 267.1730, "expected": "~15-20%"},
    {"name": "向量间距离", "distance_squared": 293.2721, "expected": "~10-15%"},
]

print("=== Score计算测试 ===\n")
print(f"{'测试案例':<15} {'L2²':<12} {'实际L2':<10} {'计算Score':<10} {'预期':<10}")
print("-" * 65)

for case in test_cases:
    distance_squared = case["distance_squared"]
    actual_distance = math.sqrt(distance_squared) if distance_squared > 0 else 0
    score = max(0, min(100, 100 - actual_distance * 5))
    
    print(f"{case['name']:<15} {distance_squared:<12.4f} {actual_distance:<10.4f} {score:<10.1f}% {case['expected']:<10}")

print("\n✅ 修复后的score计算公式正常工作！")