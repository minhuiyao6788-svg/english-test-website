#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
彻底修复词汇题选项重复问题
为所有有问题的词汇题提供完全不同的4个选项
"""

import json

def final_vocabulary_fix():
    """彻底修复词汇题的选项重复问题"""
    
    # 读取当前数据
    with open('/workspace/data/ielts_questions.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # 定义完全不同的选项
    final_corrections = {
        "voc_015": {
            "question": "The _____ of the research findings has implications for future studies.",
            "correct_word": "implications",
            "options": {
                "A": "implications",    # 正确答案
                "B": "interpretations", # 解释
                "C": "applications",    # 应用
                "D": "investigations"   # 调查
            },
            "explanation": "implications意为'含义，影响'，指研究发现的含义对未来研究有影响。"
        },
        "voc_020": {
            "question": "The _____ of the research was published in a prestigious scientific journal.",
            "correct_word": "findings",
            "options": {
                "A": "findings",        # 正确答案
                "B": "conclusions",     # 结论
                "C": "discoveries",     # 发现
                "D": "results"          # 结果
            },
            "explanation": "findings意为'发现，研究结果'，指研究结果发表在权威科学期刊上。"
        },
        "voc_024": {
            "question": "The _____ of the student's progress has been excellent this semester.",
            "correct_word": "improvement",
            "options": {
                "A": "improvement",     # 正确答案
                "B": "advancement",     # 进步
                "C": "enhancement",     # 增强
                "D": "development"      # 发展
            },
            "explanation": "improvement意为'进步，改善'，指学生这学期的进步非常出色。"
        },
        "voc_028": {
            "question": "The _____ of the research data required sophisticated computer analysis.",
            "correct_word": "processing",
            "options": {
                "A": "processing",      # 正确答案
                "B": "analysis",        # 分析
                "C": "examination",     # 检查
                "D": "evaluation"       # 评估
            },
            "explanation": "processing意为'处理'，指研究数据的处理需要复杂的计算机分析。"
        },
        "voc_029": {
            "question": "The _____ of the conference attracted participants from around the world.",
            "correct_word": "prestige",
            "options": {
                "A": "prestige",        # 正确答案
                "B": "reputation",      # 声誉
                "C": "status",          # 地位
                "D": "standing"         # 声望
            },
            "explanation": "prestige意为'声望，威望'，指会议的声望吸引了来自世界各地的参与者。"
        }
    }
    
    # 修复基础版和完整版中的词汇题
    fix_count = 0
    for section in ['basic_version', 'complete_version']:
        if section in data:
            if 'vocabulary' in data[section] and 'questions' in data[section]['vocabulary']:
                for question in data[section]['vocabulary']['questions']:
                    question_id = question['id']
                    if question_id in final_corrections:
                        print(f"最终修复题目 {question_id}: {question['question'][:50]}...")
                        question['options'] = final_corrections[question_id]['options']
                        question['explanation'] = final_corrections[question_id]['explanation']
                        print(f"  最终选项: {list(question['options'].values())}")
                        fix_count += 1
    
    # 保存修复后的数据
    with open('/workspace/data/ielts_questions.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"✅ 最终词汇题选项修复完成！共修复 {fix_count} 道题")

def comprehensive_verify():
    """全面验证所有词汇题"""
    
    with open('/workspace/data/ielts_questions.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    problems = []
    correct_count = 0
    total_count = 0
    
    # 检查基础版和完整版
    for section in ['basic_version', 'complete_version']:
        if section in data and 'vocabulary' in data[section] and 'questions' in data[section]['vocabulary']:
            for question in data[section]['vocabulary']['questions']:
                total_count += 1
                question_id = question['id']
                options = list(question['options'].values())
                
                # 检查是否有重复选项
                unique_options = set(options)
                if len(unique_options) < 4:
                    problems.append({
                        'id': question_id,
                        'options': options,
                        'unique_count': len(unique_options)
                    })
                else:
                    correct_count += 1
    
    print(f"\n=== 全面词汇题选项验证结果 ===")
    print(f"总词汇题数: {total_count}")
    print(f"正确题数: {correct_count}")
    print(f"有问题题数: {len(problems)}")
    
    if problems:
        print(f"\n仍有问题的题目:")
        for problem in problems:
            print(f"  {problem['id']}: 选项 {problem['options']} (唯一选项数: {problem['unique_count']})")
    else:
        print(f"\n🎉 所有词汇题都有4个完全不同的选项！")
    
    return len(problems) == 0

if __name__ == "__main__":
    print("开始最终修复词汇题选项重复问题...")
    final_vocabulary_fix()
    print("\n进行最终验证...")
    comprehensive_verify()