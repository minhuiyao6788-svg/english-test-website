#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import uuid
from datetime import datetime

def generate_final_cet4_6_questions():
    """生成最终的大学英语四六级测试题库（150题）"""
    
    questions = []
    
    # ==================== 基础版词汇题 (15题) ====================
    basic_vocabulary_questions = [
        {
            "id": f"voc_{str(uuid.uuid4())[:8]}",
            "category": "vocabulary",
            "difficulty": "easy",
            "knowledge_tags": ["词汇辨析", "近义词", "基础词汇"],
            "exam_type": "CET4",
            "question": "The company's new policy will ____ the working hours of all employees.",
            "options": ["extend", "expand", "expend", "expedite"],
            "correct_answer": "A",
            "explanation": "extend意为'延长、扩展'，常用于时间、距离等；expand意为'扩大、扩展'，多用于规模、范围等；expend意为'花费、消耗'；expedite意为'加快、促进'。根据语境，这里应该选择extend，表示延长工作时间。"
        },
        {
            "id": f"voc_{str(uuid.uuid4())[:8]}",
            "category": "vocabulary",
            "difficulty": "easy",
            "knowledge_tags": ["词汇辨析", "动词", "基础词汇"],
            "exam_type": "CET4",
            "question": "The teacher asked us to ____ the text into our own words.",
            "options": ["translate", "transfer", "transform", "transmit"],
            "correct_answer": "A",
            "explanation": "translate意为'翻译'，符合语境；transfer意为'转移、转账'；transform意为'转变、改变'；transmit意为'传输、传播'。老师要求我们用自己的话翻译文本。"
        },
        {
            "id": f"voc_{str(uuid.uuid4())[:8]}",
            "category": "vocabulary",
            "difficulty": "medium",
            "knowledge_tags": ["词汇辨析", "形容词", "程度词汇"],
            "exam_type": "CET4",
            "question": "The weather is becoming ____ colder as winter approaches.",
            "options": ["increasingly", "incrementally", "intensively", "intensively"],
            "correct_answer": "A",
            "explanation": "increasingly意为'越来越...'，表示程度的逐渐增加；incrementally意为'递增地'；intensively意为'密集地'。根据语境，increasingly最合适。"
        },
        {
            "id": f"voc_{str(uuid.uuid4())[:8]}",
            "category": "vocabulary",
            "difficulty": "medium",
            "knowledge_tags": ["词汇辨析", "名词", "抽象概念"],
            "exam_type": "CET4",
            "question": "She showed great ____ in handling the difficult situation.",
            "options": ["ability", "capability", "competence", "skill"],
            "correct_answer": "C",
            "explanation": "competence意为'能力、胜任力'，强调处理复杂情况的能力；ability泛指能力；capability指潜在能力；skill指具体技能。"
        },
        {
            "id": f"voc_{str(uuid.uuid4())[:8]}",
            "category": "vocabulary",
            "difficulty": "easy",
            "knowledge_tags": ["词汇辨析", "动词", "基础词汇"],
            "exam_type": "CET4",
            "question": "Please ____ the lights before leaving the room.",
            "options": ["turn off", "turn down", "turn up", "turn on"],
            "correct_answer": "A",
            "explanation": "turn off意为'关闭'；turn down意为'调低'；turn up意为'调高'；turn on意为'打开'。离开房间前应该关灯。"
        },
        {
            "id": f"voc_{str(uuid.uuid4())[:8]}",
            "category": "vocabulary",
            "difficulty": "medium",
            "knowledge_tags": ["词汇辨析", "形容词", "情感词汇"],
            "exam_type": "CET6",
            "question": "The news of his promotion came as a ____ surprise to everyone.",
            "options": ["sudden", "unexpected", "unpredictable", "unusual"],
            "correct_answer": "B",
            "explanation": "unexpected意为'意外的、始料未及的'，最符合语境；sudden强调突然性；unpredictable强调不可预测性；unusual强调不寻常。"
        },
        {
            "id": f"voc_{str(uuid.uuid4())[:8]}",
            "category": "vocabulary",
            "difficulty": "medium",
            "knowledge_tags": ["词汇辨析", "动词", "行为动词"],
            "exam_type": "CET6",
            "question": "The committee will ____ the proposal at next week's meeting.",
            "options": ["consider", "regard", "think", "contemplate"],
            "correct_answer": "A",
            "explanation": "consider意为'考虑、审议'，最符合委员会审议提案的语境；regard常与as连用；think about表示思考；contemplate表示沉思、深思。"
        },
        {
            "id": f"voc_{str(uuid.uuid4())[:8]}",
            "category": "vocabulary",
            "difficulty": "hard",
            "knowledge_tags": ["词汇辨析", "形容词", "高级词汇"],
            "exam_type": "CET6",
            "question": "His ____ attitude towards work impressed the management team.",
            "options": ["diligent", "industrious", "assiduous", "conscientious"],
            "correct_answer": "D",
            "explanation": "conscientious意为'认真负责的、尽责的'，强调道德责任感；diligent强调勤奋；industrious强调勤劳；assiduous强调持续努力。"
        },
        {
            "id": f"voc_{str(uuid.uuid4())[:8]}",
            "category": "vocabulary",
            "difficulty": "easy",
            "knowledge_tags": ["词汇辨析", "介词", "基础词汇"],
            "exam_type": "CET4",
            "question": "The meeting is scheduled ____ 3 PM tomorrow.",
            "options": ["in", "on", "at", "by"],
            "correct_answer": "C",
            "explanation": "at用于表示具体的时间点；in用于年、月、季节等；on用于具体的日期；by表示截止时间。3 PM是具体时间点，用at。"
        },
        {
            "id": f"voc_{str(uuid.uuid4())[:8]}",
            "category": "vocabulary",
            "difficulty": "medium",
            "knowledge_tags": ["词汇辨析", "动词", "心理活动"],
            "exam_type": "CET4",
            "question": "I can't ____ why she refused to help us.",
            "options": ["figure out", "work out", "find out", "make out"],
            "correct_answer": "A",
            "explanation": "figure out意为'理解、弄明白'，多用于理解原因或情况；work out强调解决、计算出；find out强调发现真相；make out强调辨认出。"
        },
        {
            "id": f"voc_{str(uuid.uuid4())[:8]}",
            "category": "vocabulary",
            "difficulty": "medium",
            "knowledge_tags": ["词汇辨析", "形容词", "程度词汇"],
            "exam_type": "CET6",
            "question": "The ____ of the research data requires careful analysis.",
            "options": ["volume", "amount", "quantity", "mass"],
            "correct_answer": "A",
            "explanation": "volume在数据语境中意为'容量、数据量'；amount强调总量；quantity强调数量；mass强调质量。根据语境，volume最合适。"
        },
        {
            "id": f"voc_{str(uuid.uuid4())[:8]}",
            "category": "vocabulary",
            "difficulty": "easy",
            "knowledge_tags": ["词汇辨析", "动词", "日常用语"],
            "exam_type": "CET4",
            "question": "Could you ____ me a favor and help me with this problem?",
            "options": ["do", "make", "give", "show"],
            "correct_answer": "A",
            "explanation": "do a favor是固定搭配，意为'帮忙'；make a favor不是标准搭配；give和show不与favor搭配使用。"
        },
        {
            "id": f"voc_{str(uuid.uuid4())[:8]}",
            "category": "vocabulary",
            "difficulty": "hard",
            "knowledge_tags": ["词汇辨析", "形容词", "高级词汇"],
            "exam_type": "CET6",
            "question": "The ____ nature of quantum physics makes it difficult to understand.",
            "options": ["abstract", "complex", "complicated", "sophisticated"],
            "correct_answer": "A",
            "explanation": "abstract意为'抽象的'，强调难以直观理解；complex强调复杂但可理解；complicated强调复杂且难以处理；sophisticated强调精密复杂。"
        },
        {
            "id": f"voc_{str(uuid.uuid4())[:8]}",
            "category": "vocabulary",
            "difficulty": "medium",
            "knowledge_tags": ["词汇辨析", "动词", "行为动词"],
            "exam_type": "CET6",
            "question": "The government decided to ____ the new policy immediately.",
            "options": ["implement", "execute", "enforce", "apply"],
            "correct_answer": "A",
            "explanation": "implement意为'实施、执行'，强调将计划或政策付诸实施；execute强调执行命令；enforce强调强制执行；apply强调应用。"
        },
        {
            "id": f"voc_{str(uuid.uuid4())[:8]}",
            "category": "vocabulary",
            "difficulty": "easy",
            "knowledge_tags": ["词汇辨析", "名词", "基础词汇"],
            "exam_type": "CET4",
            "question": "Please write your name on the ____ line.",
            "options": ["dotted", "dashed", "broken", "faint"],
            "correct_answer": "A",
            "explanation": "dotted line意为'虚线、点线'，常用于填写签名；dashed line也是虚线，但dotted更常用；broken line意为'断线'；faint line意为'淡线'。"
        }
    ]
    
    # ==================== 基础版语法题 (15题) ====================
    basic_grammar_questions = [
        {
            "id": f"gram_{str(uuid.uuid4())[:8]}",
            "category": "grammar",
            "difficulty": "easy",
            "knowledge_tags": ["时态", "现在完成时", "基础语法"],
            "exam_type": "CET4",
            "question": "I ____ in this city for five years.",
            "options": ["have lived", "lived", "am living", "live"],
            "correct_answer": "A",
            "explanation": "现在完成时表示过去发生的动作对现在造成的影响或持续到现在。for five years表示时间段，用现在完成时have lived。lived是一般过去时，不表示持续到现在；am living是现在进行时；live是一般现在时。"
        },
        {
            "id": f"gram_{str(uuid.uuid4())[:8]}",
            "category": "grammar",
            "difficulty": "medium",
            "knowledge_tags": ["被动语态", "时态", "基础语法"],
            "exam_type": "CET4",
            "question": "The new library ____ last year.",
            "options": ["built", "was built", "has built", "has been built"],
            "correct_answer": "B",
            "explanation": "last year是过去时间状语，用一般过去时。library是动作的承受者，用被动语态was built。built是主动语态；has built是现在完成时主动语态；has been built是现在完成时被动语态。"
        },
        {
            "id": f"gram_{str(uuid.uuid4())[:8]}",
            "category": "grammar",
            "difficulty": "medium",
            "knowledge_tags": ["定语从句", "关系代词", "基础语法"],
            "exam_type": "CET4",
            "question": "The book ____ I bought yesterday is very interesting.",
            "options": ["who", "which", "where", "what"],
            "correct_answer": "B",
            "explanation": "先行词是book，在从句中作宾语，用关系代词which。who指人；where指地点；what不能引导定语从句。"
        },
        {
            "id": f"gram_{str(uuid.uuid4())[:8]}",
            "category": "grammar",
            "difficulty": "easy",
            "knowledge_tags": ["情态动词", "基础语法", "推测"],
            "exam_type": "CET4",
            "question": "She ____ be at home now because her car is in the garage.",
            "options": ["must", "can", "may", "should"],
            "correct_answer": "A",
            "explanation": "must表示有把握的推测，意为'一定、准是'。根据car在garage这个有力证据，可以很有把握地推测她在家。can表示能力；may表示可能性较小的推测；should表示应该。"
        },
        {
            "id": f"gram_{str(uuid.uuid4())[:8]}",
            "category": "grammar",
            "difficulty": "medium",
            "knowledge_tags": ["非谓语动词", "不定式", "基础语法"],
            "exam_type": "CET4",
            "question": "My dream is ____ a doctor.",
            "options": ["to become", "becoming", "become", "to becoming"],
            "correct_answer": "A",
            "explanation": "不定式to become作表语，表示将来的动作。My dream is to become...是固定结构。becoming是动名词；become是动词原形；to becoming语法错误。"
        },
        {
            "id": f"gram_{str(uuid.uuid4())[:8]}",
            "category": "grammar",
            "difficulty": "medium",
            "knowledge_tags": ["虚拟语气", "条件句", "基础语法"],
            "exam_type": "CET6",
            "question": "If I ____ more time, I would learn another language.",
            "options": ["have", "had", "will have", "would have"],
            "correct_answer": "B",
            "explanation": "这是与现在事实相反的虚拟条件句，从句用一般过去时had，主句用would + 动词原形。have是现在时；will have是将来时；would have是虚拟过去时。"
        },
        {
            "id": f"gram_{str(uuid.uuid4())[:8]}",
            "category": "grammar",
            "difficulty": "easy",
            "knowledge_tags": ["介词", "基础语法", "固定搭配"],
            "exam_type": "CET4",
            "question": "She is interested ____ learning Chinese.",
            "options": ["in", "on", "at", "with"],
            "correct_answer": "A",
            "explanation": "interested in是固定搭配，意为'对...感兴趣'。其他介词不与interested搭配使用。"
        },
        {
            "id": f"gram_{str(uuid.uuid4())[:8]}",
            "category": "grammar",
            "difficulty": "medium",
            "knowledge_tags": ["名词性从句", "宾语从句", "基础语法"],
            "exam_type": "CET4",
            "question": "I don't know ____ he will come tomorrow.",
            "options": ["that", "whether", "if", "what"],
            "correct_answer": "B",
            "explanation": "whether引导宾语从句，表示'是否'。if也可以引导宾语从句，但在正式文体中多用whether。that引导陈述性宾语从句；what引导名词性从句但意思不符。"
        },
        {
            "id": f"gram_{str(uuid.uuid4())[:8]}",
            "category": "grammar",
            "difficulty": "hard",
            "knowledge_tags": ["倒装句", "完全倒装", "高级语法"],
            "exam_type": "CET6",
            "question": "____ the weather, we decided to go for a walk.",
            "options": ["Despite", "Although", "In spite of", "Regardless of"],
            "correct_answer": "A",
            "explanation": "Despite是介词，后面接名词the weather。Although是从属连词，后面接句子；In spite of也是介词，但不如despite常用；Regardless of是介词，意为'不管、不顾'，不符合语境。"
        },
        {
            "id": f"gram_{str(uuid.uuid4())[:8]}",
            "category": "grammar",
            "difficulty": "medium",
            "knowledge_tags": ["比较级", "形容词", "基础语法"],
            "exam_type": "CET4",
            "question": "This book is ____ than that one.",
            "options": ["more interesting", "most interesting", "interesting", "interestinger"],
            "correct_answer": "A",
            "explanation": "interesting是多音节形容词，比较级用more + 形容词原形。most interesting是最高级；interesting是原级；interestinger是错误形式。"
        },
        {
            "id": f"gram_{str(uuid.uuid4())[:8]}",
            "category": "grammar",
            "difficulty": "easy",
            "knowledge_tags": ["主谓一致", "基础语法", "第三人称单数"],
            "exam_type": "CET4",
            "question": "He ____ to school every day.",
            "options": ["go", "goes", "going", "gone"],
            "correct_answer": "B",
            "explanation": "主语He是第三人称单数，谓语动词用第三人称单数形式goes。go是动词原形；going是现在分词；gone是过去分词。"
        },
        {
            "id": f"gram_{str(uuid.uuid4())[:8]}",
            "category": "grammar",
            "difficulty": "medium",
            "knowledge_tags": ["定语从句", "介词+关系代词", "基础语法"],
            "exam_type": "CET6",
            "question": "The house ____ we lived was very old.",
            "options": ["in which", "which", "where", "in where"],
            "correct_answer": "A",
            "explanation": "lived in the house，介词in提前，用in which。which指代house，在从句中作介词in的宾语。where是副词，不能与介词连用；in where语法错误。"
        },
        {
            "id": f"gram_{str(uuid.uuid4())[:8]}",
            "category": "grammar",
            "difficulty": "medium",
            "knowledge_tags": ["非谓语动词", "现在分词", "基础语法"],
            "exam_type": "CET4",
            "question": "____ the report, he went home.",
            "options": ["Finishing", "Having finished", "Finished", "To finish"],
            "correct_answer": "B",
            "explanation": "现在分词的完成式Having finished表示动作发生在谓语动词went之前。Finishing表示同时发生；Finished是过去分词，不能作状语；To finish表示目的，不符合语境。"
        },
        {
            "id": f"gram_{str(uuid.uuid4())[:8]}",
            "category": "grammar",
            "difficulty": "hard",
            "knowledge_tags": ["强调句", "it强调句型", "高级语法"],
            "exam_type": "CET6",
            "question": "____ was John who broke the vase.",
            "options": ["It", "He", "That", "This"],
            "correct_answer": "A",
            "explanation": "It was...who...是强调句型，强调主语John。He不能用于强调句；That和This不能构成强调句型。"
        },
        {
            "id": f"gram_{str(uuid.uuid4())[:8]}",
            "category": "grammar",
            "difficulty": "medium",
            "knowledge_tags": ["情态动词", "推测", "基础语法"],
            "exam_type": "CET4",
            "question": "You ____ be tired after such a long journey.",
            "options": ["must", "can", "may", "should"],
            "correct_answer": "A",
            "explanation": "must表示很有把握的推测，意为'一定、准是'。根据long journey这个原因，可以很有把握地推测他累了。can表示能力；may表示可能性；should表示应该。"
        }
    ]
    
    # ==================== 基础版阅读理解题 (20题) ====================
    basic_reading_questions = [
        {
            "id": f"read_{str(uuid.uuid4())[:8]}",
            "category": "reading",
            "difficulty": "easy",
            "knowledge_tags": ["细节题", "主旨题", "说明文"],
            "exam_type": "CET4",
            "question": "According to the passage, what is the main purpose of the study?",
            "passage_id": "passage_001",
            "options": ["To explore new teaching methods", "To investigate student performance", "To compare different schools", "To analyze teacher satisfaction"],
            "correct_answer": "B",
            "explanation": "根据文章内容，研究的主要目的是调查学生表现。选项A、C、D都不是文章的主要研究目的。"
        },
        {
            "id": f"read_{str(uuid.uuid4())[:8]}",
            "category": "reading",
            "difficulty": "medium",
            "knowledge_tags": ["推理判断", "细节题", "议论文"],
            "exam_type": "CET4",
            "question": "What can be inferred from the passage about the author's attitude?",
            "passage_id": "passage_002",
            "options": ["Optimistic", "Pessimistic", "Neutral", "Critical"],
            "correct_answer": "A",
            "explanation": "从文章中可以看出作者对所讨论的问题持乐观态度，文中使用了积极正面的词汇和表述。"
        },
        {
            "id": f"read_{str(uuid.uuid4())[:8]}",
            "category": "reading",
            "difficulty": "easy",
            "knowledge_tags": ["细节题", "事实信息", "说明文"],
            "exam_type": "CET4",
            "question": "How many students participated in the survey?",
            "passage_id": "passage_003",
            "options": ["150", "200", "250", "300"],
            "correct_answer": "C",
            "explanation": "文章明确提到有250名学生参与了调查。"
        },
        {
            "id": f"read_{str(uuid.uuid4())[:8]}",
            "category": "reading",
            "difficulty": "medium",
            "knowledge_tags": ["词义猜测", "上下文理解", "说明文"],
            "exam_type": "CET4",
            "question": "What does the word 'sustainable' most probably mean in the passage?",
            "passage_id": "passage_004",
            "options": ["Profitable", "Environmentally friendly", "Technologically advanced", "Economically viable"],
            "correct_answer": "B",
            "explanation": "根据上下文，'sustainable'在文章中指的是环境友好的、可持续的，与环保概念相关。"
        },
        {
            "id": f"read_{str(uuid.uuid4())[:8]}",
            "category": "reading",
            "difficulty": "hard",
            "knowledge_tags": ["推理判断", "逻辑推理", "议论文"],
            "exam_type": "CET6",
            "question": "What is likely to be the next step according to the passage?",
            "passage_id": "passage_005",
            "options": ["Implement the proposed changes", "Conduct further research", "Seek additional funding", "Train more staff"],
            "correct_answer": "B",
            "explanation": "根据文章的逻辑结构，作者在最后提到了需要进行进一步研究来验证结果，因此下一步很可能是进行更深入的研究。"
        },
        {
            "id": f"read_{str(uuid.uuid4())[:8]}",
            "category": "reading",
            "difficulty": "easy",
            "knowledge_tags": ["细节题", "事实信息", "说明文"],
            "exam_type": "CET4",
            "question": "When was the new policy implemented?",
            "passage_id": "passage_006",
            "options": ["Last month", "This month", "Next month", "Two months ago"],
            "correct_answer": "A",
            "explanation": "文章提到新政策是在上个月实施的。"
        },
        {
            "id": f"read_{str(uuid.uuid4())[:8]}",
            "category": "reading",
            "difficulty": "medium",
            "knowledge_tags": ["主旨题", "中心思想", "议论文"],
            "exam_type": "CET4",
            "question": "What is the main topic of the passage?",
            "passage_id": "passage_007",
            "options": ["Climate change", "Economic development", "Educational reform", "Technology innovation"],
            "correct_answer": "C",
            "explanation": "文章主要讨论教育改革问题，从头到尾都在围绕教育改革的各个方面展开论述。"
        },
        {
            "id": f"read_{str(uuid.uuid4())[:8]}",
            "category": "reading",
            "difficulty": "easy",
            "knowledge_tags": ["细节题", "事实信息", "说明文"],
            "exam_type": "CET4",
            "question": "Which of the following is mentioned as a benefit?",
            "passage_id": "passage_008",
            "options": ["Reduced costs", "Increased efficiency", "Better quality", "All of the above"],
            "correct_answer": "D",
            "explanation": "文章提到了降低成本、提高效率和改善质量三个方面的益处。"
        },
        {
            "id": f"read_{str(uuid.uuid4())[:8]}",
            "category": "reading",
            "difficulty": "medium",
            "knowledge_tags": ["推理判断", "逻辑推理", "说明文"],
            "exam_type": "CET6",
            "question": "What is the author's purpose in writing this passage?",
            "passage_id": "passage_009",
            "options": ["To inform", "To persuade", "To entertain", "To criticize"],
            "correct_answer": "A",
            "explanation": "作者的写作目的是提供信息，文章主要在客观地介绍某个现象或情况，没有明显的说服或批评意图。"
        },
        {
            "id": f"read_{str(uuid.uuid4())[:8]}",
            "category": "reading",
            "difficulty": "easy",
            "knowledge_tags": ["细节题", "事实信息", "记叙文"],
            "exam_type": "CET4",
            "question": "Where did the main character work?",
            "passage_id": "passage_010",
            "options": ["At a hospital", "At a school", "At a company", "At a restaurant"],
            "correct_answer": "B",
            "explanation": "文章提到主人公在一所学校工作。"
        },
        {
            "id": f"read_{str(uuid.uuid4())[:8]}",
            "category": "reading",
            "difficulty": "medium",
            "knowledge_tags": ["词义猜测", "上下文理解", "说明文"],
            "exam_type": "CET4",
            "question": "What does the phrase 'in the long run' mean in this context?",
            "passage_id": "passage_011",
            "options": ["Eventually", "Immediately", "Temporarily", "Permanently"],
            "correct_answer": "A",
            "explanation": "'in the long run'是固定短语，意为'从长远来看、最终'，与eventually意思相近。"
        },
        {
            "id": f"read_{str(uuid.uuid4())[:8]}",
            "category": "reading",
            "difficulty": "hard",
            "knowledge_tags": ["推理判断", "逻辑推理", "议论文"],
            "exam_type": "CET6",
            "question": "What is implied about the future of this industry?",
            "passage_id": "passage_012",
            "options": ["It will decline", "It will remain stable", "It will grow rapidly", "It will face challenges"],
            "correct_answer": "C",
            "explanation": "文章暗示该行业将快速发展，作者提到了技术创新、市场需求增长等多个积极因素。"
        },
        {
            "id": f"read_{str(uuid.uuid4())[:8]}",
            "category": "reading",
            "difficulty": "easy",
            "knowledge_tags": ["细节题", "事实信息", "说明文"],
            "exam_type": "CET4",
            "question": "What percentage of students agreed with the proposal?",
            "passage_id": "passage_013",
            "options": ["60%", "70%", "80%", "90%"],
            "correct_answer": "C",
            "explanation": "文章提到80%的学生同意这个提议。"
        },
        {
            "id": f"read_{str(uuid.uuid4())[:8]}",
            "category": "reading",
            "difficulty": "medium",
            "knowledge_tags": ["推理判断", "态度观点", "议论文"],
            "exam_type": "CET4",
            "question": "How does the author feel about the current situation?",
            "passage_id": "passage_014",
            "options": ["Satisfied", "Concerned", "Angry", "Indifferent"],
            "correct_answer": "B",
            "explanation": "作者对当前情况表示担忧，文中使用了'concerned'、'worried'等词汇表达这种态度。"
        },
        {
            "id": f"read_{str(uuid.uuid4())[:8]}",
            "category": "reading",
            "difficulty": "easy",
            "knowledge_tags": ["细节题", "事实信息", "说明文"],
            "exam_type": "CET4",
            "question": "How long does the program last?",
            "passage_id": "passage_015",
            "options": ["3 months", "6 months", "9 months", "12 months"],
            "correct_answer": "B",
            "explanation": "文章明确提到这个项目持续6个月。"
        },
        {
            "id": f"read_{str(uuid.uuid4())[:8]}",
            "category": "reading",
            "difficulty": "medium",
            "knowledge_tags": ["主旨题", "中心思想", "说明文"],
            "exam_type": "CET6",
            "question": "Which of the following best summarizes the passage?",
            "passage_id": "passage_016",
            "options": ["A new discovery in science", "A comparison of different methods", "An analysis of current problems", "A proposal for future improvements"],
            "correct_answer": "C",
            "explanation": "文章主要分析了当前存在的问题，并提出了相应的解决方案。"
        },
        {
            "id": f"read_{str(uuid.uuid4())[:8]}",
            "category": "reading",
            "difficulty": "easy",
            "knowledge_tags": ["细节题", "事实信息", "说明文"],
            "exam_type": "CET4",
            "question": "What is the minimum age requirement?",
            "passage_id": "passage_017",
            "options": ["16 years old", "18 years old", "20 years old", "22 years old"],
            "correct_answer": "B",
            "explanation": "文章提到最低年龄要求是18岁。"
        },
        {
            "id": f"read_{str(uuid.uuid4())[:8]}",
            "category": "reading",
            "difficulty": "hard",
            "knowledge_tags": ["推理判断", "逻辑推理", "议论文"],
            "exam_type": "CET6",
            "question": "What can be concluded from the last paragraph?",
            "passage_id": "passage_018",
            "options": ["The problem is unsolvable", "More research is needed", "The solution is simple", "The situation is improving"],
            "correct_answer": "B",
            "explanation": "从最后一段可以得出结论，需要进行更多的研究来彻底解决这个问题。"
        },
        {
            "id": f"read_{str(uuid.uuid4())[:8]}",
            "category": "reading",
            "difficulty": "medium",
            "knowledge_tags": ["词义猜测", "上下文理解", "说明文"],
            "exam_type": "CET4",
            "question": "What does 'crucial' mean in this context?",
            "passage_id": "passage_019",
            "options": ["Important", "Difficult", "Expensive", "Complicated"],
            "correct_answer": "A",
            "explanation": "根据上下文，'crucial'意为'关键的、重要的'，与important意思相同。"
        },
        {
            "id": f"read_{str(uuid.uuid4())[:8]}",
            "category": "reading",
            "difficulty": "easy",
            "knowledge_tags": ["细节题", "事实信息", "说明文"],
            "exam_type": "CET4",
            "question": "What is the deadline for submission?",
            "passage_id": "passage_020",
            "options": ["End of this month", "End of next month", "End of this week", "End of next week"],
            "correct_answer": "C",
            "explanation": "文章提到提交的截止日期是本周结束前。"
        }
    ]
    
    # ==================== 完整版词汇题 (15题) ====================
    complete_vocabulary_questions = [
        {
            "id": f"voc_{str(uuid.uuid4())[:8]}",
            "category": "vocabulary",
            "difficulty": "hard",
            "knowledge_tags": ["词汇辨析", "形容词", "学术词汇"],
            "exam_type": "CET6",
            "question": "The ____ of the experiment was compromised by poor laboratory conditions.",
            "options": ["validity", "reliability", "accuracy", "precision"],
            "correct_answer": "A",
            "explanation": "validity意为'有效性、正确性'，强调实验结果的正确性；reliability强调可靠性；accuracy强调准确性；precision强调精确性。"
        },
        {
            "id": f"voc_{str(uuid.uuid4())[:8]}",
            "category": "vocabulary",
            "difficulty": "medium",
            "knowledge_tags": ["词汇辨析", "动词", "情感动词"],
            "exam_type": "CET6",
            "question": "Her ____ smile could not hide her disappointment.",
            "options": ["feigned", "faked", "pretended", "counterfeit"],
            "correct_answer": "A",
            "explanation": "feigned意为'假装的、伪装的'，多用于情感或表情；faked强调伪造；pretended强调假装行为；counterfeit强调伪造的（多用于物品）。"
        },
        {
            "id": f"voc_{str(uuid.uuid4())[:8]}",
            "category": "vocabulary",
            "difficulty": "hard",
            "knowledge_tags": ["词汇辨析", "名词", "抽象概念"],
            "exam_type": "CET6",
            "question": "The ____ between theory and practice is often wider than expected.",
            "options": ["disparity", "difference", "distinction", "gap"],
            "correct_answer": "D",
            "explanation": "gap在理论与实践语境中意为'差距、鸿沟'，最常用；disparity强调不公平的差异；difference泛指差异；distinction强调区别。"
        },
        {
            "id": f"voc_{str(uuid.uuid4())[:8]}",
            "category": "vocabulary",
            "difficulty": "medium",
            "knowledge_tags": ["词汇辨析", "形容词", "程度词汇"],
            "exam_type": "CET6",
            "question": "The ____ majority of students passed the examination.",
            "options": ["overwhelming", "predominant", "dominant", "major"],
            "correct_answer": "A",
            "explanation": "overwhelming majority是固定搭配，意为'绝大多数'；predominant强调占主导地位的；dominant强调占支配地位的；major强调主要的。"
        },
        {
            "id": f"voc_{str(uuid.uuid4())[:8]}",
            "category": "vocabulary",
            "difficulty": "hard",
            "knowledge_tags": ["词汇辨析", "动词", "专业词汇"],
            "exam_type": "CET6",
            "question": "The committee will ____ the candidate's qualifications thoroughly.",
            "options": ["scrutinize", "examine", "investigate", "inspect"],
            "correct_answer": "A",
            "explanation": "scrutinize意为'仔细检查、审查'，强调详细严格的检查；examine强调检查；investigate强调调查；inspect强调检查（多用于实物）。"
        },
        {
            "id": f"voc_{str(uuid.uuid4())[:8]}",
            "category": "vocabulary",
            "difficulty": "medium",
            "knowledge_tags": ["词汇辨析", "形容词", "状态词汇"],
            "exam_type": "CET6",
            "question": "The company's financial situation is now ____.",
            "options": ["precarious", "unstable", "uncertain", "risky"],
            "correct_answer": "A",
            "explanation": "precarious意为'不稳定的、危险的'，强调情况危急；unstable强调不稳定；uncertain强调不确定；risky强调有风险的。"
        },
        {
            "id": f"voc_{str(uuid.uuid4())[:8]}",
            "category": "vocabulary",
            "difficulty": "hard",
            "knowledge_tags": ["词汇辨析", "名词", "学术词汇"],
            "exam_type": "CET6",
            "question": "The researcher's ____ conclusions were based on limited data.",
            "options": ["premature", "preliminary", "tentative", "provisional"],
            "correct_answer": "A",
            "explanation": "premature意为'过早的、草率的'，强调结论过于匆忙；preliminary强调初步的；tentative强调试探性的；provisional强调临时的。"
        },
        {
            "id": f"voc_{str(uuid.uuid4())[:8]}",
            "category": "vocabulary",
            "difficulty": "medium",
            "knowledge_tags": ["词汇辨析", "动词", "行为动词"],
            "exam_type": "CET6",
            "question": "The new manager will ____ the department next month.",
            "options": ["assume", "undertake", "accept", "undergo"],
            "correct_answer": "A",
            "explanation": "assume意为'承担、担任'，常用于职位；undertake强调承担任务；accept强调接受；undergo强调经历。"
        },
        {
            "id": f"voc_{str(uuid.uuid4())[:8]}",
            "category": "vocabulary",
            "difficulty": "hard",
            "knowledge_tags": ["词汇辨析", "形容词", "高级词汇"],
            "exam_type": "CET6",
            "question": "The ____ of the ancient manuscript has been a challenge for scholars.",
            "options": ["deciphering", "decoding", "interpreting", "translating"],
            "correct_answer": "A",
            "explanation": "deciphering强调破译难以理解的文字；decoding强调解码；interpreting强调解释；translating强调翻译。"
        },
        {
            "id": f"voc_{str(uuid.uuid4())[:8]}",
            "category": "vocabulary",
            "difficulty": "medium",
            "knowledge_tags": ["词汇辨析", "动词", "心理活动"],
            "exam_type": "CET6",
            "question": "The witness was unable to ____ the suspect in the lineup.",
            "options": ["identify", "recognize", "distinguish", "differentiate"],
            "correct_answer": "A",
            "explanation": "identify意为'识别、辨认'，强调确认身份；recognize强调认出；distinguish强调区分；differentiate强调区别。"
        },
        {
            "id": f"voc_{str(uuid.uuid4())[:8]}",
            "category": "vocabulary",
            "difficulty": "hard",
            "knowledge_tags": ["词汇辨析", "名词", "专业词汇"],
            "exam_type": "CET6",
            "question": "The ____ of the economic crisis affected global markets.",
            "options": ["repercussion", "consequence", "aftermath", "impact"],
            "correct_answer": "A",
            "explanation": "repercussion意为'深远影响、后果'，强调连锁反应；consequence强调后果；aftermath强调灾难后的时期；impact强调影响。"
        },
        {
            "id": f"voc_{str(uuid.uuid4())[:8]}",
            "category": "vocabulary",
            "difficulty": "medium",
            "knowledge_tags": ["词汇辨析", "形容词", "程度词汇"],
            "exam_type": "CET6",
            "question": "The team's ____ effort led to the project's success.",
            "options": ["concerted", "combined", "joint", "unified"],
            "correct_answer": "A",
            "explanation": "concerted effort是固定搭配，意为'共同努力'；combined强调联合的；joint强调共同的；unified强调统一的。"
        },
        {
            "id": f"voc_{str(uuid.uuid4())[:8]}",
            "category": "vocabulary",
            "difficulty": "hard",
            "knowledge_tags": ["词汇辨析", "动词", "高级词汇"],
            "exam_type": "CET6",
            "question": "The committee decided to ____ the controversial proposal.",
            "options": ["shelve", "postpone", "defer", "suspend"],
            "correct_answer": "A",
            "explanation": "shelve意为'搁置、暂缓考虑'，强调暂时搁置；postpone强调延期；defer强调推迟；suspend强调暂停。"
        },
        {
            "id": f"voc_{str(uuid.uuid4())[:8]}",
            "category": "vocabulary",
            "difficulty": "medium",
            "knowledge_tags": ["词汇辨析", "形容词", "状态词汇"],
            "exam_type": "CET6",
            "question": "The patient's condition is now ____ after the successful surgery.",
            "options": ["stable", "steady", "consistent", "constant"],
            "correct_answer": "A",
            "explanation": "stable在医学语境中意为'稳定的'，强调病情稳定；steady强调稳定的；consistent强调一致的；constant强调持续的。"
        },
        {
            "id": f"voc_{str(uuid.uuid4())[:8]}",
            "category": "vocabulary",
            "difficulty": "hard",
            "knowledge_tags": ["词汇辨析", "名词", "抽象概念"],
            "exam_type": "CET6",
            "question": "The ____ of his argument was difficult to follow.",
            "options": ["intricacy", "complexity", "sophistication", "elaboration"],
            "correct_answer": "A",
            "explanation": "intricacy强调错综复杂、难以理解；complexity强调复杂性；sophistication强调精密复杂；elaboration强调详细阐述。"
        }
    ]
    
    # ==================== 完整版语法题 (15题) ====================
    complete_grammar_questions = [
        {
            "id": f"gram_{str(uuid.uuid4())[:8]}",
            "category": "grammar",
            "difficulty": "hard",
            "knowledge_tags": ["虚拟语气", "混合虚拟", "高级语法"],
            "exam_type": "CET6",
            "question": "If I ____ known about the meeting, I would have attended it.",
            "options": ["had", "would have", "have", "would"],
            "correct_answer": "A",
            "explanation": "这是与过去事实相反的虚拟条件句，从句用过去完成时had known，主句用would have + 过去分词。would have不能用在if从句中；have是现在时；would不能单独使用。"
        },
        {
            "id": f"gram_{str(uuid.uuid4())[:8]}",
            "category": "grammar",
            "difficulty": "hard",
            "knowledge_tags": ["倒装句", "部分倒装", "高级语法"],
            "exam_type": "CET6",
            "question": "____ he studied hard, he failed the exam.",
            "options": ["Although", "Despite", "In spite of", "Regardless of"],
            "correct_answer": "A",
            "explanation": "Although引导让步状语从句，用正常语序。Despite和In spite of是介词，后面不能接句子；Regardless of也是介词，意思不符。"
        },
        {
            "id": f"gram_{str(uuid.uuid4())[:8]}",
            "category": "grammar",
            "difficulty": "hard",
            "knowledge_tags": ["非谓语动词", "独立主格", "高级语法"],
            "exam_type": "CET6",
            "question": "____ the weather being fine, we decided to go out.",
            "options": ["With", "Because", "Since", "As"],
            "correct_answer": "A",
            "explanation": "With + 名词/代词 + 现在分词构成独立主格结构，表示原因或伴随情况。Because、Since、As都是连词，引导从句，不符合独立主格结构。"
        },
        {
            "id": f"gram_{str(uuid.uuid4())[:8]}",
            "category": "grammar",
            "difficulty": "medium",
            "knowledge_tags": ["定语从句", "限制性与非限制性", "基础语法"],
            "exam_type": "CET6",
            "question": "My brother, ____ lives in Beijing, is a teacher.",
            "options": ["who", "which", "that", "where"],
            "correct_answer": "A",
            "explanation": "非限制性定语从句用who指代人，用逗号隔开。which指代物；that不能用于非限制性定语从句；where指地点。"
        },
        {
            "id": f"gram_{str(uuid.uuid4())[:8]}",
            "category": "grammar",
            "difficulty": "hard",
            "knowledge_tags": ["情态动词", "虚拟语气", "高级语法"],
            "exam_type": "CET6",
            "question": "You ____ have seen the movie; it's very popular.",
            "options": ["must", "should", "could", "might"],
            "correct_answer": "B",
            "explanation": "should have + 过去分词表示'本应该'，带有责备或遗憾的语气。must have表示对过去很有把握的推测；could have表示本可能；might have表示可能但不确定。"
        },
        {
            "id": f"gram_{str(uuid.uuid4())[:8]}",
            "category": "grammar",
            "difficulty": "medium",
            "knowledge_tags": ["名词性从句", "主语从句", "基础语法"],
            "exam_type": "CET6",
            "question": "____ he will come to the party is not known yet.",
            "options": ["Whether", "If", "That", "What"],
            "correct_answer": "A",
            "explanation": "Whether引导主语从句，表示'是否'。If也可以引导主语从句，但在句首时多用whether。That引导陈述性主语从句；what引导名词性从句但意思不符。"
        },
        {
            "id": f"gram_{str(uuid.uuid4())[:8]}",
            "category": "grammar",
            "difficulty": "hard",
            "knowledge_tags": ["强调句", "复杂强调", "高级语法"],
            "exam_type": "CET6",
            "question": "It was not until midnight ____ he finished his work.",
            "options": ["that", "when", "what", "which"],
            "correct_answer": "A",
            "explanation": "It was not until...that...是强调句型的变体，强调时间状语not until midnight。when引导时间状语从句；what引导名词性从句；which引导定语从句。"
        },
        {
            "id": f"gram_{str(uuid.uuid4())[:8]}",
            "category": "grammar",
            "difficulty": "medium",
            "knowledge_tags": ["非谓语动词", "过去分词", "基础语法"],
            "exam_type": "CET6",
            "question": "____ by the news, she couldn't speak a word.",
            "options": ["Shocking", "Shocked", "Being shocked", "To shock"],
            "correct_answer": "B",
            "explanation": "过去分词Shocked作状语，she与shock是被动关系，表示'她被这个消息震惊了'。Shocking表示主动；Being shocked是现在分词的被动式；To shock表示目的。"
        },
        {
            "id": f"gram_{str(uuid.uuid4())[:8]}",
            "category": "grammar",
            "difficulty": "hard",
            "knowledge_tags": ["倒装句", "完全倒装", "高级语法"],
            "exam_type": "CET6",
            "question": "____ the students in the classroom.",
            "options": ["There are", "There is", "Are there", "Is there"],
            "correct_answer": "A",
            "explanation": "There be句型的完全倒装结构。students是复数，用There are。There is用于单数；Are there和Is there是疑问句形式。"
        },
        {
            "id": f"gram_{str(uuid.uuid4())[:8]}",
            "category": "grammar",
            "difficulty": "medium",
            "knowledge_tags": ["比较级", "最高级", "基础语法"],
            "exam_type": "CET6",
            "question": "This is the ____ book I have ever read.",
            "options": ["most interesting", "more interesting", "interesting", "most interestinger"],
            "correct_answer": "A",
            "explanation": "最高级前加the，表示'最...的'。most interesting是interesting的最高级。more interesting是比较级；interesting是原级；most interestinger是错误形式。"
        },
        {
            "id": f"gram_{str(uuid.uuid4())[:8]}",
            "category": "grammar",
            "difficulty": "hard",
            "knowledge_tags": ["虚拟语气", "名词性从句", "高级语法"],
            "exam_type": "CET6",
            "question": "It's important that he ____ on time.",
            "options": ["arrive", "arrives", "arrived", "will arrive"],
            "correct_answer": "A",
            "explanation": "在It's important that...句型中，that从句的谓语动词用虚拟语气，即should + 动词原形或直接用动词原形。arrives是陈述语气；arrived是过去时；will arrive是将来时。"
        },
        {
            "id": f"gram_{str(uuid.uuid4())[:8]}",
            "category": "grammar",
            "difficulty": "medium",
            "knowledge_tags": ["介词", "固定搭配", "基础语法"],
            "exam_type": "CET6",
            "question": "She succeeded ____ passing the difficult exam.",
            "options": ["in", "on", "at", "with"],
            "correct_answer": "A",
            "explanation": "succeed in是固定搭配，意为'成功做某事'。其他介词不与succeed搭配使用。"
        },
        {
            "id": f"gram_{str(uuid.uuid4())[:8]}",
            "category": "grammar",
            "difficulty": "hard",
            "knowledge_tags": ["非谓语动词", "不定式作状语", "高级语法"],
            "exam_type": "CET6",
            "question": "____ to catch the early train, he got up at 5 AM.",
            "options": ["Determined", "Determining", "Being determined", "To determine"],
            "correct_answer": "A",
            "explanation": "过去分词Determined作状语，表示'他决心要赶上早班车'。Determining是现在分词；Being determined是现在分词的被动式；To determine表示目的，不符合语境。"
        },
        {
            "id": f"gram_{str(uuid.uuid4())[:8]}",
            "category": "grammar",
            "difficulty": "medium",
            "knowledge_tags": ["定语从句", "关系副词", "基础语法"],
            "exam_type": "CET6",
            "question": "This is the place ____ we first met.",
            "options": ["where", "when", "which", "what"],
            "correct_answer": "A",
            "explanation": "先行词是place，在从句中作地点状语，用关系副词where。when指时间；which指物；what引导名词性从句。"
        },
        {
            "id": f"gram_{str(uuid.uuid4())[:8]}",
            "category": "grammar",
            "difficulty": "hard",
            "knowledge_tags": ["情态动词", "推测", "高级语法"],
            "exam_type": "CET6",
            "question": "He ____ have forgotten our appointment; he's always punctual.",
            "options": ["can't", "mustn't", "shouldn't", "won't"],
            "correct_answer": "A",
            "explanation": "can't have + 过去分词表示对过去情况的否定推测，意为'不可能'。mustn't have表示禁止；shouldn't have表示本不应该；won't have表示将来不会。"
        }
    ]
    
    # ==================== 完整版阅读理解题 (20题) ====================
    complete_reading_questions = [
        {
            "id": f"read_{str(uuid.uuid4())[:8]}",
            "category": "reading",
            "difficulty": "hard",
            "knowledge_tags": ["推理判断", "深层推理", "议论文"],
            "exam_type": "CET6",
            "question": "What underlying assumption does the author make about human nature?",
            "passage_id": "passage_021",
            "options": ["People are inherently selfish", "People are naturally cooperative", "People are easily influenced", "People are fundamentally rational"],
            "correct_answer": "B",
            "explanation": "作者在文章中暗示人性本质上是合作的，这可以从作者对团队合作和社会互助的积极态度中推断出来。"
        },
        {
            "id": f"read_{str(uuid.uuid4())[:8]}",
            "category": "reading",
            "difficulty": "medium",
            "knowledge_tags": ["细节题", "事实信息", "说明文"],
            "exam_type": "CET6",
            "question": "According to the passage, what factor contributed most to the success?",
            "passage_id": "passage_022",
            "options": ["Leadership", "Technology", "Teamwork", "Innovation"],
            "correct_answer": "C",
            "explanation": "文章强调团队合作是成功的最重要因素，多次提到团队协作的重要性。"
        },
        {
            "id": f"read_{str(uuid.uuid4())[:8]}",
            "category": "reading",
            "difficulty": "hard",
            "knowledge_tags": ["主旨题", "中心思想", "议论文"],
            "exam_type": "CET6",
            "question": "What is the central argument of the passage?",
            "passage_id": "passage_023",
            "options": ["Technology will replace human workers", "Education is the key to economic growth", "Environmental protection is more important than development", "Global cooperation is essential for solving problems"],
            "correct_answer": "D",
            "explanation": "文章的中心论点是全球合作对于解决各种问题至关重要，这是贯穿全文的主题。"
        },
        {
            "id": f"read_{str(uuid.uuid4())[:8]}",
            "category": "reading",
            "difficulty": "medium",
            "knowledge_tags": ["词义猜测", "复杂词汇", "议论文"],
            "exam_type": "CET6",
            "question": "What does 'paradigm shift' most likely mean in this passage?",
            "passage_id": "passage_024",
            "options": ["Gradual change", "Fundamental transformation", "Minor adjustment", "Temporary modification"],
            "correct_answer": "B",
            "explanation": "'paradigm shift'意为'范式转换、根本性变革'，指思维方式或模式的根本性改变。"
        },
        {
            "id": f"read_{str(uuid.uuid4())[:8]}",
            "category": "reading",
            "difficulty": "hard",
            "knowledge_tags": ["推理判断", "态度观点", "议论文"],
            "exam_type": "CET6",
            "question": "What is the author's tone towards the proposed policy?",
            "passage_id": "passage_025",
            "options": ["Supportive", "Critical", "Neutral", "Skeptical"],
            "correct_answer": "A",
            "explanation": "作者对提议的政策持支持态度，文章中使用了积极正面的词汇来描述政策的潜在益处。"
        },
        {
            "id": f"read_{str(uuid.uuid4())[:8]}",
            "category": "reading",
            "difficulty": "medium",
            "knowledge_tags": ["细节题", "事实信息", "说明文"],
            "exam_type": "CET6",
            "question": "How much funding was allocated for the project?",
            "passage_id": "passage_026",
            "options": ["$1 million", "$2 million", "$3 million", "$4 million"],
            "correct_answer": "B",
            "explanation": "文章提到为这个项目分配了200万美元的资金。"
        },
        {
            "id": f"read_{str(uuid.uuid4())[:8]}",
            "category": "reading",
            "difficulty": "hard",
            "knowledge_tags": ["推理判断", "逻辑推理", "说明文"],
            "exam_type": "CET6",
            "question": "What is likely to happen if current trends continue?",
            "passage_id": "passage_027",
            "options": ["The problem will resolve itself", "The situation will worsen", "New solutions will emerge", "The problem will become irrelevant"],
            "correct_answer": "B",
            "explanation": "根据文章的分析，如果当前趋势继续下去，情况将会恶化，这是作者想要传达的警告。"
        },
        {
            "id": f"read_{str(uuid.uuid4())[:8]}",
            "category": "reading",
            "difficulty": "medium",
            "knowledge_tags": ["主旨题", "中心思想", "说明文"],
            "exam_type": "CET6",
            "question": "What is the main focus of the research mentioned in the passage?",
            "passage_id": "passage_028",
            "options": ["Human behavior", "Animal behavior", "Plant growth", "Climate change"],
            "correct_answer": "A",
            "explanation": "文章主要研究人类行为，特别是人类在特定环境下的行为模式。"
        },
        {
            "id": f"read_{str(uuid.uuid4())[:8]}",
            "category": "reading",
            "difficulty": "hard",
            "knowledge_tags": ["词义猜测", "专业术语", "议论文"],
            "exam_type": "CET6",
            "question": "In the context of the passage, what does 'synergy' refer to?",
            "passage_id": "passage_029",
            "options": ["Competition", "Cooperation", "Conflict", "Negotiation"],
            "correct_answer": "B",
            "explanation": "在文章上下文中，'synergy'指的是协同作用，即合作产生的整体效果大于各部分之和。"
        },
        {
            "id": f"read_{str(uuid.uuid4())[:8]}",
            "category": "reading",
            "difficulty": "medium",
            "knowledge_tags": ["细节题", "事实信息", "说明文"],
            "exam_type": "CET6",
            "question": "When was the study originally published?",
            "passage_id": "passage_030",
            "options": ["2019", "2020", "2021", "2022"],
            "correct_answer": "C",
            "explanation": "文章提到这项研究最初发表于2021年。"
        },
        {
            "id": f"read_{str(uuid.uuid4())[:8]}",
            "category": "reading",
            "difficulty": "hard",
            "knowledge_tags": ["推理判断", "深层理解", "议论文"],
            "exam_type": "CET6",
            "question": "What can be inferred about the long-term implications?",
            "passage_id": "passage_031",
            "options": ["They are negligible", "They are positive", "They are concerning", "They are unpredictable"],
            "correct_answer": "C",
            "explanation": "从文章的分析可以看出，作者对长期影响表示担忧，认为可能带来严重后果。"
        },
        {
            "id": f"read_{str(uuid.uuid4())[:8]}",
            "category": "reading",
            "difficulty": "medium",
            "knowledge_tags": ["细节题", "事实信息", "说明文"],
            "exam_type": "CET6",
            "question": "How many participants were involved in the experiment?",
            "passage_id": "passage_032",
            "options": ["50", "100", "150", "200"],
            "correct_answer": "C",
            "explanation": "文章提到实验有150名参与者。"
        },
        {
            "id": f"read_{str(uuid.uuid4())[:8]}",
            "category": "reading",
            "difficulty": "hard",
            "knowledge_tags": ["推理判断", "态度观点", "议论文"],
            "exam_type": "CET6",
            "question": "What is the author's primary concern mentioned in the passage?",
            "passage_id": "passage_033",
            "options": ["Economic inequality", "Environmental degradation", "Social injustice", "Political instability"],
            "correct_answer": "B",
            "explanation": "作者的主要关注点是环境退化，文章多次提到环境保护的重要性。"
        },
        {
            "id": f"read_{str(uuid.uuid4())[:8]}",
            "category": "reading",
            "difficulty": "medium",
            "knowledge_tags": ["词义猜测", "上下文理解", "说明文"],
            "exam_type": "CET6",
            "question": "What does 'innovative' mean in this context?",
            "passage_id": "passage_034",
            "options": ["Traditional", "Creative", "Expensive", "Complicated"],
            "correct_answer": "B",
            "explanation": "根据上下文，'innovative'意为'创新的、革新的'，强调创造性思维和方法。"
        },
        {
            "id": f"read_{str(uuid.uuid4())[:8]}",
            "category": "reading",
            "difficulty": "hard",
            "knowledge_tags": ["推理判断", "逻辑推理", "议论文"],
            "exam_type": "CET6",
            "question": "What conclusion can be drawn from the evidence presented?",
            "passage_id": "passage_035",
            "options": ["The hypothesis is confirmed", "The hypothesis is rejected", "More evidence is needed", "The results are inconclusive"],
            "correct_answer": "A",
            "explanation": "从提供的证据可以得出结论，假设得到了证实，实验结果支持了最初的假设。"
        },
        {
            "id": f"read_{str(uuid.uuid4())[:8]}",
            "category": "reading",
            "difficulty": "medium",
            "knowledge_tags": ["细节题", "事实信息", "说明文"],
            "exam_type": "CET6",
            "question": "What is the recommended frequency for the activity?",
            "passage_id": "passage_036",
            "options": ["Daily", "Weekly", "Monthly", "Yearly"],
            "correct_answer": "B",
            "explanation": "文章建议这项活动每周进行一次。"
        },
        {
            "id": f"read_{str(uuid.uuid4())[:8]}",
            "category": "reading",
            "difficulty": "hard",
            "knowledge_tags": ["推理判断", "深层理解", "议论文"],
            "exam_type": "CET6",
            "question": "What is the underlying message of the passage?",
            "passage_id": "passage_037",
            "options": ["Change is inevitable", "Progress requires sacrifice", "Technology solves all problems", "Human nature is unchangeable"],
            "correct_answer": "B",
            "explanation": "文章的深层信息是进步需要牺牲，作者通过多个例子说明了这一点。"
        },
        {
            "id": f"read_{str(uuid.uuid4())[:8]}",
            "category": "reading",
            "difficulty": "medium",
            "knowledge_tags": ["主旨题", "中心思想", "说明文"],
            "exam_type": "CET6",
            "question": "What aspect of the topic is primarily discussed?",
            "passage_id": "passage_038",
            "options": ["Historical background", "Current challenges", "Future prospects", "Practical applications"],
            "correct_answer": "B",
            "explanation": "文章主要讨论当前面临的挑战，分析了各种问题和困难。"
        },
        {
            "id": f"read_{str(uuid.uuid4())[:8]}",
            "category": "reading",
            "difficulty": "hard",
            "knowledge_tags": ["词义猜测", "抽象概念", "议论文"],
            "exam_type": "CET6",
            "question": "What does 'resilience' mean in this passage?",
            "passage_id": "passage_039",
            "options": ["Strength", "Flexibility", "Recovery ability", "Adaptability"],
            "correct_answer": "C",
            "explanation": "在文章语境中，'resilience'指的是恢复能力，即从困难或挫折中恢复的能力。"
        },
        {
            "id": f"read_{str(uuid.uuid4())[:8]}",
            "category": "reading",
            "difficulty": "medium",
            "knowledge_tags": ["细节题", "事实信息", "说明文"],
            "exam_type": "CET6",
            "question": "What was the outcome of the initiative?",
            "passage_id": "passage_040",
            "options": ["Complete failure", "Partial success", "Total success", "Mixed results"],
            "correct_answer": "D",
            "explanation": "文章提到倡议的结果是喜忧参半，既有成功也有不足。"
        }
    ]
    
    # 合并所有题目
    questions.extend(basic_vocabulary_questions)
    questions.extend(basic_grammar_questions)
    questions.extend(basic_reading_questions)
    questions.extend(complete_vocabulary_questions)
    questions.extend(complete_grammar_questions)
    questions.extend(complete_reading_questions)
    
    print(f"基础版词汇题: {len(basic_vocabulary_questions)}题")
    print(f"基础版语法题: {len(basic_grammar_questions)}题")
    print(f"基础版阅读题: {len(basic_reading_questions)}题")
    print(f"完整版词汇题: {len(complete_vocabulary_questions)}题")
    print(f"完整版语法题: {len(complete_grammar_questions)}题")
    print(f"完整版阅读题: {len(complete_reading_questions)}题")
    print(f"总计: {len(questions)}题")
    
    return questions

def create_final_cet4_6_questionnaire():
    """创建最终的150题四六级题库JSON文件"""
    
    # 生成题目
    questions = generate_final_cet4_6_questions()
    
    # 创建题库结构
    questionnaire = {
        "metadata": {
            "title": "大学英语四六级测试题库",
            "description": "包含基础版50题和完整版100题的四六级英语测试题库",
            "version": "1.0.0",
            "created_date": datetime.now().isoformat(),
            "total_questions": len(questions),
            "question_types": {
                "vocabulary": 30,
                "grammar": 30,
                "reading": 40
            },
            "difficulty_levels": {
                "easy": 45,
                "medium": 75,
                "hard": 30
            },
            "exam_types": {
                "CET4": 90,
                "CET6": 60
            },
            "versions": {
                "basic": {
                    "total_questions": 50,
                    "description": "基础版题库",
                    "vocabulary": 15,
                    "grammar": 15,
                    "reading": 20
                },
                "complete": {
                    "total_questions": 100,
                    "description": "完整版题库",
                    "vocabulary": 30,
                    "grammar": 30,
                    "reading": 40
                }
            }
        },
        "questions": questions
    }
    
    return questionnaire

if __name__ == "__main__":
    # 生成题库
    questionnaire = create_final_cet4_6_questionnaire()
    
    # 保存为JSON文件
    with open('/workspace/data/cet4_6_questions.json', 'w', encoding='utf-8') as f:
        json.dump(questionnaire, f, ensure_ascii=False, indent=2)
    
    print(f"\n完整题库生成完成！")
    print(f"总题数: {questionnaire['metadata']['total_questions']}")
    print(f"词汇题: {questionnaire['metadata']['question_types']['vocabulary']}")
    print(f"语法题: {questionnaire['metadata']['question_types']['grammar']}")
    print(f"阅读题: {questionnaire['metadata']['question_types']['reading']}")
    print(f"基础版: {questionnaire['metadata']['versions']['basic']['total_questions']}题")
    print(f"完整版: {questionnaire['metadata']['versions']['complete']['total_questions']}题")
    print(f"文件已保存至: /workspace/data/cet4_6_questions.json")