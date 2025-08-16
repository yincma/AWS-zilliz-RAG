#!/usr/bin/env python3
"""
验证L2距离是否被平方的假设
"""
import numpy as np

# 从之前的测试获得的数据
data = [
    {"desc": "向量1 L2范数", "理论值": 16.3454, "Zilliz返回": 267.1730},
    {"desc": "向量2 L2范数", "理论值": 11.2084, "Zilliz返回": 125.6284},
    {"desc": "向量1到向量2", "理论值": 17.1252, "Zilliz返回": 293.2721}
]

print("=== L2距离平方假设验证 ===\n")
print(f"{'描述':<20} {'理论L2':<10} {'Zilliz返回':<12} {'理论L2²':<10} {'差异%':<10}")
print("-" * 70)

for item in data:
    理论值 = item["理论值"]
    zilliz值 = item["Zilliz返回"]
    理论平方 = 理论值 ** 2
    差异百分比 = abs(理论平方 - zilliz值) / zilliz值 * 100
    
    print(f"{item['desc']:<20} {理论值:<10.4f} {zilliz值:<12.4f} {理论平方:<10.4f} {差异百分比:<10.2f}%")

print("\n=== 结论 ===")
print("Zilliz返回的'L2距离'实际上是L2距离的平方！")
print("\n正确的score计算公式应该是：")
print("1. 先开方：actual_l2_distance = sqrt(zilliz_distance)")
print("2. 再计算：score = max(0, min(100, 100 - actual_l2_distance * scale_factor))")
print("\n或者调整scale_factor以适应平方距离：")
print("score = max(0, min(100, 100 - sqrt(zilliz_distance) * 10))")