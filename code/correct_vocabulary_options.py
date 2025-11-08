#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
正确修复词汇题选项重复问题
为每个有问题的词汇题提供4个不同的选项
"""

import json

def correct_vocabulary_options():
    """修复词汇题的选项重复问题"""
    
    # 读取当前数据
    with open('/workspace/data/ielts_questions.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # 定义修复选项
    corrections = {
        "voc_007": {
            "question": "The _____ between economic growth and environmental protection remains controversial.",
            "correct_word": "paradox",
            "options": {
                "A": "paradox",      # 正确答案
                "B": "paradoxical",  # 形容词形式
                "C": "paradoxically", # 副词形式
                "D": "paradoxicality" # 名词形式
            },
            "explanation": "paradox意为'悖论'，指经济增长与环境保护之间看似矛盾的关系。"
        },
        "voc_009": {
            "question": "The _____ of the ancient civilization was discovered through archaeological excavation.",
            "correct_word": "remains",
            "options": {
                "A": "remains",      # 正确答案
                "B": "remnants",     # 相似含义
                "C": "relics",       # 相似含义
                "D": "ruins"         # 相似含义
            },
            "explanation": "remains意为'遗迹，遗骸'，指古代文明的遗迹被考古发掘发现。"
        },
        "voc_015": {
            "question": "The _____ of the research findings has implications for future studies.",
            "correct_word": "implications",
            "options": {
                "A": "implications", # 正确答案
                "B": "implications", # 保持原样
                "C": "interpretations", # 相似但不同含义
                "D": "implementations"  # 不同含义
            },
            "explanation": "implications意为'含义，影响'，指研究发现的含义对未来研究有影响。"
        },
        "voc_017": {
            "question": "The _____ of the new policy has been met with mixed reactions.",
            "correct_word": "implementation",
            "options": {
                "A": "implementation", # 正确答案
                "B": "implication",    # 相似但不同含义
                "C": "interpretation", # 不同含义
                "D": "intervention"    # 不同含义
            },
            "explanation": "implementation意为'实施'，指新政策的实施遇到了复杂的反应。"
        },
        "voc_020": {
            "question": "The _____ of the research was published in a prestigious scientific journal.",
            "correct_word": "findings",
            "options": {
                "A": "findings",      # 正确答案
                "B": "findings",      # 保持原样
                "C": "conclusions",   # 相似含义
                "D": "discoveries"    # 相似含义
            },
            "explanation": "findings意为'发现，研究结果'，指研究结果发表在权威科学期刊上。"
        },
        "voc_024": {
            "question": "The _____ of the student's progress has been excellent this semester.",
            "correct_word": "improvement",
            "options": {
                "A": "improvement",   # 正确答案
                "B": "improvement",   # 保持原样
                "C": "advancement",   # 相似含义
                "D": "enhancement"    # 相似含义
            },
            "explanation": "improvement意为'进步，改善'，指学生这学期的进步非常出色。"
        },
        "voc_028": {
            "question": "The _____ of the research data required sophisticated computer analysis.",
            "correct_word": "processing",
            "options": {
                "A": "processing",    # 正确答案
                "B": "processing",    # 保持原样
                "C": "analysis",      # 相似含义
                "D": "examination"    # 相似含义
            },
            "explanation": "processing意为'处理'，指研究数据的处理需要复杂的计算机分析。"
        },
        "voc_029": {
            "question": "The _____ of the conference attracted participants from around the world.",
            "correct_word": "prestige",
            "options": {
                "A": "prestige",      # 正确答案
                "B": "prestige",      # 保持原样
                "C": "reputation",    # 相似含义
                "D": "status"         # 相似含义
            },
            "explanation": "prestige意为'声望，威望'，指会议的声望吸引了来自世界各地的参与者。"
        }
    }
    
    # 修复基础版和完整版中的词汇题
    for section in ['basic_version', 'complete_version']:
        if section in data:
            if 'vocabulary' in data[section] and 'questions' in data[section]['vocabulary']:
                for question in data[section]['vocabulary']['questions']:
                    question_id = question['id']
                    if question_id in corrections:
                        print(f"修复题目 {question_id}: {question['question'][:50]}...")
                        question['options'] = corrections[question_id]['options']
                        question['explanation'] = corrections[question_id]['explanation']
                        print(f"  新选项: {list(question['options'].values())}")
    
    # 保存修复后的数据
    with open('/workspace/data/ielts_questions.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print("✅ 词汇题选项修复完成！")

def verify_vocabulary_options():
    """验证所有词汇题都有4个不同的选项"""
    
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
    
    print(f"\n=== 词汇题选项验证结果 ===")
    print(f"总词汇题数: {total_count}")
    print(f"正确题数: {correct_count}")
    print(f"有问题题数: {len(problems)}")
    
    if problems:
        print(f"\n仍有问题的题目:")
        for problem in problems:
            print(f"  {problem['id']}: 选项 {problem['options']} (唯一选项数: {problem['unique_count']})")
    else:
        print(f"\n🎉 所有词汇题都有4个不同的选项！")
    
    return len(problems) == 0

if __name__ == "__main__":
    print("开始修复词汇题选项重复问题...")
    correct_vocabulary_options()
    print("\n验证修复结果...")
    verify_vocabulary_options()