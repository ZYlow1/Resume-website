"""网站静态数据模型（Django 版）"""

# ============ 个人信息 ============
PERSONAL = {
    "name": "张以勒",
    "name_en": "Yile Zhang",
    "title": "Python 开发 / AI 应用开发",
    "subtitle": "计算机科学与技术背景",
    "description": "专注于 Python 开发、人工智能应用和数据分析方向。",
    "hero_tagline": "Building software with Python, AI and cloud technologies",
    "email": "18957760819@163.com",
    "github": "https://github.com/ZYlow1",
    "blog_url": "https://blog.zhangyile.com",
    "status": "Looking for opportunities",
}

# ============ 关于我 ============
ABOUT = {
    "intro": (
        "我是一名计算机科学与技术专业在校生。"
        "大学期间系统学习计算机基础知识，"
        "并通过项目实践和竞赛训练提升软件开发能力。"
    ),
    "focus_areas": [
        "Python Web开发",
        "人工智能应用",
        "数据分析",
        "云计算技术",
    ],
    "extra": "拥有独立完成Web项目开发、服务器部署以及AI相关项目实践经验。",
}

# ============ 教育经历 ============
EDUCATION = [
    {
        "major": "云计算技术应用",
        "level": "专科阶段",
        "period": "2023 - 2026",
    },
    {
        "major": "计算机科学与技术",
        "level": "本科阶段",
        "period": "2026 - 至今",
    },
]

# ============ 成长路线（时间轴） ============
TIMELINE = [
    {"year": "2022", "event": "开始学习Python"},
    {"year": "2023", "event": "参与程序设计比赛"},
    {"year": "2024", "event": "完成Django博客系统"},
    {"year": "2025", "event": "参与AI、大数据相关竞赛"},
    {"year": "2026", "event": "寻找实习机会"},
]

# ============ 技能数据 ============
SKILL_CATEGORIES = [
    {
        "name": "Programming",
        "skills": [
            {"name": "Python", "level": 4},
            {"name": "Java", "level": 2},
            {"name": "SQL", "level": 4},
        ],
    },
    {
        "name": "Backend",
        "skills": [
            {"name": "Django", "level": 4},
            {"name": "REST API", "level": 3},
            {"name": "MySQL", "level": 4},
        ],
    },
    {
        "name": "System",
        "skills": [
            {"name": "Linux", "level": 4},
            {"name": "Docker", "level": 3},
            {"name": "Git", "level": 4},
        ],
    },
    {
        "name": "Data & AI",
        "skills": [
            {"name": "Hadoop", "level": 3},
            {"name": "Data Analysis", "level": 3},
            {"name": "Machine Learning", "level": 2},
        ],
    },
]

# ============ 技术标签（首页云） ============
TECH_TAGS = [
    "Python", "Django", "MySQL", "Linux",
    "Docker", "Hadoop", "AI", "Data Analysis",
]

# ============ 项目数据 ============
PROJECTS = [
    {
        "id": 1,
        "title": "Django个人博客平台",
        "tags": ["Python", "Django", "MySQL", "Bootstrap", "Linux"],
        "summary": "一个基于 Django 5.2.3 框架开发的现代化个人博客系统。采用 MySQL 数据库和 Bootstrap 5 前端技术，实现了完整的博客功能与企业级特性，包括文章发布管理、用户互动社交、分类标签系统、响应式界面设计等，具备良好的安全性、性能和用户体验。",
        "features": [
            "文章管理 — 富文本编辑、分类标签、草稿发布",
            "用户系统 — 注册登录、个人资料管理",
            "社交功能 — 多级评论、点赞、收藏、用户关注",
            "内容组织 — 分类管理、标签云、文章归档",
            "智能搜索 — 关键词搜索、按分类/标签筛选",
            "交互体验 — 阅读进度跟踪、实时通知系统",
            "管理后台 — 完整的 Django Admin 管理界面",
            "主题切换 — 支持明暗主题切换",
        ],
        "architecture": {
            "后端框架": "Django 5.2.3",
            "数据库": "MySQL 8.0",
            "前端技术": "Bootstrap 5 + Font Awesome",
            "富文本编辑器": "CKEditor 6.7.3",
        },
        "my_work": [
            "数据库设计 — 设计用户、文章、分类、评论、通知等核心数据模型，使用 select_related 和 prefetch_related 优化查询性能",
            "后端开发 — 使用 Django Class-Based Views 实现业务逻辑，包含权限控制、缓存优化、AJAX 异步接口",
            "前端开发 — 基于 Bootstrap 5 实现响应式布局，集成 Prism.js 代码高亮，CKEditor 富文本编辑",
            "安全防护 — 实现 CSRF 保护、SQL 注入防护、XSS 防护、文件上传安全验证",
            "系统部署 — 配置 Linux 服务器 + Nginx，使用 Git 进行版本管理",
        ],
        "github_url": "https://github.com/ZYlow1/django-blog",
        "demo_url": "https://zygeli.cn/blog/",
        "category": "Web Project",
    },
    {
        "id": 2,
        "title": "AI驱动云资源自动扩展系统",
        "tags": ["Python", "PyTorch", "GRU", "Dask", "CuDF"],
        "summary": "基于GRU（门控循环单元）的多任务时间序列预测系统，用于预测服务器的CPU使用率、内存使用率和响应时间（RT）。系统包含完整的数据处理、模型训练和可视化流程，能够处理大规模集群数据并提供准确的性能预测。",
        "features": [
            "大规模数据处理 — 支持CSV分块读取、Parquet高效存储，Dask+CuDF GPU加速并行处理",
            "数据合并对齐 — 多数据源（RT/RES/NODE）基于时间戳的合并与对齐",
            "多任务预测 — 同时预测CPU使用率、内存使用率和响应时间（t+1, t+2）",
            "特征工程 — 正弦/余弦时间特征编码，log1p变换处理长尾分布",
            "断点续训 — 支持训练中断后从检查点恢复",
            "早停机制 — patience=5 防止过拟合，ReduceLROnPlateau 学习率调度",
            "多指标评估 — MAE、RMSE、MAPE、R² 全方位评估模型性能",
            "可视化输出 — 指标柱状图、真实vs预测散点图、时序预测样例图",
        ],
        "architecture": {
            "数据处理": "Pandas + Dask + CuDF",
            "深度学习": "PyTorch + GRU",
            "数据存储": "Parquet 列式存储",
            "可视化": "Matplotlib + Seaborn",
        },
        "my_work": [
            "数据处理 — 设计CSV→Parquet增量转换流程，分块读取避免内存溢出，实现流式合并",
            "数据融合 — 基于 msinstanceid 和 timestamp 的多源数据时间对齐合并，支持GPU加速",
            "模型构建 — 搭建多任务GRU网络（7维输入→128隐藏层→3任务头），使用HuberLoss + Adam优化",
            "特征工程 — 提取周期性时间特征（sin_hour/cos_hour），对响应时间进行log1p变换",
            "评估可视化 — 实现多指标评估体系，生成高分辨率图表分析模型性能",
        ],
        "github_url": "https://github.com/ZYlow1/AI-powered-cloud-resource-auto-scaling-system",
        "demo_url": None,
        "category": "AI Project",
    },
]

# ============ 竞赛荣誉 ============
COMPETITIONS = [
    {
        "title": "全国大学生数学建模竞赛",
        "subtitle": "高职高专",
        "award": "省赛二等奖",
        "direction": None,
        "skills_displayed": ["数学建模", "数据分析", "问题解决"],
        "cert": "certificates/shuxue_jianmo.png",
        "is_pdf": False,
    },
    {
        "title": "中国高校计算机大赛",
        "subtitle": "团队程序设计天梯赛",
        "award": "国赛铜奖",
        "direction": None,
        "skills_displayed": ["算法基础", "程序设计"],
        "cert": "certificates/tiantisai.png",
        "is_pdf": False,
    },
    {
        "title": "码蹄杯全国大学生程序设计大赛",
        "subtitle": "职业院校赛道",
        "award": "国赛铜奖",
        "direction": None,
        "skills_displayed": ["算法设计", "程序设计", "问题求解"],
        "cert": "certificates/matibei.png",
        "is_pdf": False,
    },
    {
        "title": "中国移动杯·浙江省大学生人工智能竞赛",
        "subtitle": "网易专项赛",
        "award": "省赛二等奖",
        "direction": None,
        "skills_displayed": ["模型设计", "数据处理", "算法实践"],
        "cert": "certificates/zhongguo_yidong.png",
        "is_pdf": False,
    },
    {
        "title": "蚂蚁·数字马力杯",
        "subtitle": "大学生服务外包创新应用大赛",
        "award": "省赛二等奖",
        "direction": None,
        "skills_displayed": ["软件开发", "项目设计", "团队协作"],
        "cert": "certificates/mayi_shuzimali.png",
        "is_pdf": False,
    },
    {
        "title": "浙江省职业院校技能大赛",
        "subtitle": "网络系统管理赛项",
        "award": "省赛银奖",
        "direction": None,
        "skills_displayed": ["网络管理", "系统运维", "故障排查"],
        "cert": "certificates/wangluo_guanli.jpg",
        "is_pdf": False,
    },
    {
        "title": "浙江省职业院校技能大赛",
        "subtitle": "商务数据分析赛项",
        "award": "省赛铜奖",
        "direction": None,
        "skills_displayed": ["数据分析", "数据可视化", "商业洞察"],
        "cert": "certificates/shangwu_shuju.jpg",
        "is_pdf": False,
    },
]


# ============ 联系信息 ============
CONTACT = {
    "email": PERSONAL["email"],
    "github": PERSONAL["github"],
    "blog": PERSONAL["blog_url"],
}
