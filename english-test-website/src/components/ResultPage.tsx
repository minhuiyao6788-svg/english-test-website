import React, { useState, useEffect } from 'react';
import { useNavigate, useLocation } from 'react-router-dom';
import { Trophy, Clock, Target, BookOpen, RotateCcw, Home, Star, Award, Mail, Send, BarChart3, PieChart } from 'lucide-react';
import { BarChart, Bar, PieChart as RechartsPieChart, Pie, Cell, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';

interface ResultData {
  testType: string;
  mode: string;
  answers: { [key: string]: string };
  questions: any[];
  timeUsed: number;
}

interface ScoreResult {
  score: number;
  percentage: number;
  level: string;
  levelDescription: string;
  recommendations: string[];
}

const ResultPage: React.FC = () => {
  const navigate = useNavigate();
  const location = useLocation();
  const { testType, mode, answers, questions, timeUsed } = location.state as ResultData;

  const [scoreResult, setScoreResult] = useState<ScoreResult | null>(null);
  const [detailedResults, setDetailedResults] = useState<any[]>([]);
  const [email, setEmail] = useState<string>('');
  const [emailSent, setEmailSent] = useState<boolean>(false);
  const [sendingEmail, setSendingEmail] = useState<boolean>(false);
  const [categoryStats, setCategoryStats] = useState<any[]>([]);
  const [pieData, setPieData] = useState<any[]>([]);

  useEffect(() => {
    if (!location.state) {
      navigate('/');
      return;
    }

    calculateResults();
  }, [location.state, navigate]);

  const calculateResults = () => {
    let correctAnswers = 0;
    const results = questions.map((question, index) => {
      const userAnswer = answers[question.id]; // 用户答案格式为索引 "0", "1", "2", "3"
      // 支持两种答案字段名: answer (CET4/6等) 和 correct_answer (其他测试)
      const correctAnswerRaw = (question as any).answer || question.correct_answer;
      
      // 将正确答案统一转换为索引格式 (0, 1, 2, 3)
      let correctAnswerIndex = correctAnswerRaw;
      if (/^[A-D]$/i.test(correctAnswerRaw)) {
        // 如果是字母格式 (A, B, C, D)，转换为索引
        correctAnswerIndex = String(correctAnswerRaw.toUpperCase().charCodeAt(0) - 65);
      }
      
      const isCorrect = userAnswer === correctAnswerIndex;
      if (isCorrect) correctAnswers++;
      
      // 处理答案显示：将索引转换为字母 A, B, C, D
      const formatAnswer = (answer: string) => {
        if (!answer) return undefined;
        // 如果是数字，转换为字母
        if (/^[0-3]$/.test(answer)) {
          return String.fromCharCode(65 + parseInt(answer));
        }
        // 如果已经是字母，直接返回
        return answer.toUpperCase();
      };
      
      return {
        questionNumber: index + 1,
        question: question.question,
        userAnswer: formatAnswer(userAnswer),
        correctAnswer: formatAnswer(correctAnswerIndex),
        isCorrect,
        explanation: question.explanation,
        category: question.category || '未知',
        // 词汇测试特有字段
        word: (question as any).word,
        example_sentence: (question as any).example_sentence
      };
    });

    const percentage = Math.round((correctAnswers / questions.length) * 100);
    const score = Math.round(percentage);

    // 调试信息
    console.log('=== 测试结果计算 ===');
    console.log('总题数:', questions.length);
    console.log('正确题数:', correctAnswers);
    console.log('正确率:', percentage + '%');
    console.log('分数:', score);

    let level = '';
    let levelDescription = '';
    let recommendations: string[] = [];

    // 根据测试类型和分数确定等级
    if (testType === 'vocabulary') {
      if (score >= 90) {
        level = '词汇大师';
        levelDescription = '您的词汇量已达到8000+水平，具备优秀的英语表达能力';
        recommendations = ['继续保持词汇学习', '多阅读英文原版书籍', '参与英语写作和演讲练习'];
      } else if (score >= 80) {
        level = '词汇达人';
        levelDescription = '您的词汇量约在5000-8000之间，具备良好的英语理解能力';
        recommendations = ['继续扩充高级词汇', '学习词汇的深层含义', '加强词汇的实际运用'];
      } else if (score >= 70) {
        level = '词汇进阶';
        levelDescription = '您的词汇量约在3000-5000之间，具备中等英语水平';
        recommendations = ['重点学习常用词汇', '掌握词汇的多种用法', '增加词汇练习量'];
      } else if (score >= 60) {
        level = '词汇基础';
        levelDescription = '您的词汇量约在2000-3000之间，需要加强基础词汇学习';
        recommendations = ['重点记忆基础词汇', '学习词汇的基本用法', '多背诵常用短语'];
      } else {
        level = '词汇初学';
        levelDescription = '您的词汇量需要大量提升，建议从最基础的词汇开始';
        recommendations = ['从最基础的1000个单词开始', '使用词汇卡片记忆', '每天坚持词汇学习'];
      }
    } else if (testType === 'cet4' || testType === 'cet6' || testType === 'cet4_6') {
      if (score >= 90) {
        level = '优秀';
        levelDescription = '您的英语水平已达到优秀标准，具备扎实的语言基础';
        recommendations = ['继续保持当前学习状态', '可以尝试更高级的英语考试', '多参与英语交流活动'];
      } else if (score >= 80) {
        level = '良好';
        levelDescription = '您的英语水平良好，在多数场景下能够流利交流';
        recommendations = ['加强薄弱环节的练习', '扩大词汇量', '多听英语广播和观看英文影片'];
      } else if (score >= 70) {
        level = '中等';
        levelDescription = '您的英语水平中等，具备基本的交流能力';
        recommendations = ['系统学习语法知识', '增加阅读量', '练习口语表达'];
      } else if (score >= 60) {
        level = '及格';
        levelDescription = '您的英语水平刚刚及格，需要加强基础学习';
        recommendations = ['重点学习基础词汇', '加强语法练习', '多做模拟试题'];
      } else {
        level = '需要提高';
        levelDescription = '您的英语基础需要加强，建议从基础开始学习';
        recommendations = ['从基础词汇开始', '学习基本语法规则', '多听多读多练习'];
      }
    } else if (testType === 'ielts') {
      if (score >= 8.0) {
        level = '优秀 (8.0+)';
        levelDescription = '您的雅思水平优秀，可以申请任何英语国家大学';
        recommendations = ['保持当前水平', '关注学术英语', '参与国际交流'];
      } else if (score >= 7.0) {
        level = '良好 (7.0)';
        levelDescription = '您的雅思水平良好，可以申请大部分国外大学';
        recommendations = ['提升写作水平', '加强口语流利度', '扩大词汇量'];
      } else if (score >= 6.0) {
        level = '中等 (6.0)';
        levelDescription = '您的雅思水平中等，需要进一步提升';
        recommendations = ['加强语法准确性', '提升听力理解', '练习写作结构'];
      } else {
        level = '需要提高 (6.0以下)';
        levelDescription = '您的雅思基础需要加强，建议系统学习';
        recommendations = ['从基础开始', '大量练习真题', '寻求专业指导'];
      }
    }

    setScoreResult({
      score,
      percentage,
      level,
      levelDescription,
      recommendations
    });

    setDetailedResults(results);
    
    // 计算分类统计数据
    const categoryMap = new Map<string, { correct: number; total: number }>();
    results.forEach(result => {
      const category = result.category;
      if (!categoryMap.has(category)) {
        categoryMap.set(category, { correct: 0, total: 0 });
      }
      const stats = categoryMap.get(category)!;
      stats.total++;
      if (result.isCorrect) {
        stats.correct++;
      }
    });
    
    const categoryStatsData = Array.from(categoryMap.entries()).map(([category, stats]) => ({
      name: category === 'vocabulary' ? '词汇' : 
            category === 'grammar' ? '语法' : 
            category === 'reading' ? '阅读' : category,
      正确率: Math.round((stats.correct / stats.total) * 100),
      正确: stats.correct,
      错误: stats.total - stats.correct,
      总数: stats.total
    }));
    
    setCategoryStats(categoryStatsData);
    
    // 计算饼图数据
    const correctCount = results.filter(r => r.isCorrect).length;
    const incorrectCount = results.length - correctCount;
    setPieData([
      { name: '正确', value: correctCount, percentage: Math.round((correctCount / results.length) * 100) },
      { name: '错误', value: incorrectCount, percentage: Math.round((incorrectCount / results.length) * 100) }
    ]);
  };

  const getTestTypeName = (type: string) => {
    switch (type) {
      case 'cet4': return '大学英语四级';
      case 'cet6': return '大学英语六级';
      case 'cet4_6': return '大学英语四六级';
      case 'ielts': return '雅思 IELTS';
      case 'vocabulary': return '词汇量测试';
      default: return '英语测试';
    }
  };

  const getModeName = (mode: string) => {
    return mode === 'basic' ? '基础版' : '完整版';
  };

  const formatTime = (seconds: number) => {
    const hours = Math.floor(seconds / 3600);
    const minutes = Math.floor((seconds % 3600) / 60);
    const secs = seconds % 60;
    
    if (hours > 0) {
      return `${hours}小时${minutes}分钟${secs}秒`;
    } else if (minutes > 0) {
      return `${minutes}分钟${secs}秒`;
    } else {
      return `${secs}秒`;
    }
  };

  const getScoreColor = (score: number) => {
    if (score >= 90) return 'text-green-600';
    if (score >= 80) return 'text-blue-600';
    if (score >= 70) return 'text-yellow-600';
    if (score >= 60) return 'text-orange-600';
    return 'text-red-600';
  };

  const getScoreBgColor = (score: number) => {
    if (score >= 90) return 'from-green-400 to-green-600';
    if (score >= 80) return 'from-blue-400 to-blue-600';
    if (score >= 70) return 'from-yellow-400 to-yellow-600';
    if (score >= 60) return 'from-orange-400 to-orange-600';
    return 'from-red-400 to-red-600';
  };

  const handleSendEmail = async () => {
    if (!email || !email.includes('@')) {
      alert('请输入有效的邮箱地址');
      return;
    }

    setSendingEmail(true);
    
    try {
      const correctAnswers = detailedResults.filter(r => r.isCorrect).length;
      
      const requestBody = {
        email,
        testType: getTestTypeName(testType),
        mode: getModeName(mode),
        score: scoreResult?.score || 0,
        totalQuestions: questions.length,
        correctAnswers: correctAnswers
      };

      console.log('发送邮件请求:', requestBody);
      
      const response = await fetch('/api/send-email', {
        method: 'POST',
        headers: { 
          'Content-Type': 'application/json',
          'Accept': 'application/json'
        },
        body: JSON.stringify(requestBody)
      });
      
      console.log('响应状态:', response.status);
      console.log('Content-Type:', response.headers.get('content-type'));

      // 检查响应是否为 JSON 格式
      const contentType = response.headers.get('content-type');
      if (!contentType || !contentType.includes('application/json')) {
        const text = await response.text();
        console.error('服务器返回非-JSON 响应:', text);
        throw new Error(`服务器错误 (${response.status}): 请检查后端配置`);
      }
      
      const data = await response.json();
      console.log('响应数据:', data);
      
      if (response.ok && data.success) {
        setEmailSent(true);
        alert(`✅ 测试结果已成功发送至 ${email}！\n请查收您的邮箱。`);
      } else {
        throw new Error(data.error || '发送失败');
      }
    } catch (error: any) {
      console.error('发送邮件失败:', error);
      alert(`❌ 发送失败：${error.message}\n请检查邮箱地址或稍后重试。`);
    } finally {
      setSendingEmail(false);
    }
  };

  if (!scoreResult) {
    return (
      <div className="min-h-screen bg-gradient-to-br from-teal-50 to-cyan-100 flex items-center justify-center">
        <div className="text-center">
          <div className="w-16 h-16 border-4 border-teal-200 border-t-teal-500 rounded-full animate-spin mx-auto mb-4"></div>
          <p className="text-lg text-gray-600">正在计算结果...</p>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-teal-50 to-cyan-100">
      {/* Header */}
      <header className="bg-white/80 backdrop-blur-sm border-b border-teal-100 sticky top-0 z-10">
        <div className="max-w-6xl mx-auto px-4 py-4">
          <div className="flex items-center justify-between">
            {/* Logo and Brand */}
            <div className="flex items-center space-x-3">
              <div className="w-10 h-10 rounded-xl overflow-hidden">
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
                  <Trophy className="w-6 h-6 text-white" />
                </div>
              </div>
              <div>
                <h1 className="text-2xl font-bold bg-gradient-to-r from-teal-600 to-cyan-600 bg-clip-text text-transparent">
                  CocoTest
                </h1>
                <p className="text-xs text-gray-500">测试结果</p>
              </div>
            </div>
            
            <button
              onClick={() => navigate('/')}
              className="px-4 py-2 text-teal-600 hover:bg-teal-50 rounded-lg transition-colors font-medium"
            >
              返回首页
            </button>
          </div>
        </div>
      </header>

      <main className="max-w-6xl mx-auto px-4 py-12">
        {/* Score Overview */}
        <div className="text-center mb-12">
          <div className="inline-flex items-center justify-center w-32 h-32 rounded-full bg-gradient-to-r from-teal-400 to-cyan-400 mb-6">
            <div className="text-center">
              <div className={`text-4xl font-bold ${getScoreColor(scoreResult.score)}`}>
                {scoreResult.score}
              </div>
              <div className="text-sm text-white font-medium">
                {testType === 'ielts' ? '分' : '%'}
              </div>
            </div>
          </div>
          
          <h2 className="text-3xl font-bold text-gray-900 mb-2">
            恭喜完成测试！
          </h2>
          <p className="text-lg text-gray-600">
            {getTestTypeName(testType)} {getModeName(mode)}
          </p>
        </div>

        {/* Main Results */}
        <div className="grid lg:grid-cols-3 gap-8 mb-12">
          {/* Score Card */}
          <div className="lg:col-span-2">
            <div className="bg-white rounded-2xl shadow-lg p-8">
              <div className="flex items-center mb-6">
                <div className={`w-12 h-12 rounded-xl bg-gradient-to-r ${getScoreBgColor(scoreResult.score)} flex items-center justify-center mr-4`}>
                  <Award className="w-6 h-6 text-white" />
                </div>
                <div>
                  <h3 className="text-2xl font-bold text-gray-900">您的等级</h3>
                  <p className="text-gray-600">{scoreResult.level}</p>
                </div>
              </div>
              
              <div className="mb-6">
                <div className="flex items-center justify-between mb-2">
                  <span className="text-gray-700">正确率</span>
                  <span className={`text-2xl font-bold ${getScoreColor(scoreResult.score)}`}>
                    {scoreResult.percentage}%
                  </span>
                </div>
                <div className="w-full bg-gray-200 rounded-full h-3">
                  <div 
                    className={`bg-gradient-to-r ${getScoreBgColor(scoreResult.score)} h-3 rounded-full transition-all duration-1000`}
                    style={{ width: `${scoreResult.percentage}%` }}
                  ></div>
                </div>
              </div>

              <div className="mb-6">
                <h4 className="font-semibold text-gray-900 mb-2">等级描述</h4>
                <p className="text-gray-600 leading-relaxed">{scoreResult.levelDescription}</p>
              </div>

              <div>
                <h4 className="font-semibold text-gray-900 mb-3">学习建议</h4>
                <ul className="space-y-2">
                  {scoreResult.recommendations.map((recommendation, index) => (
                    <li key={index} className="flex items-start">
                      <Star className="w-5 h-5 text-yellow-500 mr-2 mt-0.5 flex-shrink-0" />
                      <span className="text-gray-600">{recommendation}</span>
                    </li>
                  ))}
                </ul>
              </div>
            </div>
          </div>

          {/* Stats Card */}
          <div className="space-y-6">
            <div className="bg-white rounded-2xl shadow-lg p-6">
              <h4 className="font-semibold text-gray-900 mb-4">测试统计</h4>
              <div className="space-y-4">
                <div className="flex items-center justify-between">
                  <div className="flex items-center">
                    <Target className="w-5 h-5 text-green-500 mr-2" />
                    <span className="text-gray-600">正确题数</span>
                  </div>
                  <span className="font-semibold text-gray-900">
                    {Object.values(answers).filter((answer, index) => 
                      answer === questions[index]?.correct_answer
                    ).length}/{questions.length}
                  </span>
                </div>
                
                <div className="flex items-center justify-between">
                  <div className="flex items-center">
                    <Clock className="w-5 h-5 text-blue-500 mr-2" />
                    <span className="text-gray-600">用时</span>
                  </div>
                  <span className="font-semibold text-gray-900">
                    {formatTime(timeUsed)}
                  </span>
                </div>
                
                <div className="flex items-center justify-between">
                  <div className="flex items-center">
                    <BookOpen className="w-5 h-5 text-purple-500 mr-2" />
                    <span className="text-gray-600">测试类型</span>
                  </div>
                  <span className="font-semibold text-gray-900">
                    {getTestTypeName(testType)}
                  </span>
                </div>
              </div>
            </div>

            <div className="bg-white rounded-2xl shadow-lg p-6">
              <h4 className="font-semibold text-gray-900 mb-4">邮箱接收结果</h4>
              <p className="text-sm text-gray-600 mb-4">填写邮箱，我们将把测试结果发送给您</p>
              <div className="space-y-3">
                <div className="relative">
                  <Mail className="absolute left-3 top-1/2 transform -translate-y-1/2 w-5 h-5 text-gray-400" />
                  <input
                    type="email"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                    placeholder="请输入您的邮箱地址"
                    disabled={emailSent}
                    className="w-full pl-10 pr-4 py-3 border border-gray-300 rounded-xl focus:outline-none focus:ring-2 focus:ring-teal-500 focus:border-transparent disabled:bg-gray-100 disabled:cursor-not-allowed"
                  />
                </div>
                <button
                  onClick={handleSendEmail}
                  disabled={sendingEmail || emailSent || !email}
                  className="w-full flex items-center justify-center px-4 py-3 bg-gradient-to-r from-purple-500 to-purple-600 text-white rounded-xl hover:from-purple-600 hover:to-purple-700 transition-all disabled:opacity-50 disabled:cursor-not-allowed"
                >
                  {sendingEmail ? (
                    <>
                      <div className="w-5 h-5 border-2 border-white border-t-transparent rounded-full animate-spin mr-2"></div>
                      发送中...
                    </>
                  ) : emailSent ? (
                    <>
                      <Award className="w-5 h-5 mr-2" />
                      已发送
                    </>
                  ) : (
                    <>
                      <Send className="w-5 h-5 mr-2" />
                      发送结果
                    </>
                  )}
                </button>
              </div>
            </div>

            <div className="bg-white rounded-2xl shadow-lg p-6">
              <h4 className="font-semibold text-gray-900 mb-4">操作</h4>
              <div className="space-y-3">
                <button
                  onClick={() => navigate('/', { state: { retakeTest: true } })}
                  className="w-full flex items-center justify-center px-4 py-3 bg-gradient-to-r from-teal-500 to-cyan-500 text-white rounded-xl hover:from-teal-600 hover:to-cyan-600 transition-all"
                >
                  <RotateCcw className="w-5 h-5 mr-2" />
                  重新测试
                </button>
                
                <button
                  onClick={() => navigate('/')}
                  className="w-full flex items-center justify-center px-4 py-3 bg-gray-100 text-gray-700 rounded-xl hover:bg-gray-200 transition-colors"
                >
                  <Home className="w-5 h-5 mr-2" />
                  返回首页
                </button>
              </div>
            </div>
          </div>
        </div>

        {/* Data Visualization */}
        {categoryStats.length > 1 && (
          <div className="mb-12">
            <div className="flex items-center mb-6">
              <BarChart3 className="w-6 h-6 text-teal-600 mr-2" />
              <h3 className="text-2xl font-bold text-gray-900">成绩可视化分析</h3>
            </div>
            
            <div className="grid lg:grid-cols-2 gap-8">
              {/* 分类成绩条形图 */}
              <div className="bg-white rounded-2xl shadow-lg p-6">
                <div className="flex items-center mb-4">
                  <BarChart3 className="w-5 h-5 text-blue-600 mr-2" />
                  <h4 className="text-lg font-semibold text-gray-900">各部分正确率</h4>
                </div>
                <p className="text-sm text-gray-600 mb-6">分析各类题型的掌握情况，帮助您了解优势和薄弱环节</p>
                <ResponsiveContainer width="100%" height={300}>
                  <BarChart data={categoryStats}>
                    <CartesianGrid strokeDasharray="3 3" stroke="#f0f0f0" />
                    <XAxis 
                      dataKey="name" 
                      tick={{ fill: '#6b7280' }}
                      axisLine={{ stroke: '#e5e7eb' }}
                    />
                    <YAxis 
                      tick={{ fill: '#6b7280' }}
                      axisLine={{ stroke: '#e5e7eb' }}
                      label={{ value: '正确率(%)', angle: -90, position: 'insideLeft', fill: '#6b7280' }}
                    />
                    <Tooltip 
                      contentStyle={{ 
                        backgroundColor: '#fff', 
                        border: '1px solid #e5e7eb', 
                        borderRadius: '8px',
                        padding: '12px'
                      }}
                      formatter={(value: any, name: string) => {
                        if (name === '正确率') return [`${value}%`, name];
                        return [value, name];
                      }}
                    />
                    <Legend 
                      wrapperStyle={{ paddingTop: '20px' }}
                      iconType="circle"
                    />
                    <Bar 
                      dataKey="正确率" 
                      fill="#14b8a6" 
                      radius={[8, 8, 0, 0]}
                      animationDuration={1000}
                    />
                  </BarChart>
                </ResponsiveContainer>
                
                {/* 数据表格 */}
                <div className="mt-6 overflow-hidden rounded-lg border border-gray-200">
                  <table className="min-w-full divide-y divide-gray-200">
                    <thead className="bg-gray-50">
                      <tr>
                        <th className="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase">类型</th>
                        <th className="px-4 py-3 text-center text-xs font-medium text-gray-500 uppercase">正确</th>
                        <th className="px-4 py-3 text-center text-xs font-medium text-gray-500 uppercase">错误</th>
                        <th className="px-4 py-3 text-center text-xs font-medium text-gray-500 uppercase">正确率</th>
                      </tr>
                    </thead>
                    <tbody className="bg-white divide-y divide-gray-200">
                      {categoryStats.map((stat, index) => (
                        <tr key={index} className="hover:bg-gray-50">
                          <td className="px-4 py-3 text-sm font-medium text-gray-900">{stat.name}</td>
                          <td className="px-4 py-3 text-sm text-center text-green-600 font-medium">{stat.正确}</td>
                          <td className="px-4 py-3 text-sm text-center text-red-600 font-medium">{stat.错误}</td>
                          <td className="px-4 py-3 text-sm text-center">
                            <span className={`inline-flex items-center px-2 py-1 rounded-full text-xs font-medium ${
                              stat.正确率 >= 80 ? 'bg-green-100 text-green-800' :
                              stat.正确率 >= 60 ? 'bg-yellow-100 text-yellow-800' :
                              'bg-red-100 text-red-800'
                            }`}>
                              {stat.正确率}%
                            </span>
                          </td>
                        </tr>
                      ))}
                    </tbody>
                  </table>
                </div>
              </div>

              {/* 答题情况饼图 */}
              <div className="bg-white rounded-2xl shadow-lg p-6">
                <div className="flex items-center mb-4">
                  <PieChart className="w-5 h-5 text-purple-600 mr-2" />
                  <h4 className="text-lg font-semibold text-gray-900">答题情况分布</h4>
                </div>
                <p className="text-sm text-gray-600 mb-6">整体答题准确度的直观展示</p>
                <ResponsiveContainer width="100%" height={300}>
                  <RechartsPieChart>
                    <Pie
                      data={pieData}
                      cx="50%"
                      cy="50%"
                      labelLine={false}
                      label={({ name, percentage }) => `${name} ${percentage}%`}
                      outerRadius={100}
                      fill="#8884d8"
                      dataKey="value"
                      animationDuration={1000}
                    >
                      <Cell fill="#10b981" />
                      <Cell fill="#ef4444" />
                    </Pie>
                    <Tooltip 
                      contentStyle={{ 
                        backgroundColor: '#fff', 
                        border: '1px solid #e5e7eb', 
                        borderRadius: '8px',
                        padding: '12px'
                      }}
                      formatter={(value: any, name: string) => [value + ' 题', name]}
                    />
                    <Legend 
                      verticalAlign="bottom" 
                      height={36}
                      iconType="circle"
                    />
                  </RechartsPieChart>
                </ResponsiveContainer>
                
                {/* 统计卡片 */}
                <div className="mt-6 grid grid-cols-2 gap-4">
                  <div className="p-4 bg-green-50 rounded-lg border border-green-200">
                    <div className="flex items-center justify-between">
                      <span className="text-sm text-green-700">正确题数</span>
                      <Target className="w-4 h-4 text-green-600" />
                    </div>
                    <p className="text-2xl font-bold text-green-900 mt-2">{pieData[0]?.value || 0}</p>
                    <p className="text-xs text-green-600 mt-1">占比 {pieData[0]?.percentage || 0}%</p>
                  </div>
                  <div className="p-4 bg-red-50 rounded-lg border border-red-200">
                    <div className="flex items-center justify-between">
                      <span className="text-sm text-red-700">错误题数</span>
                      <Target className="w-4 h-4 text-red-600" />
                    </div>
                    <p className="text-2xl font-bold text-red-900 mt-2">{pieData[1]?.value || 0}</p>
                    <p className="text-xs text-red-600 mt-1">占比 {pieData[1]?.percentage || 0}%</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        )}

        {/* Detailed Results */}
        <div className="bg-white rounded-2xl shadow-lg p-8">
          <h3 className="text-2xl font-bold text-gray-900 mb-6">详细答题记录</h3>
          <div className="space-y-6">
            {detailedResults.map((result, index) => (
              <div key={index} className="border border-gray-200 rounded-xl p-6">
                <div className="flex items-start justify-between mb-4">
                  <div className="flex items-center">
                    <span className="inline-flex items-center justify-center w-8 h-8 bg-gray-100 rounded-full text-sm font-medium text-gray-600 mr-3">
                      {result.questionNumber}
                    </span>
                    <span className={`inline-flex items-center px-3 py-1 rounded-full text-sm font-medium ${
                      result.isCorrect 
                        ? 'bg-green-100 text-green-800' 
                        : 'bg-red-100 text-red-800'
                    }`}>
                      {result.isCorrect ? '正确' : '错误'}
                    </span>
                    <span className="ml-2 inline-flex items-center px-3 py-1 rounded-full text-sm font-medium bg-gray-100 text-gray-800">
                      {result.category}
                    </span>
                  </div>
                </div>
                
                <p className="text-gray-900 mb-4">{result.question}</p>
                
                {/* 词汇测试特殊显示 */}
                {testType === 'vocabulary' && result.word && (
                  <div className="mb-4 p-3 bg-orange-50 rounded-lg border border-orange-200">
                    <div className="flex items-center justify-between">
                      <span className="text-lg font-semibold text-orange-800">{result.word}</span>
                      <span className="text-sm text-orange-600 bg-orange-100 px-2 py-1 rounded">
                        {result.category}
                      </span>
                    </div>
                    {result.example_sentence && (
                      <p className="text-orange-700 text-sm mt-2 italic">
                        例句：{result.example_sentence}
                      </p>
                    )}
                  </div>
                )}
                
                <div className="grid md:grid-cols-2 gap-4">
                  <div>
                    <span className="text-sm text-gray-600">您的答案：</span>
                    <span className={`ml-2 font-medium ${result.isCorrect ? 'text-green-600' : 'text-red-600'}`}>
                      {result.userAnswer || '未答'}
                    </span>
                  </div>
                  <div>
                    <span className="text-sm text-gray-600">正确答案：</span>
                    <span className="ml-2 font-medium text-green-600">
                      {result.correctAnswer}
                    </span>
                  </div>
                </div>
                
                {result.explanation && (
                  <div className="mt-4 p-4 bg-blue-50 rounded-lg">
                    <h5 className="font-medium text-blue-900 mb-2">解析：</h5>
                    <p className="text-blue-800 text-sm">{result.explanation}</p>
                  </div>
                )}
              </div>
            ))}
          </div>
        </div>
      </main>
    </div>
  );
};

export default ResultPage;