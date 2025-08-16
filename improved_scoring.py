#!/usr/bin/env python3
"""
改进的评分系统
"""
import math

def improved_score_calculation(distance_squared):
    """改进的相似度分数计算"""
    actual_distance = math.sqrt(distance_squared) if distance_squared > 0 else 0
    
    # 方案1: 线性映射（更宽松）
    # 0-5 → 100-75, 5-10 → 75-50, 10-20 → 50-0
    linear_score = max(0, min(100, 100 - actual_distance * 2.5))
    
    # 方案2: 指数衰减（更自然）
    # 使用指数函数，距离越近分数下降越慢
    exp_score = math.exp(-actual_distance / 10) * 100
    
    # 方案3: 对数映射（折中方案）
    # 距离0-30映射到100-0
    if actual_distance == 0:
        log_score = 100
    else:
        log_score = max(0, 100 - 20 * math.log(actual_distance + 1))
    
    return {
        "distance": actual_distance,
        "linear": linear_score,
        "exponential": exp_score,
        "logarithmic": log_score
    }

def improved_confidence_calculation(scores):
    """基于实际相似度计算置信度"""
    if not scores:
        return 0.2  # 无结果时的默认置信度
    
    # 获取最高分
    max_score = max(scores)
    # 获取平均分
    avg_score = sum(scores) / len(scores)
    
    # 置信度基于最高分和平均分的组合
    # 如果最高分很高且平均分也不错，置信度就高
    confidence = (max_score * 0.7 + avg_score * 0.3) / 100
    
    # 根据找到的文档数量调整
    doc_count_factor = min(1.0, len(scores) / 3)  # 3个文档达到满分
    
    # 最终置信度
    final_confidence = confidence * (0.7 + 0.3 * doc_count_factor)
    
    return min(1.0, final_confidence)

# 测试数据
test_cases = [
    {"name": "README_CN.md", "distance_squared": 125.6284},
    {"name": "document.txt", "distance_squared": 267.1730},
    {"name": "完美匹配", "distance_squared": 0},
    {"name": "较近文档", "distance_squared": 25},
    {"name": "中等距离", "distance_squared": 100},
]

print("=== 改进的评分系统 ===\n")
print(f"{'文档':<15} {'L2距离':<10} {'当前公式':<10} {'线性改进':<10} {'指数衰减':<10} {'对数映射':<10}")
print("-" * 75)

all_scores = {"current": [], "linear": [], "exp": [], "log": []}

for case in test_cases:
    results = improved_score_calculation(case["distance_squared"])
    current_score = max(0, min(100, 100 - results["distance"] * 5))
    
    all_scores["current"].append(current_score)
    all_scores["linear"].append(results["linear"])
    all_scores["exp"].append(results["exponential"])
    all_scores["log"].append(results["logarithmic"])
    
    print(f"{case['name']:<15} {results['distance']:<10.2f} {current_score:<10.1f} "
          f"{results['linear']:<10.1f} {results['exponential']:<10.1f} {results['logarithmic']:<10.1f}")

print("\n=== 置信度计算对比 ===\n")
print(f"{'方案':<15} {'最高分':<10} {'平均分':<10} {'置信度':<10}")
print("-" * 45)

for method, scores in all_scores.items():
    max_score = max(scores)
    avg_score = sum(scores) / len(scores)
    confidence = improved_confidence_calculation(scores[:2])  # 假设只返回前2个文档
    
    print(f"{method:<15} {max_score:<10.1f} {avg_score:<10.1f} {confidence*100:<10.1f}%")

print("\n=== 推荐方案 ===")
print("1. Score计算：使用指数衰减或对数映射，更符合人类对相似度的感知")
print("2. 置信度：基于实际分数动态计算，而不是硬编码80%")
print("3. 系数调整：将当前的系数5改为2.5或使用非线性映射")