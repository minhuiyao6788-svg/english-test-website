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
        if (testType === 'cet4_6') {
          fileName = 'cet4_6_questions.json';
        } else if (testType === 'toefl') {
          fileName = 'toefl_questions.json';
        } else if (testType === 'ielts') {
          fileName = 'ielts_questions.json';
        } else if (testType === 'vocabulary') {
          fileName = 'vocabulary_test_questions.json';
        }
        
        const response = await fetch(`/${fileName}`);
        const data: TestData = await response.json();
        setTestData(data);
        
        let selectedQuestions: Question[] = [];
        if (mode === 'basic') {
          selectedQuestions = data.basic_version?.questions || data.questions.slice(0, 50);
        } else {
          selectedQuestions = data.complete_version?.questions || data.questions.slice(0, 100);
        }
        
        setQuestions(selectedQuestions);
        setTimeLeft(selectedQuestions.length * 45); // 每题45秒
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
    
    // 自动跳转到下一题
    setTimeout(() => {
      if (currentQuestionIndex < questions.length - 1) {
        setCurrentQuestionIndex(currentQuestionIndex + 1);
      } else {
        // 最后一题，自动提交测试
        handleSubmitTest();
      }
    }, 300); // 300ms延迟，让用户看到选择效果
  };

  const handleNext = () => {
    if (currentQuestionIndex < questions.length - 1) {
      setCurrentQuestionIndex(currentQuestionIndex + 1);
    }
  };

  const handlePrevious = () => {
    if (currentQuestionIndex > 0) {
      setCurrentQuestionIndex(currentQuestionIndex - 1);
    }
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
            <button
              onClick={() => navigate('/')}
              className="flex items-center text-gray-600 hover:text-teal-600 transition-colors"
            >
              <ChevronLeft className="w-5 h-5 mr-1" />
              返回首页
            </button>
            
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
            {Object.entries(currentQuestion.options).map(([key, value]) => (
              <div
                key={key}
                className={`p-4 rounded-xl border-2 cursor-pointer transition-all duration-200 ${
                  answers[currentQuestion.id] === key
                    ? 'border-teal-500 bg-teal-50'
                    : 'border-gray-200 hover:border-teal-300 hover:bg-teal-25'
                }`}
                onClick={() => handleAnswerSelect(currentQuestion.id, key)}
              >
                <div className="flex items-center">
                  <div className={`w-6 h-6 rounded-full border-2 flex items-center justify-center mr-4 ${
                    answers[currentQuestion.id] === key
                      ? 'border-teal-500 bg-teal-500'
                      : 'border-gray-300'
                  }`}>
                    {answers[currentQuestion.id] === key && (
                      <div className="w-2 h-2 bg-white rounded-full"></div>
                    )}
                  </div>
                  <span className="font-medium text-gray-700 mr-3">{String.fromCharCode(65 + parseInt(key))}.</span>
                  <span className="text-gray-900">{value}</span>
                </div>
              </div>
            ))}
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
              {questions.map((_, index) => (
                <button
                  key={index}
                  onClick={() => setCurrentQuestionIndex(index)}
                  className={`w-8 h-8 rounded-full text-sm font-medium transition-colors ${
                    index === currentQuestionIndex
                      ? 'bg-teal-500 text-white'
                      : answers[questions[index].id]
                      ? 'bg-green-100 text-green-700'
                      : 'bg-gray-100 text-gray-600 hover:bg-gray-200'
                  }`}
                >
                  {index + 1}
                </button>
              ))}
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