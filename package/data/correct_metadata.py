#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
from datetime import datetime

def correct_metadata():
    """修正题库metadata中的分布信息"""
    
    with open('data/cet4_6_questions.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # 重新统计实际分布
    voc_count = sum(1 for q in data['questions'] if q['category'] == 'vocabulary')
    gram_count = sum(1 for q in data['questions'] if q['category'] == 'grammar')
    read_count = sum(1 for q in data['questions'] if q['category'] == 'reading')
    
    # 统计难度分布
    easy_count = sum(1 for q in data['questions'] if q['difficulty'] == 'easy')
    medium_count = sum(1 for q in data['questions'] if q['difficulty'] == 'medium')
    hard_count = sum(1 for q in data['questions'] if q['difficulty'] == 'hard')
    
    # 统计考试类型分布
    cet4_count = sum(1 for q in data['questions'] if q['exam_type'] == 'CET4')
    cet6_count = sum(1 for q in data['questions'] if q['exam_type'] == 'CET6')
    
    # 修正metadata
    data['metadata']['question_types'] = {
        "vocabulary": voc_count,
        "grammar": gram_count,
        "reading": read_count
    }
    
    data['metadata']['difficulty_levels'] = {
        "easy": easy_count,
        "medium": medium_count,
        "hard": hard_count
    }
    
    data['metadata']['exam_types'] = {
        "CET4": cet4_count,
        "CET6": cet6_count
    }
    
    # 保存修正后的文件
    with open('data/cet4_6_questions.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print("=== 修正后的题库统计信息 ===")
    print(f'总题数: {data["metadata"]["total_questions"]}')
    print(f'题目类型分布:')
    for qtype, count in data['metadata']['question_types'].items():
        print(f'  {qtype}: {count}题')
    
    print(f'难度分布:')
    for difficulty, count in data['metadata']['difficulty_levels'].items():
        print(f'  {difficulty}: {count}题')
    
    print(f'考试类型分布:')
    for exam_type, count in data['metadata']['exam_types'].items():
        print(f'  {exam_type}: {count}题')
    
    print(f'版本分布:')
    for version, info in data['metadata']['versions'].items():
        print(f'  {version}: {info["total_questions"]}题')
    
    print(f'\n✅ metadata已修正完成！')

if __name__ == "__main__":
    correct_metadata()