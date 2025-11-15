import React, { useState, useEffect } from 'react';
import { useNavigate, useLocation } from 'react-router-dom';
import { ChevronLeft, ChevronRight, Clock, CheckCircle } from 'lucide-react';

interface Question {
  id: string;
  question: string;
  options: {
    A: string;
    B: string;
    C: string;
    D: string;
  };
  correct_answer: string;
  explanation?: string;
  category?: string;
  difficulty?: string;
  // 词汇测试特有字段
  word?: string;
  example_sentence?: string;
}

interface TestData {
  metadata: any;
  questions: Question[];
  basic_version?: {
    total_questions: number;
    questions: Question[];
  };
  complete_version?: {
    total_questions: number;
    questions: Question[];
  };
}

const TestPage: React.FC = () => {
  const navigate = useNavigate();
  const location = useLocation();
  const { testType, mode } = location.state || {};

  const [questions, setQuestions] = useState<Question[]>([]);
  const [currentQuestionIndex, setCurrentQuestionIndex] = useState(0);
  const [answers, setAnswers] = useState<{ [key: string]: string }>({});
  const [timeLeft, setTimeLeft] = useState(0);
  const [isLoading, setIsLoading] = useState(true);
  const [testData, setTestData] = useState<TestData | null>(null);

  // 加载题库数据
  useEffect(() => {
    const loadQuestions = async () => {
      try {
        let fileName = '';
        if (testType === 'cet4') {
          fileName = 'cet4_questions.json';
        } else if (testType === 'cet6') {
          fileName = 'cet6_questions.json';
        } else if (testType === 'cet4_6') {
          fileName = 'cet4_6_questions.json';
        } else if (testType === 'ielts') {
          fileName = 'ielts_questions.json';
        } else if (testType === 'vocabulary') {
          fileName = 'vocabulary_test_questions.json';
        }
        
        const response = await fetch(`/${fileName}`);
        const data: TestData = await response.json();
        setTestData(data);
        
        let selectedQuestions: Question[] = [];
        
        // 雅思题库特殊处理
        if (testType === 'ielts') {
          const dataAny = data as any; // 雅思题库结构复杂，使用any类型
          if (mode === 'basic' && dataAny.basic_version) {
            // 合并雅思 basic_version 中的所有题目
            const vocabQuestions = dataAny.basic_version.vocabulary?.questions || [];
            const grammarQuestions = dataAny.basic_version.grammar?.questions || [];
            const readingQuestions = dataAny.basic_version.reading?.questions || [];
            selectedQuestions = [...vocabQuestions, ...grammarQuestions, ...readingQuestions];
          } else if (mode === 'complete' && dataAny.complete_version) {
            // 合并雅思 complete_version 中的所有题目
            const vocabQuestions = dataAny.complete_version.vocabulary?.questions || [];
            const grammarQuestions = dataAny.complete_version.grammar?.questions || [];
            const readingQuestions = dataAny.complete_version.reading?.questions || [];
            selectedQuestions = [...vocabQuestions, ...grammarQuestions, ...readingQuestions];
          }
        } else {
          // 其他题库的处理
          if (mode === 'basic') {
            selectedQuestions = data.basic_version?.questions || data.questions.slice(0, 50);
          } else {
            selectedQuestions = data.complete_version?.questions || data.questions.slice(0, 100);
          }
        }
        
        // 打乱题目顺序（Fisher-Yates洗牌算法）
        const shuffledQuestions = [...selectedQuestions];
        for (let i = shuffledQuestions.length - 1; i > 0; i--) {
          const j = Math.floor(Math.random() * (i + 1));
          [shuffledQuestions[i], shuffledQuestions[j]] = [shuffledQuestions[j], shuffledQuestions[i]];
        }
        
        setQuestions(shuffledQuestions);
        setTimeLeft(shuffledQuestions.length * 45); // 每题45秒
        setIsLoading(false);
      } catch (error) {
        console.error('加载题库失败:', error);
        setIsLoading(false);
      }
    };

    if (testType && mode) {
      loadQuestions();
    }
  }, [testType, mode]);

  // 计时器
  useEffect(() => {
    if (timeLeft > 0 && !isLoading) {
      const timer = setTimeout(() => {
        setTimeLeft(timeLeft - 1);
      }, 1000);
      return () => clearTimeout(timer);
    } else if (timeLeft === 0 && questions.length > 0) {
      // 时间到，自动提交
      handleSubmitTest();
    }
  }, [timeLeft, isLoading, questions.length]);

  const formatTime = (seconds: number) => {
    const mins = Math.floor(seconds / 60);
    const secs = seconds % 60;
    return `${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;
  };

  const handleAnswerSelect = (questionId: string, answer: string) => {
    setAnswers(prev => ({
      ...prev,
      [questionId]: answer
    }));
    
    // 自动跳转到下一题，使用函数式更新确保状态正确
    setTimeout(() => {
      setCurrentQuestionIndex(prevIndex => {
        if (prevIndex < questions.length - 1) {
          return prevIndex + 1;
        } else {
          // 最后一题，自动提交测试
          handleSubmitTest();
          return prevIndex;
        }
      });
    }, 300); // 300ms延迟，让用户看到选择效果
  };

  const handleNext = () => {
    if (currentQuestionIndex < questions.length - 1) {
      setCurrentQuestionIndex(prevIndex => prevIndex + 1);
    }
  };

  const handlePrevious = () => {
    if (currentQuestionIndex > 0) {
      setCurrentQuestionIndex(prevIndex => prevIndex - 1);
    }
  };

  const handleQuestionJump = (index: number) => {
    setCurrentQuestionIndex(index);
  };

  const handleSubmitTest = () => {
    navigate('/result', {
      state: {
        testType,
        mode,
        answers,
        questions,
        timeUsed: questions.length * 45 - timeLeft
      }
    });
  };

  const currentQuestion = questions[currentQuestionIndex];
  const progress = ((currentQuestionIndex + 1) / questions.length) * 100;
  const answeredCount = Object.keys(answers).length;
  const isLastQuestion = currentQuestionIndex === questions.length - 1;

  if (isLoading) {
    return (
      <div className="min-h-screen bg-gradient-to-br from-teal-50 to-cyan-100 flex items-center justify-center">
        <div className="text-center">
          <div className="w-16 h-16 border-4 border-teal-200 border-t-teal-500 rounded-full animate-spin mx-auto mb-4"></div>
          <p className="text-lg text-gray-600">正在加载题库...</p>
        </div>
      </div>
    );
  }

  if (!currentQuestion) {
    return (
      <div className="min-h-screen bg-gradient-to-br from-teal-50 to-cyan-100 flex items-center justify-center">
        <div className="text-center">
          <p className="text-lg text-gray-600">加载题目失败</p>
          <button 
            onClick={() => navigate('/')}
            className="mt-4 px-6 py-2 bg-teal-500 text-white rounded-lg hover:bg-teal-600"
          >
            返回首页
          </button>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-teal-50 to-cyan-100">
      {/* Header */}
      <header className="bg-white/80 backdrop-blur-sm border-b border-teal-100 sticky top-0 z-10">
        <div className="max-w-4xl mx-auto px-4 py-4">
          <div className="flex items-center justify-between">
            {/* Logo and Brand */}
            <div className="flex items-center space-x-3">
              <div className="w-8 h-8 rounded-xl overflow-hidden">
                <img 
                  src="/logo.png" 
                  alt="CocoTest Logo" 
                  className="w-full h-full object-cover"
                  onError={(e) => {
                    const target = e.target as HTMLImageElement;
                    target.style.display = 'none';
                    const fallbackIcon = target.nextElementSibling as HTMLElement;
                    if (fallbackIcon) fallbackIcon.style.display = 'flex';
                  }}
                />
                <div className="hidden w-full h-full bg-gradient-to-r from-teal-500 to-cyan-500 items-center justify-center">
                  <span className="text-white font-bold text-sm">C</span>
                </div>
              </div>
              <h1 className="text-xl font-bold bg-gradient-to-r from-teal-600 to-cyan-600 bg-clip-text text-transparent">
                CocoTest
              </h1>
            </div>
            
            <button
              onClick={() => navigate('/')}
              className="flex items-center text-gray-600 hover:text-teal-600 transition-colors"
            >
              <ChevronLeft className="w-5 h-5 mr-1" />
              返回首页
            </button>
          </div>
          
          <div className="flex items-center justify-between mt-4">
            <div className="flex items-center space-x-6">
              <div className="flex items-center space-x-2">
                <Clock className="w-5 h-5 text-gray-500" />
                <span className={`font-mono text-lg ${timeLeft < 300 ? 'text-red-500' : 'text-gray-700'}`}>
                  {formatTime(timeLeft)}
                </span>
              </div>
              
              <div className="flex items-center space-x-2">
                <CheckCircle className="w-5 h-5 text-green-500" />
                <span className="text-gray-700">
                  {answeredCount}/{questions.length}
                </span>
              </div>
            </div>
          </div>
        </div>
      </header>

      {/* Progress Bar */}
      <div className="bg-white/60 backdrop-blur-sm border-b border-teal-100">
        <div className="max-w-4xl mx-auto px-4 py-3">
          <div className="flex items-center justify-between mb-2">
            <span className="text-sm text-gray-600">
              第 {currentQuestionIndex + 1} 题 / 共 {questions.length} 题
            </span>
            <span className="text-sm text-gray-600">
              {Math.round(progress)}% 完成
            </span>
          </div>
          <div className="w-full bg-gray-200 rounded-full h-2">
            <div 
              className="bg-gradient-to-r from-teal-500 to-cyan-500 h-2 rounded-full transition-all duration-300"
              style={{ width: `${progress}%` }}
            ></div>
          </div>
        </div>
      </div>

      {/* Question Content */}
      <main className="max-w-4xl mx-auto px-4 py-8">
        <div className="bg-white rounded-2xl shadow-lg p-8">
          {/* Question */}
          <div className="mb-8">
            <div className="flex items-center mb-4">
              <span className="inline-flex items-center px-3 py-1 rounded-full text-sm font-medium bg-teal-100 text-teal-800">
                {currentQuestion.category || '题目'}
              </span>
              {currentQuestion.difficulty && (
                <span className="ml-2 inline-flex items-center px-3 py-1 rounded-full text-sm font-medium bg-gray-100 text-gray-800">
                  {currentQuestion.difficulty}
                </span>
              )}
            </div>
            <h2 className="text-xl font-semibold text-gray-900 leading-relaxed">
              {currentQuestion.question}
            </h2>
          </div>

          {/* Options */}
          <div className="space-y-4 mb-8">
            {Object.entries(currentQuestion.options).map(([key, value], index) => {
              // 将数字键转换为字母 A, B, C, D
              const optionLetter = String.fromCharCode(65 + index);
              // 用户选择的答案存储为索引格式
              const answerIndex = String(index);
              
              // 只保留分号或顿号前的第一个含义，统一选项格式
              const displayValue = value.split(/[;；、]/)[0].trim();
              
              return (
                <div
                  key={key}
                  className={`p-4 rounded-xl border-2 cursor-pointer transition-all duration-200 ${
                    answers[currentQuestion.id] === answerIndex
                      ? 'border-teal-500 bg-teal-50'
                      : 'border-gray-200 hover:border-teal-300 hover:bg-teal-25'
                  }`}
                  onClick={() => handleAnswerSelect(currentQuestion.id, answerIndex)}
                >
                  <div className="flex items-center">
                    <div className={`w-6 h-6 rounded-full border-2 flex items-center justify-center mr-4 ${
                      answers[currentQuestion.id] === answerIndex
                        ? 'border-teal-500 bg-teal-500'
                        : 'border-gray-300'
                    }`}>
                      {answers[currentQuestion.id] === answerIndex && (
                        <div className="w-2 h-2 bg-white rounded-full"></div>
                      )}
                    </div>
                    <span className="font-medium text-gray-700 mr-3">{optionLetter}.</span>
                    <span className="text-gray-900">{displayValue}</span>
                  </div>
                </div>
              );
            })}
          </div>

          {/* Navigation */}
          <div className="flex items-center justify-between">
            <button
              onClick={handlePrevious}
              disabled={currentQuestionIndex === 0}
              className="flex items-center px-6 py-3 text-gray-600 bg-gray-100 rounded-xl hover:bg-gray-200 disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
            >
              <ChevronLeft className="w-5 h-5 mr-1" />
              上一题
            </button>

            <div className="flex items-center space-x-2">
              {/* 第一题按钮 */}
              {currentQuestionIndex > 3 && (
                <>
                  <button
                    onClick={() => handleQuestionJump(0)}
                    className="w-8 h-8 rounded-full text-sm font-medium transition-colors cursor-pointer bg-gray-100 text-gray-600 hover:bg-gray-200"
                  >
                    1
                  </button>
                  <span className="text-gray-400">...</span>
                </>
              )}

              {/* 显示当前题目附近的按钮（前后各3题） */}
              {questions.map((_, index) => {
                const isNearCurrent = Math.abs(index - currentQuestionIndex) <= 3;
                const isFirst = index === 0;
                const isLast = index === questions.length - 1;
                
                if (!isNearCurrent && !isFirst && !isLast) {
                  return null;
                }
                
                return (
                  <button
                    key={index}
                    onClick={() => handleQuestionJump(index)}
                    className={`w-8 h-8 rounded-full text-sm font-medium transition-colors cursor-pointer ${
                      index === currentQuestionIndex
                        ? 'bg-teal-500 text-white'
                        : answers[questions[index].id]
                        ? 'bg-green-100 text-green-700'
                        : 'bg-gray-100 text-gray-600 hover:bg-gray-200'
                    }`}
                  >
                    {index + 1}
                  </button>
                );
              })}

              {/* 最后一题按钮 */}
              {currentQuestionIndex < questions.length - 4 && (
                <>
                  <span className="text-gray-400">...</span>
                  <button
                    onClick={() => handleQuestionJump(questions.length - 1)}
                    className={`w-8 h-8 rounded-full text-sm font-medium transition-colors cursor-pointer ${
                      answers[questions[questions.length - 1].id]
                        ? 'bg-green-100 text-green-700'
                        : 'bg-gray-100 text-gray-600 hover:bg-gray-200'
                    }`}
                  >
                    {questions.length}
                  </button>
                </>
              )}
            </div>

            {isLastQuestion ? (
              <button
                onClick={handleSubmitTest}
                className="flex items-center px-6 py-3 bg-gradient-to-r from-teal-500 to-cyan-500 text-white rounded-xl hover:from-teal-600 hover:to-cyan-600 transition-all"
              >
                提交测试
                <CheckCircle className="w-5 h-5 ml-1" />
              </button>
            ) : (
              <button
                onClick={handleNext}
                className="flex items-center px-6 py-3 bg-gradient-to-r from-teal-500 to-cyan-500 text-white rounded-xl hover:from-teal-600 hover:to-cyan-600 transition-all"
              >
                下一题
                <ChevronRight className="w-5 h-5 ml-1" />
              </button>
            )}
          </div>
        </div>
      </main>
    </div>
  );
};

export default TestPage;