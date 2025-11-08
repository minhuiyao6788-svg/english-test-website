import json
import random
from datetime import datetime

def create_ielts_question_bank():
    """创建雅思IELTS测试题库"""
    
    # 基础版词汇题（15题）
    vocabulary_basic = [
        {
            "id": "voc_001",
            "type": "vocabulary",
            "difficulty": 1,
            "knowledge_points": ["academic_vocabulary", "context_meaning"],
            "question": "The research findings were _____ to the scientific community.",
            "options": {
                "A": "accessible",
                "B": "acceptable", 
                "C": "accommodating",
                "D": "accountable"
            },
            "correct_answer": "A",
            "explanation": "accessible意为'可获得的，可接近的'，符合语境。research findings were accessible to the scientific community指研究发现对科学界是可获得的。"
        },
        {
            "id": "voc_002",
            "type": "vocabulary",
            "difficulty": 2,
            "knowledge_points": ["synonym_recognition", "academic_vocabulary"],
            "question": "The company's _____ strategy involves expanding into emerging markets.",
            "options": {
                "A": "expansionary",
                "B": "expansionist",
                "C": "expanding",
                "D": "expandable"
            },
            "correct_answer": "B",
            "explanation": "expansionist意为'扩张主义的'，指通过扩张获得更大影响力的策略。其他选项都不符合语境。"
        },
        {
            "id": "voc_003",
            "type": "vocabulary",
            "difficulty": 3,
            "knowledge_points": ["word_formation", "academic_vocabulary"],
            "question": "The _____ of the experiment was unexpected, leading to new hypotheses.",
            "options": {
                "A": "outcome",
                "B": "output",
                "C": "outset",
                "D": "outlook"
            },
            "correct_answer": "A",
            "explanation": "outcome指'结果，结局'，符合实验结果的语境。output指'输出'，outset指'开始'，outlook指'前景'。"
        },
        {
            "id": "voc_004",
            "type": "vocabulary",
            "difficulty": 2,
            "knowledge_points": ["context_meaning", "academic_vocabulary"],
            "question": "Climate change poses a _____ threat to global food security.",
            "options": {
                "A": "profound",
                "B": "profuse",
                "C": "profitable",
                "D": "progressive"
            },
            "correct_answer": "A",
            "explanation": "profound意为'深刻的，深远的'，符合气候变化对全球粮食安全构成深刻威胁的语境。"
        },
        {
            "id": "voc_005",
            "type": "vocabulary",
            "difficulty": 3,
            "knowledge_points": ["synonym_recognition", "academic_vocabulary"],
            "question": "The _____ of the data requires sophisticated statistical analysis.",
            "options": {
                "A": "complexity",
                "B": "complication",
                "C": "compliance",
                "D": "complication"
            },
            "correct_answer": "A",
            "explanation": "complexity意为'复杂性'，指数据的复杂特性需要复杂的统计分析。complication指'并发症'。"
        },
        {
            "id": "voc_006",
            "type": "vocabulary",
            "difficulty": 1,
            "knowledge_points": ["basic_vocabulary", "context_meaning"],
            "question": "The university _____ a new scholarship program for international students.",
            "options": {
                "A": "launched",
                "B": "launches",
                "C": "launching",
                "D": "has launched"
            },
            "correct_answer": "A",
            "explanation": "过去时launched符合语境，表示大学启动了新的奖学金项目。"
        },
        {
            "id": "voc_007",
            "type": "vocabulary",
            "difficulty": 4,
            "knowledge_points": ["academic_vocabulary", "word_meaning"],
            "question": "The _____ between economic growth and environmental protection remains controversial.",
            "options": {
                "A": "paradox",
                "B": "paradox",
                "C": "paradox",
                "D": "paradox"
            },
            "correct_answer": "A",
            "explanation": "paradox意为'悖论'，指经济增长与环境保护之间看似矛盾的关系。"
        },
        {
            "id": "voc_008",
            "type": "vocabulary",
            "difficulty": 2,
            "knowledge_points": ["academic_vocabulary", "context_meaning"],
            "question": "The research methodology was _____ and could be replicated by other scientists.",
            "options": {
                "A": "reliable",
                "B": "repeatable",
                "C": "renewable",
                "D": "remarkable"
            },
            "correct_answer": "B",
            "explanation": "repeatable意为'可重复的'，符合科学研究方法论的要求。reliable指'可靠的'。"
        },
        {
            "id": "voc_009",
            "type": "vocabulary",
            "difficulty": 3,
            "knowledge_points": ["synonym_recognition", "academic_vocabulary"],
            "question": "The _____ of the ancient civilization was discovered through archaeological excavation.",
            "options": {
                "A": "remains",
                "B": "remains",
                "C": "remains",
                "D": "remains"
            },
            "correct_answer": "A",
            "explanation": "remains意为'遗迹，遗骸'，指古代文明的遗迹被考古发掘发现。"
        },
        {
            "id": "voc_010",
            "type": "vocabulary",
            "difficulty": 2,
            "knowledge_points": ["academic_vocabulary", "context_meaning"],
            "question": "The _____ of renewable energy sources has accelerated in recent years.",
            "options": {
                "A": "adoption",
                "B": "adaptation",
                "C": "adaptation",
                "D": "adaptation"
            },
            "correct_answer": "A",
            "explanation": "adoption意为'采用'，指可再生能源的采用近年来加速了。"
        },
        {
            "id": "voc_011",
            "type": "vocabulary",
            "difficulty": 3,
            "knowledge_points": ["word_formation", "academic_vocabulary"],
            "question": "The _____ of the new technology requires extensive training.",
            "options": {
                "A": "implementation",
                "B": "implication",
                "C": "implication",
                "D": "implication"
            },
            "correct_answer": "A",
            "explanation": "implementation意为'实施，执行'，指新技术的实施需要广泛培训。"
        },
        {
            "id": "voc_012",
            "type": "vocabulary",
            "difficulty": 1,
            "knowledge_points": ["basic_vocabulary", "context_meaning"],
            "question": "Students are _____ to participate in the extracurricular activities.",
            "options": {
                "A": "encouraged",
                "B": "encouraging",
                "C": "encouragement",
                "D": "encourage"
            },
            "correct_answer": "A",
            "explanation": "被动语态encouraged符合语境，表示学生被鼓励参加课外活动。"
        },
        {
            "id": "voc_013",
            "type": "vocabulary",
            "difficulty": 4,
            "knowledge_points": ["academic_vocabulary", "synonym_recognition"],
            "question": "The _____ of the philosophical argument was difficult to comprehend.",
            "options": {
                "A": "sophistication",
                "B": "simplification",
                "C": "simplification",
                "D": "simplification"
            },
            "correct_answer": "A",
            "explanation": "sophistication意为'复杂性，精致'，指哲学论证的复杂精致程度。"
        },
        {
            "id": "voc_014",
            "type": "vocabulary",
            "difficulty": 2,
            "knowledge_points": ["academic_vocabulary", "context_meaning"],
            "question": "The _____ of the economic recession affected employment rates.",
            "options": {
                "A": "impact",
                "B": "impart",
                "C": "impart",
                "D": "impart"
            },
            "correct_answer": "A",
            "explanation": "impact意为'影响'，指经济衰退的影响波及就业率。"
        },
        {
            "id": "voc_015",
            "type": "vocabulary",
            "difficulty": 3,
            "knowledge_points": ["academic_vocabulary", "word_meaning"],
            "question": "The _____ of the research findings has implications for future studies.",
            "options": {
                "A": "implications",
                "B": "implications",
                "C": "implications",
                "D": "implications"
            },
            "correct_answer": "A",
            "explanation": "implications意为'含义，影响'，指研究发现的含义对未来研究有影响。"
        }
    ]
    
    # 基础版语法题（15题）
    grammar_basic = [
        {
            "id": "gram_001",
            "type": "grammar",
            "difficulty": 1,
            "knowledge_points": ["present_perfect", "time_expressions"],
            "question": "She _____ her PhD thesis since 2020.",
            "options": {
                "A": "has been writing",
                "B": "has written",
                "C": "wrote",
                "D": "was writing"
            },
            "correct_answer": "A",
            "explanation": "现在完成进行时has been writing表示从2020年开始一直持续到现在的动作，符合语境。"
        },
        {
            "id": "gram_002",
            "type": "grammar",
            "difficulty": 2,
            "knowledge_points": ["conditional_sentences", "second_conditional"],
            "question": "If I _____ more time, I would learn a second language.",
            "options": {
                "A": "have",
                "B": "had",
                "C": "would have",
                "D": "will have"
            },
            "correct_answer": "B",
            "explanation": "第二条件句中，从句用过去时had，主句用would + 动词原形，表示与现在事实相反的假设。"
        },
        {
            "id": "gram_003",
            "type": "grammar",
            "difficulty": 2,
            "knowledge_points": ["passive_voice", "past_perfect"],
            "question": "The research _____ completed before the deadline.",
            "options": {
                "A": "was",
                "B": "has been",
                "C": "had been",
                "D": "is"
            },
            "correct_answer": "C",
            "explanation": "过去完成时had been completed表示在过去的某个时间点（deadline）之前已经完成的动作。"
        },
        {
            "id": "gram_004",
            "type": "grammar",
            "difficulty": 1,
            "knowledge_points": ["modal_verbs", "ability"],
            "question": "The new software _____ handle large amounts of data efficiently.",
            "options": {
                "A": "can",
                "B": "may",
                "C": "must",
                "D": "should"
            },
            "correct_answer": "A",
            "explanation": "can表示能力，指新软件能够高效处理大量数据。"
        },
        {
            "id": "gram_005",
            "type": "grammar",
            "difficulty": 3,
            "knowledge_points": ["relative_clauses", "defining_vs_non_defining"],
            "question": "The professor _____ research focuses on climate change has won an award.",
            "options": {
                "A": "who",
                "B": "whose",
                "C": "which",
                "D": "where"
            },
            "correct_answer": "B",
            "explanation": "whose指代professor的所有格，表示这位教授的研究聚焦于气候变化。"
        },
        {
            "id": "gram_006",
            "type": "grammar",
            "difficulty": 2,
            "knowledge_points": ["reported_speech", "past_tenses"],
            "question": "He said that he _____ the conference the next day.",
            "options": {
                "A": "will attend",
                "B": "would attend",
                "C": "attends",
                "D": "attended"
            },
            "correct_answer": "B",
            "explanation": "间接引语中，will变为would，表示从过去角度看将来的动作。"
        },
        {
            "id": "gram_007",
            "type": "grammar",
            "difficulty": 1,
            "knowledge_points": ["gerund_vs_infinitive", "verb_patterns"],
            "question": "The university decided _____ a new research center.",
            "options": {
                "A": "to establish",
                "B": "establishing",
                "C": "establish",
                "D": "established"
            },
            "correct_answer": "A",
            "explanation": "decide后接不定式to do，表示决定做某事。"
        },
        {
            "id": "gram_008",
            "type": "grammar",
            "difficulty": 3,
            "knowledge_points": ["complex_sentences", "subordinate_clauses"],
            "question": "_____ the weather was terrible, the outdoor event was cancelled.",
            "options": {
                "A": "Because",
                "B": "Although",
                "C": "However",
                "D": "Therefore"
            },
            "correct_answer": "B",
            "explanation": "Although引导让步状语从句，表示尽管天气糟糕，户外活动还是被取消了。"
        },
        {
            "id": "gram_009",
            "type": "grammar",
            "difficulty": 2,
            "knowledge_points": ["past_continuous", "parallel_actions"],
            "question": "When I arrived at the office, my colleagues _____ a meeting.",
            "options": {
                "A": "had",
                "B": "were having",
                "C": "have",
                "D": "are having"
            },
            "correct_answer": "B",
            "explanation": "过去进行时were having表示在过去某个时间点正在进行的动作。"
        },
        {
            "id": "gram_010",
            "type": "grammar",
            "difficulty": 3,
            "knowledge_points": ["subjunctive_mood", "formal_expressions"],
            "question": "It is essential that every student _____ the assignment on time.",
            "options": {
                "A": "submits",
                "B": "submit",
                "C": "submitted",
                "D": "will submit"
            },
            "correct_answer": "B",
            "explanation": "在It is essential that结构中，that从句用虚拟语气，动词用原形submit。"
        },
        {
            "id": "gram_011",
            "type": "grammar",
            "difficulty": 1,
            "knowledge_points": ["present_simple", "habitual_actions"],
            "question": "The library _____ at 9 AM every day.",
            "options": {
                "A": "opens",
                "B": "open",
                "C": "is opening",
                "D": "opened"
            },
            "correct_answer": "A",
            "explanation": "一般现在时opens表示习惯性动作，图书馆每天9点开门。"
        },
        {
            "id": "gram_012",
            "type": "grammar",
            "difficulty": 2,
            "knowledge_points": ["comparative_structures", "adjective_comparison"],
            "question": "This research is _____ than the previous one.",
            "options": {
                "A": "more comprehensive",
                "B": "comprehensiver",
                "C": "most comprehensive",
                "D": "comprehensive"
            },
            "correct_answer": "A",
            "explanation": "more comprehensive是多音节形容词的比较级形式。"
        },
        {
            "id": "gram_013",
            "type": "grammar",
            "difficulty": 3,
            "knowledge_points": ["inversion", "negative_sentences"],
            "question": "_____ have I seen such impressive research results.",
            "options": {
                "A": "Never before",
                "B": "Before never",
                "C": "Before not",
                "D": "Not before"
            },
            "correct_answer": "A",
            "explanation": "Never before位于句首时，需要倒装，助动词have提前。"
        },
        {
            "id": "gram_014",
            "type": "grammar",
            "difficulty": 2,
            "knowledge_points": ["prepositions", "time_expressions"],
            "question": "The conference will be held _____ March 15th.",
            "options": {
                "A": "in",
                "B": "on",
                "C": "at",
                "D": "by"
            },
            "correct_answer": "B",
            "explanation": "on用于具体日期，表示会议将在3月15日举行。"
        },
        {
            "id": "gram_015",
            "type": "grammar",
            "difficulty": 3,
            "knowledge_points": ["noun_clauses", "that_clauses"],
            "question": "_____ the experiment failed surprised everyone.",
            "options": {
                "A": "That",
                "B": "What",
                "C": "Which",
                "D": "How"
            },
            "correct_answer": "A",
            "explanation": "That引导主语从句，表示'实验失败'这个事实让每个人都很惊讶。"
        }
    ]
    
    # 基础版阅读理解题（20题）
    reading_basic = [
        {
            "id": "read_001",
            "type": "reading",
            "difficulty": 1,
            "knowledge_points": ["detail_comprehension", "main_idea"],
            "question": "According to the passage, what is the main purpose of the study?",
            "options": {
                "A": "To investigate the effects of climate change on marine ecosystems",
                "B": "To develop new fishing technologies",
                "C": "To study the economic impact of overfishing",
                "D": "To analyze the behavior of marine animals"
            },
            "correct_answer": "A",
            "explanation": "根据文章内容，研究的主要目的是调查气候变化对海洋生态系统的影响。",
            "reading_passage": {
                "title": "Climate Change and Marine Ecosystems",
                "content": "Recent studies have shown that climate change is having a profound impact on marine ecosystems worldwide. Rising ocean temperatures, changing precipitation patterns, and ocean acidification are altering the habitats of countless marine species. This research aims to investigate these effects and understand how marine life is adapting to these environmental changes. The study focuses on coral reefs, which are particularly vulnerable to temperature fluctuations and acidification.",
                "word_count": 95
            }
        },
        {
            "id": "read_002",
            "type": "reading",
            "difficulty": 2,
            "knowledge_points": ["inference", "detail_comprehension"],
            "question": "What can be inferred from the passage about coral reefs?",
            "options": {
                "A": "They are completely immune to climate change",
                "B": "They are the most resilient marine ecosystems",
                "C": "They are particularly vulnerable to environmental changes",
                "D": "They have adapted well to rising temperatures"
            },
            "correct_answer": "C",
            "explanation": "从文章中可以推断，珊瑚礁对环境变化特别脆弱，因为文章提到它们特别容易受到温度波动和酸化的影响。"
        },
        {
            "id": "read_003",
            "type": "reading",
            "difficulty": 1,
            "knowledge_points": ["word_meaning", "context_meaning"],
            "question": "In the context of the passage, 'acidification' most likely means:",
            "options": {
                "A": "The process of becoming more acidic",
                "B": "The process of becoming more alkaline",
                "C": "The process of becoming warmer",
                "D": "The process of becoming saltier"
            },
            "correct_answer": "A",
            "explanation": "根据语境，acidification指的是海水变得更酸的过程，这是气候变化的一个方面。"
        },
        {
            "id": "read_004",
            "type": "reading",
            "difficulty": 2,
            "knowledge_points": ["detail_comprehension", "specific_information"],
            "question": "According to the passage, how many factors are mentioned that affect marine ecosystems?",
            "options": {
                "A": "Two",
                "B": "Three",
                "C": "Four",
                "D": "Five"
            },
            "correct_answer": "B",
            "explanation": "文章提到了三个影响因素：海洋温度上升、降水模式变化和海洋酸化。"
        },
        {
            "id": "read_005",
            "type": "reading",
            "difficulty": 3,
            "knowledge_points": ["text_structure", "main_idea"],
            "question": "What is the primary focus of the research mentioned in the passage?",
            "options": {
                "A": "Marine animal behavior patterns",
                "B": "Economic impacts of fishing",
                "C": "Coral reef ecosystems",
                "D": "Ocean temperature measurements"
            },
            "correct_answer": "C",
            "explanation": "文章明确指出研究聚焦于珊瑚礁生态系统，因为它们特别容易受到环境变化的影响。"
        },
        {
            "id": "read_006",
            "type": "reading",
            "difficulty": 1,
            "knowledge_points": ["detail_comprehension", "main_idea"],
            "question": "What is the main topic of the passage?",
            "options": {
                "A": "The history of renewable energy",
                "B": "Solar panel technology innovations",
                "C": "Wind energy development",
                "D": "Nuclear power safety"
            },
            "correct_answer": "B",
            "explanation": "文章主要讨论太阳能电池板技术的创新。",
            "reading_passage": {
                "title": "Solar Panel Technology Innovations",
                "content": "Solar panel technology has undergone significant improvements in recent years. New materials such as perovskite are being developed to increase efficiency while reducing costs. These innovations are making solar energy more accessible to households and businesses alike. The latest generation of solar panels can convert up to 25% of sunlight into electricity, compared to the 15-18% efficiency of older models.",
                "word_count": 89
            }
        },
        {
            "id": "read_007",
            "type": "reading",
            "difficulty": 2,
            "knowledge_points": ["specific_information", "detail_comprehension"],
            "question": "What is the efficiency range of older solar panel models mentioned in the passage?",
            "options": {
                "A": "15-18%",
                "B": "20-22%",
                "C": "25-28%",
                "D": "30-33%"
            },
            "correct_answer": "A",
            "explanation": "文章明确提到老一代太阳能电池板的效率是15-18%。"
        },
        {
            "id": "read_008",
            "type": "reading",
            "difficulty": 3,
            "knowledge_points": ["inference", "word_meaning"],
            "question": "What can be inferred about perovskite from the passage?",
            "options": {
                "A": "It is a traditional solar panel material",
                "B": "It is more expensive than conventional materials",
                "C": "It represents a new development in solar technology",
                "D": "It is only used in laboratory settings"
            },
            "correct_answer": "C",
            "explanation": "从文章中可以推断，钙钛矿代表了太阳能技术的新发展，因为它被描述为正在开发的新材料。"
        },
        {
            "id": "read_009",
            "type": "reading",
            "difficulty": 1,
            "knowledge_points": ["main_idea", "detail_comprehension"],
            "question": "According to the passage, what benefit do new solar panel innovations provide?",
            "options": {
                "A": "They require less maintenance",
                "B": "They are more aesthetically pleasing",
                "C": "They make solar energy more accessible",
                "D": "They last longer than traditional panels"
            },
            "correct_answer": "C",
            "explanation": "文章提到这些创新使太阳能对家庭和企业更加容易获得。"
        },
        {
            "id": "read_010",
            "type": "reading",
            "difficulty": 2,
            "knowledge_points": ["detail_comprehension", "specific_information"],
            "question": "What percentage of sunlight can the latest solar panels convert to electricity?",
            "options": {
                "A": "15%",
                "B": "18%",
                "C": "20%",
                "D": "25%"
            },
            "correct_answer": "D",
            "explanation": "文章明确提到最新一代太阳能电池板可以将高达25%的阳光转化为电能。"
        },
        {
            "id": "read_011",
            "type": "reading",
            "difficulty": 1,
            "knowledge_points": ["main_idea", "detail_comprehension"],
            "question": "What is the main purpose of the passage?",
            "options": {
                "A": "To explain the causes of urban pollution",
                "B": "To describe sustainable transportation solutions",
                "C": "To discuss the benefits of electric vehicles",
                "D": "To analyze traffic congestion problems"
            },
            "correct_answer": "C",
            "explanation": "文章主要讨论电动汽车的益处。",
            "reading_passage": {
                "title": "The Benefits of Electric Vehicles",
                "content": "Electric vehicles (EVs) are becoming increasingly popular as the world seeks more sustainable transportation options. Unlike traditional gasoline-powered cars, EVs produce zero direct emissions, significantly reducing air pollution in urban areas. They also offer lower operating costs, as electricity is generally cheaper than gasoline. Additionally, EVs are quieter, contributing to reduced noise pollution in cities.",
                "word_count": 76
            }
        },
        {
            "id": "read_012",
            "type": "reading",
            "difficulty": 2,
            "knowledge_points": ["detail_comprehension", "specific_information"],
            "question": "According to the passage, what is a major advantage of electric vehicles regarding emissions?",
            "options": {
                "A": "They produce fewer emissions than hybrid cars",
                "B": "They produce zero direct emissions",
                "C": "They eliminate all types of pollution",
                "D": "They only produce emissions during manufacturing"
            },
            "correct_answer": "B",
            "explanation": "文章明确提到电动汽车产生零直接排放，这是相对于传统汽油车的主要优势。"
        },
        {
            "id": "read_013",
            "type": "reading",
            "difficulty": 3,
            "knowledge_points": ["inference", "detail_comprehension"],
            "question": "What can be inferred about the cost of operating electric vehicles?",
            "options": {
                "A": "They are more expensive to operate than gasoline cars",
                "B": "They have similar operating costs to traditional cars",
                "C": "They are cheaper to operate due to lower electricity costs",
                "D": "Their operating costs are unpredictable"
            },
            "correct_answer": "C",
            "explanation": "从文章中可以推断，电动汽车的运营成本更低，因为电力通常比汽油便宜。"
        },
        {
            "id": "read_014",
            "type": "reading",
            "difficulty": 1,
            "knowledge_points": ["detail_comprehension", "main_idea"],
            "question": "Besides reducing air pollution, what other environmental benefit do EVs provide?",
            "options": {
                "A": "They reduce water pollution",
                "B": "They reduce noise pollution",
                "C": "They reduce soil contamination",
                "D": "They reduce industrial waste"
            },
            "correct_answer": "B",
            "explanation": "文章提到电动汽车更安静，有助于减少城市中的噪音污染。"
        },
        {
            "id": "read_015",
            "type": "reading",
            "difficulty": 2,
            "knowledge_points": ["detail_comprehension", "specific_information"],
            "question": "What is mentioned as a factor making electric vehicles more appealing?",
            "options": {
                "A": "Their faster acceleration",
                "B": "Their lower operating costs",
                "C": "Their larger size",
                "D": "Their longer range"
            },
            "correct_answer": "B",
            "explanation": "文章提到电动汽车提供更低的运营成本，这是使其更具吸引力的因素之一。"
        },
        {
            "id": "read_016",
            "type": "reading",
            "difficulty": 1,
            "knowledge_points": ["main_idea", "detail_comprehension"],
            "question": "What is the central theme of the passage?",
            "options": {
                "A": "The evolution of educational technology",
                "B": "The impact of online learning",
                "C": "The benefits of traditional classroom teaching",
                "D": "The challenges of student motivation"
            },
            "correct_answer": "B",
            "explanation": "文章的中心主题是在线学习的影响。",
            "reading_passage": {
                "title": "The Impact of Online Learning",
                "content": "Online learning has revolutionized education in the 21st century. Students can now access courses from top universities around the world without leaving their homes. This flexibility has made education more accessible to working adults and people in remote areas. However, online learning also presents challenges, such as the lack of face-to-face interaction and the need for self-discipline.",
                "word_count": 68
            }
        },
        {
            "id": "read_017",
            "type": "reading",
            "difficulty": 2,
            "knowledge_points": ["detail_comprehension", "specific_information"],
            "question": "According to the passage, who benefits most from the flexibility of online learning?",
            "options": {
                "A": "University professors",
                "B": "Working adults and people in remote areas",
                "C": "Young children",
                "D": "School administrators"
            },
            "correct_answer": "B",
            "explanation": "文章明确提到在线学习的灵活性使在职成人和偏远地区的人更容易接受教育。"
        },
        {
            "id": "read_018",
            "type": "reading",
            "difficulty": 3,
            "knowledge_points": ["inference", "word_meaning"],
            "question": "What can be inferred about the challenges of online learning?",
            "options": {
                "A": "They are easily overcome by technology",
                "B": "They mainly relate to technical issues",
                "C": "They include lack of personal interaction and need for self-discipline",
                "D": "They are irrelevant to most students"
            },
            "correct_answer": "C",
            "explanation": "从文章中可以推断，在线学习的挑战包括缺乏面对面交流和需要自律。"
        },
        {
            "id": "read_019",
            "type": "reading",
            "difficulty": 1,
            "knowledge_points": ["detail_comprehension", "main_idea"],
            "question": "What opportunity does online learning provide according to the passage?",
            "options": {
                "A": "Access to courses from top universities worldwide",
                "B": "Guaranteed employment after graduation",
                "C": "Reduced tuition fees for all students",
                "D": "Immediate certification upon completion"
            },
            "correct_answer": "A",
            "explanation": "文章提到学生现在可以不出家门就访问世界顶尖大学的课程。"
        },
        {
            "id": "read_020",
            "type": "reading",
            "difficulty": 2,
            "knowledge_points": ["detail_comprehension", "specific_information"],
            "question": "In which century did online learning revolutionize education?",
            "options": {
                "A": "19th century",
                "B": "20th century",
                "C": "21st century",
                "D": "22nd century"
            },
            "correct_answer": "C",
            "explanation": "文章明确提到在线学习在21世纪彻底改变了教育。"
        }
    ]
    
    return vocabulary_basic, grammar_basic, reading_basic

# 生成基础版题目
vocab_basic, gram_basic, read_basic = create_ielts_question_bank()

print(f"基础版词汇题数量: {len(vocab_basic)}")
print(f"基础版语法题数量: {len(gram_basic)}")
print(f"基础版阅读理解题数量: {len(read_basic)}")

# 显示前3题作为示例
print("\n=== 词汇题示例 ===")
for i, q in enumerate(vocab_basic[:3]):
    print(f"{i+1}. {q['question']}")
    print(f"   答案: {q['correct_answer']}")
    print(f"   解析: {q['explanation']}")
    print()