#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CET-4/6题库最终修复脚本
修复版本标识、答案字段名等问题
"""

import json
import random

def fix_cet4_6_questions():
    """修复CET-4/6题库问题"""
    
    # 读取题库文件
    with open('data/cet4_6_questions.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    print("开始修复题库...")
    
    # 修复题目格式和添加版本标识
    questions = data['questions']
    
    # 根据题型和难度分配版本
    # 基础版：词汇15题(简单+中等)、语法15题(简单+中等)、阅读20题(简单+中等)
    # 完整版：词汇30题、语法30题、阅读40题
    
    vocabulary_questions = [q for q in questions if q['category'] == 'vocabulary']
    grammar_questions = [q for q in questions if q['category'] == 'grammar']
    reading_questions = [q for q in questions if q['category'] == 'reading']
    
    print(f"词汇题: {len(vocabulary_questions)}题")
    print(f"语法题: {len(grammar_questions)}题")
    print(f"阅读题: {len(reading_questions)}题")
    
    # 分配基础版题目 (50题)
    basic_vocab = vocabulary_questions[:15]  # 前15题词汇
    basic_grammar = grammar_questions[:15]  # 前15题语法
    basic_reading = reading_questions[:20]  # 前20题阅读
    
    # 分配完整版题目 (100题)
    complete_vocab = vocabulary_questions[15:45]  # 剩余30题词汇
    complete_grammar = grammar_questions[15:45]  # 剩余30题语法
    complete_reading = reading_questions[20:60]  # 剩余40题阅读
    
    # 重新组织题目列表
    fixed_questions = []
    
    # 添加版本标识和修复字段名
    for q in basic_vocab + basic_grammar + basic_reading:
        q['version'] = 'basic'
        if 'correct_answer' in q:
            q['answer'] = q.pop('correct_answer')
        fixed_questions.append(q)
    
    for q in complete_vocab + complete_grammar + complete_reading:
        q['version'] = 'complete'
        if 'correct_answer' in q:
            q['answer'] = q.pop('correct_answer')
        fixed_questions.append(q)
    
    # 更新数据
    data['questions'] = fixed_questions
    
    # 更新元数据
    data['metadata']['total_questions'] = len(fixed_questions)
    data['metadata']['question_types'] = {
        'vocabulary': 45,
        'grammar': 45,
        'reading': 60
    }
    data['metadata']['versions'] = {
        'basic': {
            'total_questions': 50,
            'description': '基础版题库',
            'vocabulary': 15,
            'grammar': 15,
            'reading': 20
        },
        'complete': {
            'total_questions': 100,
            'description': '完整版题库',
            'vocabulary': 30,
            'grammar': 30,
            'reading': 40
        }
    }
    
    # 重新计算难度分布
    difficulty_counts = {'easy': 0, 'medium': 0, 'hard': 0}
    exam_type_counts = {'CET4': 0, 'CET6': 0}
    version_counts = {'basic': 0, 'complete': 0}
    
    for q in fixed_questions:
        difficulty_counts[q['difficulty']] += 1
        exam_type_counts[q['exam_type']] += 1
        version_counts[q['version']] += 1
    
    data['metadata']['difficulty_levels'] = difficulty_counts
    data['metadata']['exam_types'] = exam_type_counts
    
    # 保存修复后的文件
    with open('data/cet4_6_questions.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print("\n=== 修复结果 ===")
    print(f"总题数: {len(fixed_questions)}")
    print(f"基础版题目: {version_counts['basic']}题")
    print(f"完整版题目: {version_counts['complete']}题")
    print(f"词汇题: {sum(1 for q in fixed_questions if q['category'] == 'vocabulary')}题")
    print(f"语法题: {sum(1 for q in fixed_questions if q['category'] == 'grammar')}题")
    print(f"阅读题: {sum(1 for q in fixed_questions if q['category'] == 'reading')}题")
    print(f"难度分布: 简单{difficulty_counts['easy']}题, 中等{difficulty_counts['medium']}题, 困难{difficulty_counts['hard']}题")
    print(f"考试类型: CET4{exam_type_counts['CET4']}题, CET6{exam_type_counts['CET6']}题")
    
    # 验证字段完整性
    has_answer = all('answer' in q for q in fixed_questions)
    has_version = all('version' in q for q in fixed_questions)
    
    print(f"\n✅ 所有题目都有answer字段: {has_answer}")
    print(f"✅ 所有题目都有version字段: {has_version}")
    
    if (len(fixed_questions) == 150 and 
        version_counts['basic'] == 50 and 
        version_counts['complete'] == 100 and
        has_answer and has_version):
        print("\n🎉 题库修复完成！所有问题已解决。")
    else:
        print("\n❌ 修复失败，仍有问题。")

if __name__ == "__main__":
    fix_cet4_6_questions()