# 张以勒 | 个人技术网站

基于 Django 构建的个人技术作品集，面向技术招聘者，展示项目经历、竞赛成果和技术能力。

**线上地址：** [zygeli.cn](https://zygeli.cn)

## 技术栈

- **后端：** Django 5.2 + Python 3.12
- **前端：** 原生 HTML/CSS/JS，JetBrains Mono + Sora 字体
- **部署：** Linux + Nginx + Gunicorn

## 本地运行

```bash
# 克隆仓库
git clone https://github.com/ZYlow1/Resume-website.git
cd Resume-website

# 创建虚拟环境并安装依赖
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# 启动开发服务器
python manage.py runserver
```

访问 http://127.0.0.1:8000

## 页面结构

| 页面 | 路径 | 内容 |
|------|------|------|
| 首页 | `/` | 个人介绍、技术标签、精选项目 |
| 关于 | `/about/` | 个人背景、教育经历、成长时间轴 |
| 技能 | `/skills/` | 技术栈与熟练度 |
| 项目 | `/projects/` | 项目卡片列表 + 详情页 |
| 竞赛 | `/competitions/` | 竞赛奖项与证书 |
| 简历 | `/resume/` | 在线简历 + PDF 下载 |
| 联系 | `/contact/` | 联系方式与社交链接 |

## 数据配置

所有个人信息、项目、竞赛数据集中在 `home/data.py` 中管理，修改后自动反映到所有页面。

## 许可证

GPL
