#!/usr/bin/env python3
"""
随机化词汇测试题目的选项顺序
"""

import json
import random

def randomize_vocabulary_options():
    """随机化词汇测试题目的选项顺序"""
    
    # 读取原始题目
    with open('/workspace/english-test-website/public/vocabulary_test_questions.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    questions = data['questions']
    
    # 随机化每道题的选项顺序
    for question in questions:
        # 获取当前选项和正确答案
        options = question['options']
        correct_answer = question['correct_answer']
        
        # 将数字选项转换为列表
        option_items = list(options.items())  # [(key, value), ...]
        
        # 随机打乱选项顺序
        random.shuffle(option_items)
        
        # 重新构建选项
        new_options = {}
        new_correct_index = None
        
        for i, (old_key, value) in enumerate(option_items):
            # 新的选项键（0, 1, 2, 3）
            new_key = str(i)
            new_options[new_key] = value
            
            # 如果这个选项是正确答案，记录新位置
            if old_key == correct_answer:
                new_correct_index = str(i)
        
        # 更新题目
        question['options'] = new_options
        question['correct_answer'] = new_correct_index
        
        print(f"题目 {question['id']}: 正确答案从 {correct_answer} 变为 {new_correct_index}")
    
    # 保存修改后的题目
    with open('/workspace/english-test-website/public/vocabulary_test_questions.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"\n✅ 已随机化 {len(questions)} 道题目的选项顺序")
    print("文件已保存到: /workspace/english-test-website/public/vocabulary_test_questions.json")

if __name__ == "__main__":
    random.seed(42)  # 设置随机种子，确保结果可重现
    randomize_vocabulary_options()