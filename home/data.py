"""网站静态数据模型（Django 版）"""

# ============ 个人信息 ============
PERSONAL = {
    "name": "张以勒",
    "name_en": "Yile Zhang",
    "title": "Python 开发 / AI 应用开发",
    "subtitle": "计算机科学与技术背景",
    "description": "专注于 Python 开发、人工智能应用和数据分析方向。",
    "hero_tagline": "Building software with Python, AI and cloud technologies",
    "email": "zygeli05@gmail.com",
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
        "title": "Django 个人博客系统",
        "tags": ["Python", "Django", "MySQL", "Bootstrap", "Linux"],
        "summary": "基于 Django 5.2 的全功能博客系统，13 个数据模型覆盖内容管理、社交互动与辅助功能三层架构。采用 MySQL + Bootstrap 5 + CKEditor，支持暗色主题、AJAX 无刷新交互、nginx 子路径部署。",
        "features": [
            "内容管理 — 列表分页、特色推荐、分类浏览、标签云、全文搜索、年月归档",
            "文章展示 — 代码高亮（Prism.js）、自动目录（TOC）、阅读进度追踪",
            "社交互动 — 多级评论（嵌套回复）、点赞、收藏、用户关注、实时通知",
            "后台管理 — 自定义 Django Admin，文章/用户/系统设置管理，list_select_related 翻页优化",
            "用户体验 — 暗色主题默认启用并持久化、响应式设计、AJAX 无刷新交互",
            "性能优化 — select_related / prefetch_related 消除 N+1 查询，TruncMonth 数据库端分组，高频字段建索引",
        ],
        "architecture": {
            "后端框架": "Django 5.2.3",
            "数据库": "MySQL 8.0（utf8mb4）",
            "前端": "Bootstrap 5 + Font Awesome + Prism.js",
            "富文本编辑": "CKEditor 6.7",
            "标签系统": "django-taggit 6.1",
            "部署方案": "gunicorn + nginx（子路径转发）",
        },
        "my_work": [
            "数据建模 — 设计 13 个数据模型，覆盖 Post/Category/Tag 核心内容、Comment/PostLike/PostFavorite/UserFollow 社交互动、Notification/ReadingProgress/VisitorLog 辅助功能三层",
            "视图架构 — CBV + FBV 混合：ListView/DetailView 处理内容展示，15 个函数视图处理 AJAX（点赞/收藏/关注/通知已读），自定义 context processor 全局注入导航和博主信息",
            "性能优化 — select_related / prefetch_related 消除外键 N+1，归档页 TruncMonth 数据库端分组替代 Python 循环，后台 list_select_related + show_full_result_count 大数据翻页优化，published_at / status / is_featured 建索引",
            "后台定制 — 覆盖 Django Admin 模板（login.html / base_site.html / change_form.html），统一字体配色与表单控件样式，User post_save 信号合并消除冗余",
            "前端体验 — 暗色模式 localStorage 持久化，Prism.js 代码高亮 + 自动 TOC 目录，响应式 Bootstrap 5 布局适配移动端",
            "工程规范 — 清理重复/未使用导入，import re 提升至模块顶层，精简依赖至 7 个包，标准 collectstatic + nginx 子路径部署",
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
