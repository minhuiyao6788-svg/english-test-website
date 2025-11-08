# 雅思IELTS测试题库JSON结构设计

## 数据结构概述
```json
{
  "metadata": {
    "version": "1.0",
    "created_date": "2025-11-04",
    "total_questions": 100,
    "description": "雅思IELTS测试题库 - 包含词汇、语法、阅读理解三大类型",
    "difficulty_levels": {
      "1": "4.5分及以下（基础水平）",
      "2": "5-5.5分（基础水平，未达到合格）",
      "3": "6-6.5分（基本符合合格水平）",
      "4": "7分及以上（良好水平）"
    },
    "question_types": {
      "vocabulary": "词汇题",
      "grammar": "语法题", 
      "reading": "阅读理解题"
    }
  },
  "basic_version": {
    "total_questions": 50,
    "vocabulary": {
      "count": 15,
      "questions": []
    },
    "grammar": {
      "count": 15,
      "questions": []
    },
    "reading": {
      "count": 20,
      "questions": []
    }
  },
  "complete_version": {
    "total_questions": 100,
    "vocabulary": {
      "count": 30,
      "questions": []
    },
    "grammar": {
      "count": 30,
      "questions": []
    },
    "reading": {
      "count": 40,
      "questions": []
    }
  }
}
```

## 单个题目数据结构
```json
{
  "id": "string - 唯一标识符",
  "type": "string - 题目类型(vocabulary/grammar/reading)",
  "difficulty": "integer - 难度等级(1-4)",
  "knowledge_points": ["array - 知识点标签"],
  "question": "string - 题目内容",
  "options": {
    "A": "string - 选项A",
    "B": "string - 选项B", 
    "C": "string - 选项C",
    "D": "string - 选项D"
  },
  "correct_answer": "string - 正确答案(A/B/C/D)",
  "explanation": "string - 详细解析",
  "reading_passage": {
    "title": "string - 阅读文章标题（如适用）",
    "content": "string - 阅读文章内容（如适用）",
    "word_count": "integer - 字数（如适用）"
  }
}
```

## 知识点标签体系

### 词汇题知识点标签
- "academic_vocabulary" - 学术词汇
- "synonym_recognition" - 同义词识别
- "context_meaning" - 语境含义
- "word_formation" - 构词法
- "collocations" - 搭配用法
- "phrasal_verbs" - 短语动词
- "advanced_vocabulary" - 高级词汇

### 语法题知识点标签
- "sentence_structure" - 句子结构
- "verb_tenses" - 动词时态
- "voice" - 语态
- "modal_verbs" - 情态动词
- "conditionals" - 条件句
- "relative_clauses" - 定语从句
- "adverbial_clauses" - 状语从句
- "passive_voice" - 被动语态
- "reported_speech" - 间接引语
- "complex_sentences" - 复合句

### 阅读理解题知识点标签
- "main_idea" - 中心思想
- "detail_comprehension" - 细节理解
- "inference" - 推理判断
- "word_meaning" - 词义理解
- "text_structure" - 文章结构
- "summary_completion" - 摘要填空
- "true_false_not_given" - 判断题
- "matching_headings" - 标题匹配
- "multiple_choice" - 选择题
- "chart_completion" - 图表完成

## 难度等级设计标准

### 难度1（4.5分及以下）
- 词汇：基础词汇（初中高中水平）
- 语法：基本时态、简单句
- 阅读：简单文章，事实信息

### 难度2（5-5.5分）
- 词汇：中等词汇量，包含部分学术词汇
- 语法：复合句、定语从句
- 阅读：中等难度文章，需要一定推理

### 难度3（6-6.5分）
- 词汇：学术词汇、复杂词汇
- 语法：复杂语法结构、虚拟语气
- 阅读：学术文章，需要深度理解

### 难度4（7分及以上）
- 词汇：高级学术词汇、专业词汇
- 语法：高级语法结构、复杂句式
- 阅读：学术研究文章，需要高级理解能力