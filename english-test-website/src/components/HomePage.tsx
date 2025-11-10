import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { BookOpen, Clock, Target, Users, Zap } from 'lucide-react';

const HomePage: React.FC = () => {
  const navigate = useNavigate();
  const [selectedTest, setSelectedTest] = useState<string>('');
  const [selectedMode, setSelectedMode] = useState<string>('');

  const testTypes = [
    {
      id: 'cet4_6',
      title: '大学英语四六级',
      description: '适合中国大学生和职场人士',
      icon: BookOpen,
      color: 'from-blue-500 to-blue-600',
      bgColor: 'bg-blue-50',
      borderColor: 'border-blue-200'
    },
    {
      id: 'toefl',
      title: '托福 TOEFL',
      description: '适合准备留学申请的学生',
      icon: Target,
      color: 'from-green-500 to-green-600',
      bgColor: 'bg-green-50',
      borderColor: 'border-green-200'
    },
    {
      id: 'ielts',
      title: '雅思 IELTS',
      description: '适合国际交流和移民申请',
      icon: Users,
      color: 'from-purple-500 to-purple-600',
      bgColor: 'bg-purple-50',
      borderColor: 'border-purple-200'
    },
    {
      id: 'vocabulary',
      title: '词汇量测试',
      description: '测试您的英语词汇掌握程度',
      icon: Zap,
      color: 'from-orange-500 to-red-500',
      bgColor: 'bg-orange-50',
      borderColor: 'border-orange-200'
    }
  ];

  const modes = [
    {
      id: 'basic',
      title: '基础版',
      description: '50题，约30-40分钟',
      questions: 50,
      time: '30-40分钟',
      icon: Clock,
      color: 'from-teal-500 to-cyan-500'
    },
    {
      id: 'complete',
      title: '完整版',
      description: '100题，约60-80分钟',
      questions: 100,
      time: '60-80分钟',
      icon: Clock,
      color: 'from-emerald-500 to-teal-500'
    }
  ];

  const handleStartTest = () => {
    if (selectedTest && selectedMode) {
      navigate('/test', { 
        state: { 
          testType: selectedTest, 
          mode: selectedMode 
        } 
      });
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-teal-50 via-cyan-50 to-blue-50">
      {/* Header */}
      <header className="bg-white/80 backdrop-blur-sm border-b border-teal-100 sticky top-0 z-10">
        <div className="max-w-6xl mx-auto px-4 py-4">
          <div className="flex items-center justify-center">
            <div className="flex items-center space-x-3">
              <div className="w-10 h-10 bg-gradient-to-r from-teal-500 to-cyan-500 rounded-xl flex items-center justify-center">
                <BookOpen className="w-6 h-6 text-white" />
              </div>
              <h1 className="text-2xl font-bold bg-gradient-to-r from-teal-600 to-cyan-600 bg-clip-text text-transparent">
                英语测试demo版
              </h1>
            </div>
          </div>
        </div>
      </header>

      {/* Main Content */}
      <main className="max-w-6xl mx-auto px-4 py-12">
        {/* Hero Section */}
        <div className="text-center mb-16">
          <h2 className="text-5xl font-bold text-gray-900 mb-6">
            测一测你的
            <span className="bg-gradient-to-r from-teal-600 to-cyan-600 bg-clip-text text-transparent"> 英语水平</span>
          </h2>
          <p className="text-xl text-gray-600 max-w-3xl mx-auto leading-relaxed">
            选择适合的测试类型和难度，获得专业的英语能力评估报告。
            支持四六级、托福、雅思三种主流考试标准。
          </p>
        </div>

        {/* Test Type Selection */}
        <section className="mb-16">
          <h3 className="text-3xl font-semibold text-gray-900 mb-8 text-center">
            选择测试类型
          </h3>
          <div className="grid md:grid-cols-3 gap-6">
            {testTypes.map((test) => {
              const IconComponent = test.icon;
              return (
                <div
                  key={test.id}
                  className={`relative p-6 rounded-2xl border-2 cursor-pointer transition-all duration-300 hover:scale-105 hover:shadow-lg ${
                    selectedTest === test.id
                      ? `${test.borderColor} ${test.bgColor} shadow-lg`
                      : 'border-gray-200 bg-white hover:border-teal-200'
                  }`}
                  onClick={() => setSelectedTest(test.id)}
                >
                  <div className="text-center">
                    <div className={`w-16 h-16 mx-auto mb-4 rounded-2xl bg-gradient-to-r ${test.color} flex items-center justify-center`}>
                      <IconComponent className="w-8 h-8 text-white" />
                    </div>
                    <h4 className="text-xl font-semibold text-gray-900 mb-2">{test.title}</h4>
                    <p className="text-gray-600">{test.description}</p>
                  </div>
                  {selectedTest === test.id && (
                    <div className="absolute top-4 right-4">
                      <div className="w-6 h-6 bg-teal-500 rounded-full flex items-center justify-center">
                        <svg className="w-4 h-4 text-white" fill="currentColor" viewBox="0 0 20 20">
                          <path fillRule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clipRule="evenodd" />
                        </svg>
                      </div>
                    </div>
                  )}
                </div>
              );
            })}
          </div>
        </section>

        {/* Mode Selection */}
        {selectedTest && (
          <section className="mb-16">
            <h3 className="text-3xl font-semibold text-gray-900 mb-8 text-center">
              选择测试模式
            </h3>
            <div className="grid md:grid-cols-2 gap-6 max-w-4xl mx-auto">
              {modes.map((mode) => {
                const IconComponent = mode.icon;
                return (
                  <div
                    key={mode.id}
                    className={`relative p-8 rounded-2xl border-2 cursor-pointer transition-all duration-300 hover:scale-105 hover:shadow-lg ${
                      selectedMode === mode.id
                        ? 'border-teal-300 bg-teal-50 shadow-lg'
                        : 'border-gray-200 bg-white hover:border-teal-200'
                    }`}
                    onClick={() => setSelectedMode(mode.id)}
                  >
                    <div className="text-center">
                      <div className={`w-16 h-16 mx-auto mb-4 rounded-2xl bg-gradient-to-r ${mode.color} flex items-center justify-center`}>
                        <IconComponent className="w-8 h-8 text-white" />
                      </div>
                      <h4 className="text-2xl font-semibold text-gray-900 mb-2">{mode.title}</h4>
                      <p className="text-gray-600 mb-4">{mode.description}</p>
                      <div className="flex justify-center space-x-6 text-sm text-gray-500">
                        <span className="flex items-center">
                          <span className="w-2 h-2 bg-teal-500 rounded-full mr-2"></span>
                          {mode.questions}题
                        </span>
                        <span className="flex items-center">
                          <span className="w-2 h-2 bg-cyan-500 rounded-full mr-2"></span>
                          {mode.time}
                        </span>
                      </div>
                    </div>
                    {selectedMode === mode.id && (
                      <div className="absolute top-4 right-4">
                        <div className="w-6 h-6 bg-teal-500 rounded-full flex items-center justify-center">
                          <svg className="w-4 h-4 text-white" fill="currentColor" viewBox="0 0 20 20">
                            <path fillRule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clipRule="evenodd" />
                          </svg>
                        </div>
                      </div>
                    )}
                  </div>
                );
              })}
            </div>
          </section>
        )}

        {/* Start Button */}
        {selectedTest && selectedMode && (
          <section className="text-center">
            <button
              onClick={handleStartTest}
              className="inline-flex items-center px-12 py-4 text-lg font-semibold text-white bg-gradient-to-r from-teal-500 to-cyan-500 rounded-2xl hover:from-teal-600 hover:to-cyan-600 transform hover:scale-105 transition-all duration-300 shadow-lg hover:shadow-xl"
            >
              <span>开始测试</span>
              <svg className="w-6 h-6 ml-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13 7l5 5m0 0l-5 5m5-5H6" />
              </svg>
            </button>
          </section>
        )}

        {/* Features */}
        <section className="mt-20 grid md:grid-cols-4 gap-6">
          <div className="text-center p-6 bg-white/60 backdrop-blur-sm rounded-2xl border border-teal-100">
            <div className="w-12 h-12 mx-auto mb-4 bg-gradient-to-r from-blue-500 to-blue-600 rounded-xl flex items-center justify-center">
              <BookOpen className="w-6 h-6 text-white" />
            </div>
            <h4 className="font-semibold text-gray-900 mb-2">专业题库</h4>
            <p className="text-sm text-gray-600">权威考试标准</p>
          </div>
          <div className="text-center p-6 bg-white/60 backdrop-blur-sm rounded-2xl border border-teal-100">
            <div className="w-12 h-12 mx-auto mb-4 bg-gradient-to-r from-green-500 to-green-600 rounded-xl flex items-center justify-center">
              <Clock className="w-6 h-6 text-white" />
            </div>
            <h4 className="font-semibold text-gray-900 mb-2">智能计时</h4>
            <p className="text-sm text-gray-600">实时进度跟踪</p>
          </div>
          <div className="text-center p-6 bg-white/60 backdrop-blur-sm rounded-2xl border border-teal-100">
            <div className="w-12 h-12 mx-auto mb-4 bg-gradient-to-r from-purple-500 to-purple-600 rounded-xl flex items-center justify-center">
              <Target className="w-6 h-6 text-white" />
            </div>
            <h4 className="font-semibold text-gray-900 mb-2">精准评估</h4>
            <p className="text-sm text-gray-600">详细能力分析</p>
          </div>
          <div className="text-center p-6 bg-white/60 backdrop-blur-sm rounded-2xl border border-teal-100">
            <div className="w-12 h-12 mx-auto mb-4 bg-gradient-to-r from-orange-500 to-orange-600 rounded-xl flex items-center justify-center">
              <Users className="w-6 h-6 text-white" />
            </div>
            <h4 className="font-semibold text-gray-900 mb-2">友好体验</h4>
            <p className="text-sm text-gray-600">15-60岁适用</p>
          </div>
        </section>
      </main>
    </div>
  );
};

export default HomePage;
