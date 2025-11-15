import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { BookOpen, Clock, Target, Users, Zap } from 'lucide-react';

const HomePage: React.FC = () => {
  const navigate = useNavigate();
  const [selectedTest, setSelectedTest] = useState<string>('');
  const [selectedLevel, setSelectedLevel] = useState<string>(''); // 四级或六级
  const [selectedMode, setSelectedMode] = useState<string>('');

  const testTypes = [
    {
      id: 'cet4_6',
      title: '大学英语四六级',
      description: '适合中国大学生和职场人士',
      icon: BookOpen,
      color: 'from-emerald-600 to-teal-600',
      bgColor: 'bg-emerald-50',
      borderColor: 'border-emerald-300'
    },
    {
      id: 'ielts',
      title: '雅思 IELTS',
      description: '适合国际交流和留学申请',
      icon: Users,
      color: 'from-teal-600 to-cyan-600',
      bgColor: 'bg-teal-50',
      borderColor: 'border-teal-300'
    },
    {
      id: 'vocabulary',
      title: '词汇量测试',
      description: '测试您的英语词汇掌握程度',
      icon: Zap,
      color: 'from-green-600 to-emerald-600',
      bgColor: 'bg-green-50',
      borderColor: 'border-green-300'
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
      color: 'from-emerald-600 to-teal-600'
    },
    {
      id: 'complete',
      title: '完整版',
      description: '100题，约60-80分钟',
      questions: 100,
      time: '60-80分钟',
      icon: Clock,
      color: 'from-teal-600 to-cyan-600'
    }
  ];

  // 四六级级别选项
  const cetLevels = [
    {
      id: 'cet4',
      title: '英语四级',
      description: '适合大学一二年级学生',
      icon: BookOpen,
      color: 'from-emerald-600 to-teal-600'
    },
    {
      id: 'cet6',
      title: '英语六级',
      description: '适合大学三四年级学生',
      icon: Target,
      color: 'from-teal-600 to-cyan-600'
    }
  ];

  const handleStartTest = () => {
    // 四六级需要选择级别
    if (selectedTest === 'cet4_6' && selectedLevel && selectedMode) {
      navigate('/test', { 
        state: { 
          testType: selectedLevel, // 传递 cet4 或 cet6
          mode: selectedMode 
        } 
      });
    } else if (selectedTest !== 'cet4_6' && selectedTest && selectedMode) {
      // 其他测试类型
      navigate('/test', { 
        state: { 
          testType: selectedTest, 
          mode: selectedMode 
        } 
      });
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-emerald-50 via-teal-50 to-cyan-50 relative overflow-hidden">
      {/* 背景装饰元素 - 椰子叶主题 */}
      <div className="absolute top-0 left-0 w-full h-full overflow-hidden pointer-events-none">
        <div className="absolute top-20 left-10 w-72 h-72 bg-gradient-to-br from-emerald-200/20 to-teal-200/20 rounded-full blur-3xl"></div>
        <div className="absolute bottom-20 right-10 w-96 h-96 bg-gradient-to-br from-teal-200/20 to-cyan-200/20 rounded-full blur-3xl"></div>
        <div className="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 w-80 h-80 bg-gradient-to-br from-green-200/15 to-emerald-200/15 rounded-full blur-3xl"></div>
      </div>

      {/* Header */}
      <header className="bg-white/70 backdrop-blur-md border-b border-emerald-100/50 shadow-sm sticky top-0 z-50 relative">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-5">
          <div className="flex items-center justify-center">
            {/* Logo and Brand */}
            <div className="flex items-center space-x-4">
              <div className="w-12 h-12 rounded-2xl overflow-hidden shadow-lg transform hover:scale-110 transition-transform duration-300">
                <img 
                  src="/logo.png" 
                  alt="CocoTest Logo" 
                  className="w-full h-full object-cover"
                  onError={(e) => {
                    // 如果图片加载失败，显示默认图标
                    const target = e.target as HTMLImageElement;
                    target.style.display = 'none';
                    const fallbackIcon = target.nextElementSibling as HTMLElement;
                    if (fallbackIcon) fallbackIcon.style.display = 'flex';
                  }}
                />
                <div className="hidden w-full h-full bg-gradient-to-br from-emerald-600 via-teal-600 to-green-600 items-center justify-center">
                  <BookOpen className="w-7 h-7 text-white" />
                </div>
              </div>
              <div>
                <h1 className="text-3xl font-extrabold bg-gradient-to-r from-emerald-700 via-teal-700 to-green-700 bg-clip-text text-transparent">
                  CocoTest
                </h1>
                <p className="text-sm text-emerald-700/80 font-medium">专业英语水平测试平台</p>
              </div>
            </div>
          </div>
        </div>
      </header>

      {/* Main Content */}
      <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16 relative z-10">
        {/* Hero Section */}
        <div className="text-center mb-20">
          <div className="inline-block mb-6">
            <span className="inline-flex items-center px-4 py-2 rounded-full bg-gradient-to-r from-emerald-500/10 to-teal-500/10 border border-emerald-300/50 text-emerald-800 text-sm font-semibold backdrop-blur-sm">
              <span className="w-2 h-2 bg-emerald-600 rounded-full mr-2 animate-pulse"></span>
              专业·准确·快速
            </span>
          </div>
          <h2 className="text-6xl md:text-7xl font-extrabold text-gray-900 mb-8 leading-tight">
            测一测你的
            <span className="block mt-2 bg-gradient-to-r from-emerald-700 via-teal-700 to-green-700 bg-clip-text text-transparent">英语水平</span>
          </h2>
          <p className="text-xl md:text-2xl text-gray-700 max-w-4xl mx-auto leading-relaxed font-light">
            选择适合的测试类型和难度，获得专业的英语能力评估报告。<br/>
            支持四六级、雅思、词汇量测试，全面评估英语水平。
          </p>
        </div>

        {/* Test Type Selection */}
        <section className="mb-20">
          <div className="text-center mb-12">
            <h3 className="text-4xl font-bold text-gray-900 mb-4">
              选择测试类型
            </h3>
            <p className="text-gray-600 text-lg">三种专业测试，全面评估您的英语能力</p>
          </div>
          <div className="grid md:grid-cols-3 gap-8">
            {testTypes.map((test) => {
              const IconComponent = test.icon;
              return (
                <div
                  key={test.id}
                  className={`group relative p-8 rounded-3xl border-2 cursor-pointer transition-all duration-500 transform hover:-translate-y-2 ${
                    selectedTest === test.id
                      ? `${test.borderColor} ${test.bgColor} shadow-2xl scale-105`
                      : 'border-gray-200 bg-white/80 backdrop-blur-sm hover:border-emerald-300 hover:shadow-xl'
                  }`}
                  onClick={() => setSelectedTest(test.id)}
                >
                  {/* 背景渐变效果 */}
                  <div className={`absolute inset-0 rounded-3xl bg-gradient-to-br ${
                    selectedTest === test.id ? test.color : 'from-transparent to-transparent'
                  } opacity-5 transition-opacity duration-500`}></div>
                  
                  <div className="relative text-center">
                    <div className={`w-20 h-20 mx-auto mb-6 rounded-2xl bg-gradient-to-br ${test.color} flex items-center justify-center shadow-lg transform group-hover:scale-125 transition-all duration-300`}>
                      <IconComponent className="w-10 h-10 text-white" />
                    </div>
                    <h4 className="text-2xl font-bold text-gray-900 mb-3">{test.title}</h4>
                    <p className="text-gray-600 leading-relaxed">{test.description}</p>
                  </div>
                  {selectedTest === test.id && (
                    <div className="absolute -top-3 -right-3 animate-bounce">
                      <div className="w-8 h-8 bg-gradient-to-br from-emerald-600 to-teal-600 rounded-full flex items-center justify-center shadow-lg">
                        <svg className="w-5 h-5 text-white" fill="currentColor" viewBox="0 0 20 20">
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
          <>
            {/* 四六级需要先选择级别 */}
            {selectedTest === 'cet4_6' && (
              <section className="mb-20 animate-fadeIn">
                <div className="text-center mb-12">
                  <h3 className="text-4xl font-bold text-gray-900 mb-4">
                    选择级别
                  </h3>
                  <p className="text-gray-600 text-lg">根据您的学习阶段选择合适的级别</p>
                </div>
                <div className="grid md:grid-cols-2 gap-8 max-w-5xl mx-auto">
                  {cetLevels.map((level) => {
                    const IconComponent = level.icon;
                    return (
                      <div
                        key={level.id}
                        className={`group relative p-10 rounded-3xl border-2 cursor-pointer transition-all duration-500 transform hover:-translate-y-2 ${
                          selectedLevel === level.id
                            ? 'border-emerald-300 bg-gradient-to-br from-emerald-50 to-teal-50 shadow-2xl scale-105'
                            : 'border-gray-200 bg-white/80 backdrop-blur-sm hover:border-emerald-300 hover:shadow-xl'
                        }`}
                        onClick={() => setSelectedLevel(level.id)}
                      >
                        <div className="relative text-center">
                          <div className={`w-20 h-20 mx-auto mb-6 rounded-2xl bg-gradient-to-br ${level.color} flex items-center justify-center shadow-lg transform group-hover:scale-125 transition-all duration-300`}>
                            <IconComponent className="w-10 h-10 text-white" />
                          </div>
                          <h4 className="text-2xl font-bold text-gray-900 mb-3">{level.title}</h4>
                          <p className="text-gray-600 text-lg leading-relaxed">{level.description}</p>
                        </div>
                        {selectedLevel === level.id && (
                          <div className="absolute -top-3 -right-3 animate-bounce">
                            <div className="w-8 h-8 bg-gradient-to-br from-emerald-600 to-teal-600 rounded-full flex items-center justify-center shadow-lg">
                              <svg className="w-5 h-5 text-white" fill="currentColor" viewBox="0 0 20 20">
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

            {/* 测试模式选择：四六级需要先选级别，其他直接显示 */}
            {(selectedTest !== 'cet4_6' || selectedLevel) && (
              <section className="mb-20 animate-fadeIn">
                <div className="text-center mb-12">
                  <h3 className="text-4xl font-bold text-gray-900 mb-4">
                    选择测试模式
                  </h3>
                  <p className="text-gray-600 text-lg">基础版适合快速评估，完整版更全面深入</p>
                </div>
                <div className="grid md:grid-cols-2 gap-8 max-w-5xl mx-auto">
                  {modes.map((mode) => {
                    const IconComponent = mode.icon;
                    return (
                      <div
                        key={mode.id}
                        className={`group relative p-10 rounded-3xl border-2 cursor-pointer transition-all duration-500 transform hover:-translate-y-2 ${
                          selectedMode === mode.id
                            ? 'border-emerald-300 bg-gradient-to-br from-emerald-50 to-teal-50 shadow-2xl scale-105'
                            : 'border-gray-200 bg-white/80 backdrop-blur-sm hover:border-emerald-300 hover:shadow-xl'
                        }`}
                        onClick={() => setSelectedMode(mode.id)}
                      >
                        <div className="relative text-center">
                          <div className={`w-20 h-20 mx-auto mb-6 rounded-2xl bg-gradient-to-br ${mode.color} flex items-center justify-center shadow-lg transform group-hover:scale-125 transition-all duration-300`}>
                            <IconComponent className="w-10 h-10 text-white" />
                          </div>
                          <h4 className="text-2xl font-bold text-gray-900 mb-4">{mode.title}</h4>
                          <p className="text-gray-600 text-lg mb-6">{mode.description}</p>
                          <div className="flex justify-center space-x-8">
                            <div className="flex items-center px-4 py-2 bg-white/50 rounded-xl">
                              <div className="w-2 h-2 bg-emerald-600 rounded-full mr-2"></div>
                              <span className="text-sm font-semibold text-gray-700">{mode.questions}题</span>
                            </div>
                            <div className="flex items-center px-4 py-2 bg-white/50 rounded-xl">
                              <div className="w-2 h-2 bg-teal-600 rounded-full mr-2"></div>
                              <span className="text-sm font-semibold text-gray-700">{mode.time}</span>
                            </div>
                          </div>
                        </div>
                        {selectedMode === mode.id && (
                          <div className="absolute -top-3 -right-3 animate-bounce">
                            <div className="w-8 h-8 bg-gradient-to-br from-emerald-600 to-teal-600 rounded-full flex items-center justify-center shadow-lg">
                              <svg className="w-5 h-5 text-white" fill="currentColor" viewBox="0 0 20 20">
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
          </>
        )}

        {/* Start Button */}
        {((selectedTest === 'cet4_6' && selectedLevel && selectedMode) || 
          (selectedTest !== 'cet4_6' && selectedTest && selectedMode)) && (
          <section className="text-center mb-24 animate-fadeIn">
            <button
              onClick={handleStartTest}
              className="group relative inline-flex items-center px-16 py-5 text-xl font-bold text-white bg-gradient-to-r from-emerald-600 via-teal-600 to-cyan-600 rounded-full hover:from-emerald-700 hover:via-teal-700 hover:to-cyan-700 transform hover:scale-110 transition-all duration-300 shadow-2xl hover:shadow-3xl overflow-hidden"
            >
              <span className="absolute inset-0 w-full h-full bg-gradient-to-r from-white/0 via-white/20 to-white/0 transform translate-x-full group-hover:translate-x-[-100%] transition-transform duration-1000"></span>
              <span className="relative">开始测试</span>
              <svg className="relative w-7 h-7 ml-3 transform group-hover:translate-x-2 transition-transform duration-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2.5} d="M13 7l5 5m0 0l-5 5m5-5H6" />
              </svg>
            </button>
            <p className="mt-6 text-emerald-700 text-sm">预计用时 {selectedMode === 'basic' ? '30-40' : '60-80'} 分钟，请合理安排时间</p>
          </section>
        )}

        {/* Features */}
        <section className="grid md:grid-cols-4 gap-6">
          <div className="text-center p-8 bg-white/70 backdrop-blur-md rounded-3xl border border-emerald-100 shadow-lg">
            <div className="w-16 h-16 mx-auto mb-5 bg-gradient-to-br from-emerald-600 to-teal-600 rounded-2xl flex items-center justify-center shadow-lg">
              <BookOpen className="w-8 h-8 text-white" />
            </div>
            <h4 className="text-lg font-bold text-gray-900 mb-2">专业题库</h4>
            <p className="text-sm text-gray-600">权威考试标准</p>
          </div>
          <div className="text-center p-8 bg-white/70 backdrop-blur-md rounded-3xl border border-emerald-100 shadow-lg">
            <div className="w-16 h-16 mx-auto mb-5 bg-gradient-to-br from-teal-600 to-cyan-600 rounded-2xl flex items-center justify-center shadow-lg">
              <Clock className="w-8 h-8 text-white" />
            </div>
            <h4 className="text-lg font-bold text-gray-900 mb-2">智能计时</h4>
            <p className="text-sm text-gray-600">实时进度跟踪</p>
          </div>
          <div className="text-center p-8 bg-white/70 backdrop-blur-md rounded-3xl border border-emerald-100 shadow-lg">
            <div className="w-16 h-16 mx-auto mb-5 bg-gradient-to-br from-green-600 to-emerald-600 rounded-2xl flex items-center justify-center shadow-lg">
              <Target className="w-8 h-8 text-white" />
            </div>
            <h4 className="text-lg font-bold text-gray-900 mb-2">精准评估</h4>
            <p className="text-sm text-gray-600">详细能力分析</p>
          </div>
          <div className="text-center p-8 bg-white/70 backdrop-blur-md rounded-3xl border border-emerald-100 shadow-lg">
            <div className="w-16 h-16 mx-auto mb-5 bg-gradient-to-br from-emerald-700 to-teal-700 rounded-2xl flex items-center justify-center shadow-lg">
              <Users className="w-8 h-8 text-white" />
            </div>
            <h4 className="text-lg font-bold text-gray-900 mb-2">友好体验</h4>
            <p className="text-sm text-gray-600">15-60岁适用</p>
          </div>
        </section>

        {/* Footer */}
        <footer className="mt-20 text-center pb-8">
          <div className="text-gray-500 text-sm">
            <p className="mb-2">© 2025 CocoTest. All rights reserved.</p>
            <p className="mb-2">专业英语水平测试平台 | 让英语学习更简单</p>
            <p className="text-xs text-gray-400">版本 v1.1.0</p>
          </div>
        </footer>
      </main>
    </div>
  );
};

export default HomePage;
