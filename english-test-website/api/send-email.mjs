// Vercel Serverless Function (ES Module)
import { Resend } from 'resend';

export default async (req, res) => {
  // 设置 CORS
  res.setHeader('Access-Control-Allow-Credentials', 'true');
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET,OPTIONS,PATCH,DELETE,POST,PUT');
  res.setHeader(
    'Access-Control-Allow-Headers',
    'X-CSRF-Token, X-Requested-With, Accept, Accept-Version, Content-Length, Content-MD5, Content-Type, Date, X-Api-Version'
  );

  // 处理 OPTIONS 请求
  if (req.method === 'OPTIONS') {
    return res.status(200).end();
  }

  // 只允许 POST 请求
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  try {
    // 从环境变量获取 API Key
    const apiKey = process.env.RESEND_API_KEY;
    
    if (!apiKey) {
      console.error('RESEND_API_KEY 未设置');
      return res.status(500).json({ error: '服务器配置错误：API密钥未设置' });
    }

    const resend = new Resend(apiKey);
    const { email, testType, score, totalQuestions, correctAnswers } = req.body;

    // 验证必填字段
    if (!email || !testType) {
      return res.status(400).json({ error: '缺少必填字段' });
    }

    // 发送邮件
    const { data, error } = await resend.emails.send({
      from: 'CocoTest <onboarding@resend.dev>',
      to: [email],
      subject: `CocoTest 测试结果 - ${testType}`,
      html: `
        <!DOCTYPE html>
        <html>
        <head>
          <meta charset="utf-8">
          <style>
            body { font-family: Arial, sans-serif; line-height: 1.6; color: #333; }
            .container { max-width: 600px; margin: 0 auto; padding: 20px; }
            .header { background: linear-gradient(135deg, #10b981 0%, #14b8a6 100%); color: white; padding: 30px; text-align: center; border-radius: 10px 10px 0 0; }
            .content { background: #f9fafb; padding: 30px; border-radius: 0 0 10px 10px; }
            .score-card { background: white; padding: 20px; border-radius: 8px; margin: 20px 0; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
            .score { font-size: 48px; font-weight: bold; color: #10b981; text-align: center; margin: 20px 0; }
            .stats { display: flex; justify-content: space-around; margin: 20px 0; }
            .stat { text-align: center; }
            .stat-value { font-size: 24px; font-weight: bold; color: #14b8a6; }
            .stat-label { color: #6b7280; font-size: 14px; }
            .footer { text-align: center; color: #9ca3af; font-size: 12px; margin-top: 30px; }
          </style>
        </head>
        <body>
          <div class="container">
            <div class="header">
              <h1>🥥 CocoTest 测试结果</h1>
              <p>专业英语水平测试平台</p>
            </div>
            <div class="content">
              <h2>您好！</h2>
              <p>恭喜您完成 <strong>${testType}</strong> 测试！以下是您的测试结果：</p>
              
              <div class="score-card">
                <div class="score">${score}分</div>
                <div class="stats">
                  <div class="stat">
                    <div class="stat-value">${correctAnswers}</div>
                    <div class="stat-label">答对题数</div>
                  </div>
                  <div class="stat">
                    <div class="stat-value">${totalQuestions}</div>
                    <div class="stat-label">总题数</div>
                  </div>
                  <div class="stat">
                    <div class="stat-value">${((correctAnswers / totalQuestions) * 100).toFixed(1)}%</div>
                    <div class="stat-label">正确率</div>
                  </div>
                </div>
              </div>

              <p><strong>测试类型：</strong>${testType}</p>
              <p><strong>测试时间：</strong>${new Date().toLocaleString('zh-CN')}</p>

              <p style="margin-top: 30px; padding: 15px; background: #ecfdf5; border-left: 4px solid #10b981; border-radius: 4px;">
                💡 <strong>温馨提示：</strong>请继续保持学习，不断提升英语水平！
              </p>
            </div>
            <div class="footer">
              <p>© 2025 CocoTest - 专业英语水平测试平台</p>
              <p>本邮件由系统自动发送，请勿直接回复</p>
            </div>
          </div>
        </body>
        </html>
      `,
    });

    if (error) {
      console.error('Resend API 错误:', error);
      return res.status(400).json({ error: error.message || '发送邮件失败' });
    }

    return res.status(200).json({ success: true, data });
  } catch (error) {
    console.error('发送邮件异常:', error);
    return res.status(500).json({ 
      error: error.message || '服务器内部错误',
      details: process.env.NODE_ENV === 'development' ? error.stack : undefined
    });
  }
};
