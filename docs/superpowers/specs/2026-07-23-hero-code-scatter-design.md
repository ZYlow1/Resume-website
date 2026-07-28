# Hero 区代码装饰拆分散布设计

## 概述

将首页 Hero 区两侧的代码块（`hero-code-left` 和 `hero-code-right`）拆散为独立行元素，融入全局 `.code-lines` 背景系统，使代码装饰自然散布在页面各处。

## 改动范围

### 1. 新增代码行（base.html）

将 9 行代码拆为独立的 `<span class="code-line">`，加入到 `.code-lines` 容器中：

| # | 代码内容 | 位置 | 不透明度 |
|---|---------|------|---------|
| 1 | `import { developer } from 'portfolio'` | top:8%, right:15% | 0.10 |
| 2 | `const skills = ['Python', 'Django', 'AI']` | top:16%, left:10% | 0.07 |
| 3 | `function buildProject() {` | top:28%, right:6% | 0.12 |
| 4 | `return new Website()` | top:38%, left:20% | 0.09 |
| 5 | `}` | top:48%, right:18% | 0.06 |
| 6 | `# server.py` | top:58%, left:5% | 0.11 |
| 7 | `@app.route('/api')` | top:70%, right:8% | 0.08 |
| 8 | `def hello_world():` | top:80%, left:12% | 0.10 |
| 9 | `return jsonify(data)` | top:92%, right:5% | 0.07 |

位置分布在页面不同高度，左侧/右侧交替排列，形成自然散布感。

### 2. 删除 hero-code（home.html）

移除 `home.html` 中的：
- `<div class="hero-code hero-code-left">...</div>` 整个块
- `<div class="hero-code hero-code-right">...</div>` 整个块

### 3. 清理 CSS（style.css）

删除 `.hero-code`、`.hero-code-left`、`.hero-code-right` 样式块（从第 1572 行开始）。

## 现有系统不变

- `.code-lines` / `.code-line` CSS 规则不变
- `codePulse` 动画不变
- 移动端隐藏逻辑不变
- 其他页面不受影响
