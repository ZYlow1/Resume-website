---
name: Yile Zhang | Python Developer Portfolio
description: A light-themed editorial-style portfolio with electric violet accent
colors:
  primary: "#7C3AED"
  primary-hover: "#6D28D9"
  neutral-bg: "#f8f6f3"
  neutral-surface: "#f0ece6"
  neutral-card: "#ffffff"
  neutral-text: "#1a1a2e"
  neutral-text-secondary: "#5b5560"
  neutral-text-muted: "#6b6570"
  neutral-border: "#e5e0d8"
  success: "#059669"
  warning: "#D97706"
  danger: "#DC2626"
  terminal-bg: "#ffffff"
  terminal-body: "#faf9f7"
  terminal-header: "#f3f1ee"
  terminal-border: "#e5e0d8"
typography:
  display:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'JetBrains Mono', 'Fira Code', monospace, sans-serif"
    fontSize: "clamp(1.8rem, 4vw, 2.5rem)"
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: "-1px"
  title:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'JetBrains Mono', 'Fira Code', monospace, sans-serif"
    fontSize: "1.1rem"
    fontWeight: 600
    lineHeight: 1.3
  body:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'JetBrains Mono', 'Fira Code', monospace, sans-serif"
    fontSize: "1rem"
    fontWeight: 400
    lineHeight: 1.6
  label:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'JetBrains Mono', 'Fira Code', monospace, sans-serif"
    fontSize: "0.85rem"
    fontWeight: 500
rounded:
  sm: "8px"
  md: "12px"
spacing:
  xs: "6px"
  sm: "8px"
  md: "12px"
  lg: "16px"
  xl: "24px"
  xxl: "32px"
components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "#0f172a"
    rounded: "{rounded.sm}"
    padding: "12px 28px"
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
  button-outline:
    backgroundColor: "transparent"
    textColor: "{colors.neutral-text}"
    rounded: "{rounded.sm}"
    padding: "12px 28px"
  card-default:
    backgroundColor: "{colors.neutral-surface}"
    rounded: "{rounded.md}"
    padding: "24px"
  nav-link:
    textColor: "{colors.neutral-text-secondary}"
    rounded: "{rounded.sm}"
    padding: "8px 14px"
---

# Design System: Yile Zhang | Python Developer Portfolio

## 1. Overview

**Creative North Star: "Code Narrative"**

代码叙事。浅色底色 + 电光紫强调——干净、大胆、独特。暗色终端换成了浅色代码窗口，保持开发者身份的同时呈现出更具编辑感的气质。每一个页面都是一次 `cat` 或 `ls` 操作，把项目、竞赛、技能以最直接的方式呈现给读者。

**Visual Atmosphere:** 干净 · 大胆 · 独特。温暖的米白底色（`#f8f6f3`）建立亲和舒适的阅读环境，Electric Violet 电光紫（`#7C3AED`）注入能量和个性。这是传统技术作品集不会选择的配色——而这正是重点。

**Key Characteristics:**
- 浅色底色 + 紫罗兰强调色的胆大配色
- 终端窗口保留为标志性组件，适配浅色模式
- Sora 标题字体 + 电光紫强调，表达性排版
- 纯白卡片在暖底色上形成清晰层次
- 暖灰边框代替深色边框，保持柔和边界

**Anti-references:** 不追求炫目视觉效果，不采用 SaaS 落地页模板（大数字指标、渐变文字、玻璃拟态），不把竞赛荣誉塞进简历角落。网站是技术档案，不是设计作品展。

## 2. Colors

配色基于暖白底色 + 单一 Electric Violet 强调色——大胆、独特、有记忆点。

### Primary
- **Electric Violet** (`#7C3AED`): 唯一的强调色。用于链接、按钮、活动导航项、时间轴节点、accent 边框和标签。出镜率控制在 ≤10% 的页面面积；其稀有性就是力量。
- **Deep Violet** (`#6D28D9`): 强调色的悬浮态。用于按钮和链接的 hover 效果。

### Neutral
- **Warm Paper** (`#f8f6f3`): 页面主背景色。全站通用。
- **Warm Surface** (`#f0ece6`): 卡片、导航悬浮态、二级背景。
- **Pure White** (`#ffffff`): 卡片背景、终端窗口背景。
- **Ink Black** (`#1a1a2e`): 主文字色。标题和正文首选。
- **Warm Gray** (`#5b5560`): 次级文字。段落正文、导航链接默认态、技能标签。
- **Muted Gray** (`#6b6570`): 弱化文字。footer、日期、元数据、提示文本。
- **Warm Border** (`#e5e0d8`): 分割线和卡片边框。

### Semantic
- **Emerald** (`#059669`): 成功状态、终端提示符 `$`。
- **Amber** (`#D97706`): 警告状态、技能星级评分。
- **Red** (`#DC2626`): 错误状态。

### Terminal (Light Mode)
- **Terminal White** (`#ffffff`): 终端窗口背景。
- **Terminal Body** (`#faf9f7`): 终端代码区域背景。
- **Terminal Header** (`#f3f1ee`): 终端窗口标题栏背景。
- **Terminal Border** (`#e5e0d8`): 终端边框。

### Named Rules
**The One-Voice Rule.** Electric Violet 是唯一的强调色。任何页面不应出现第二种强调色。颜色层级完全通过同色系的明度和饱和度变化来实现。

**The Terminal-Honesty Rule.** 终端窗口的圆点（红/黄/绿）必须保持与真实终端一致，不做创意化改造。它们是身份锚点，不是装饰元素。浅色终端背景是适配整体配色的有意选择。

## 3. Typography

**Primary Font Stack:** `-apple-system, BlinkMacSystemFont, 'Segoe UI', 'JetBrains Mono', 'Fira Code', monospace, sans-serif`

一个混合栈——系统 sans-serif 确保跨平台可读性，monospace 字体注入开发者身份感。整个网站使用同一套字体栈，不配对第二种字体。体重大小和间距创造层次。

**Mono Font Stack (终端内容):** `'JetBrains Mono', 'Fira Code', monospace`

终端窗口内的全部内容使用纯 monospace，与系统界面形成明确区隔。

### Hierarchy

- **Display** (700, `clamp(1.8rem, 4vw, 2.5rem)`, 1.2, -1px letter-spacing): Hero 标题 "你好，我是张以勒" 等页面主标题。使用 `text-wrap: balance`。
- **Title** (600, 1.1rem, 1.3): 项目卡片标题、竞赛标题、页面次级标题。
- **Body** (400, 1rem, 1.6): 正文段落、页面说明文字。行宽限制在 65–75ch。
- **Label** (500, 0.85rem): 导航链接、标签、按钮文字、元数据。
- **Mono** (400, 0.95rem, 1.5): 终端窗口内容（命令、输出、提示符）。

### Named Rules
**The One-Stack Rule.** 不分显示字体和正文字体。整个系统使用同一套字体栈，层次完全通过权重（700/600/500/400）、字号和间距实现。不引入单独的 display 字体或衬线字体。

## 4. Elevation

平面优先，阴影为辅助。浅色底色上的层次通过背景色明度（Warm Paper → Pure White）和 1px 暖灰边框实现。阴影在浅色主题中更柔和，只为需要强调的元素提供轻微深度。

### Shadow Vocabulary
- **Terminal Soft** (`0 8px 32px rgba(0, 0, 0, 0.06), 0 1px 3px rgba(0, 0, 0, 0.04)`): 仅用于终端窗口，赋予它柔和的存在感。
- **Hover Lift** (`0 12px 40px rgba(0, 0, 0, 0.08)`): 出现在卡片 hover 态，配合 `translateY(-4px)` 提供触感反馈。

### Named Rules
**The Flat-by-Default Rule.** 表面静止时无阴影。边框和背景层级是默认的分隔手段。阴影只在交互态出现，表示"这个元素正在被注视"。

## 5. Components

### Terminal Window
整个网站的签名组件，出现在 Hero 区域。

- **Shape:** 圆角矩形 (12px)，带 1px 暖灰边框
- **Structure:** 三部分——标题栏（含红/黄/绿圆点 + 标题）、命令输出区域
- **Title Bar:** Terminal Header 背景 (`#f3f1ee`)，10px padding，圆点间距 8px
- **Body:** Terminal Body 背景 (`#faf9f7`)，24px padding，纯 monospace 排版
- **Lines:** 提示符 `$` (Emerald) + 命令（Ink Black）+ 输出（Electric Violet），间距 12px
- **Cursor:** 8px × 16px Electric Violet 矩形，`blink` 动画 1s step-end 无限循环

### Buttons
- **Shape:** 圆角 (8px)，12px 上下 + 28px 左右 padding，600 weight
- **Primary:** Electric Violet 背景 + 白色文字。Hover: Deep Violet + `translateY(-2px)` + 紫色阴影
- **Outline:** 透明背景 + Ink Black 文字 + 1px Warm Border。Hover: 边框变 Electric Violet，文字变 Electric Violet
- **Transition:** 全部 0.25s cubic-bezier(0.16, 1, 0.3, 1)

### Cards
- **Corner Style:** 圆角 (12px)
- **Background:** Slate Surface (`#1e293b`)
- **Border:** 1px Slate Border (`#334155`)
- **Shadow Strategy:** 无默认阴影。Hover 时出现 Hover Lift (`0 4px 20px rgba(56, 189, 248, 0.1)`) + `translateY(-2px)`
- **Internal Padding:** 24px
- **Variants:** 项目卡片、竞赛卡片、教育卡片 —— 统一造型，通过内部元素区分类型

### Tags / Chips
- **Shape:** 圆角 (20px)，6px 上下 + 16px 左右 padding
- **Default:** Slate Surface 背景 + 1px Slate Border + Muted Slate 文字
- **Hover:** 边框变 Sky Blue，文字变 Sky Blue
- **Size:** 0.85rem, 500 weight
- **Project Tags Variant:** 更小 (0.75rem, 3px 10px padding)

### Navigation
- **Style:** 固定顶部，64px 高度，深层背景 `rgba(15, 23, 42, 0.95)` + `backdrop-filter: blur(12px)`，底部 1px Slate Border
- **Links:** 8px 14px padding，圆角 8px，Muted Slate 文字
- **Default → Hover:** 文字变白 + Slate Surface 背景
- **Active:** Sky Blue 文字 + `rgba(56, 189, 248, 0.1)` 背景
- **Mobile:** 汉堡菜单按钮，点击展开垂直菜单

### Inputs / Fields
- **Contact Cards:** Slate Surface 背景 + 1px Slate Border + 圆角 8px + 16px 32px padding
- **Hover:** 边框变 Sky Blue + `translateY(-1px)`

### Timeline
- **Structure:** 左侧垂直线 (2px, Slate Border) + 时间轴节点
- **Node:** 12px Sky Blue 圆点，3px Deep Navy border 包裹
- **Year:** Sky Blue, 1rem, 700 weight
- **Event:** Muted Slate, 0.95rem
- **Spacing:** 每个节点间距 32px

### Competition Cards
包含一个特色元素:
- **Award Badge:** 内嵌标签，4px 12px padding，`rgba(234, 179, 8, 0.15)` 背景 + Caution Amber 文字，圆角 20px
- **Skills Row:** 小号标签行，紧跟在卡片底部

### Certificate Modal
- **Backdrop:** 全屏固定定位，`rgba(0, 0, 0, 0.9)`，z-index 9999
- **Content:** 最大 90vw/90vh，维持比例，圆角 4px
- **Close:** 右上角，白色 2.5rem 字体，hover 变 Sky Blue

## 6. Do's and Don'ts

### Do:
- **Do** 用 Electric Violet 单一强调色系统，保持 ≤10% 页面色块占比
- **Do** 用背景色层级 (Warm Paper → Warm Surface → Pure White) 来区分内容区域
- **Do** 保证正文对比度 ≥4.5:1，大号文字 ≥3:1
- **Do** 在 hover 时给交互元素提供明确的触感反馈（上浮 + 阴影 + 边框变色）
- **Do** 在终端窗口中使用纯 monospace 字体，与系统 UI 区隔
- **Do** 让项目和竞赛卡片承载最大的视觉重量——它们是招聘者的核心关注点
- **Do** 使用 `text-wrap: balance` 在 h1–h3 上，`text-wrap: pretty` 在长段落上

### Don't:
- **Don't** 使用第二种强调色。整个系统只有 Electric Violet。
- **Don't** 回到深色主题。这套配色是浅色+紫色的有意选择。
- **Don't** 使用大范围投影作为默认分隔手段。平面 + 边框优先。
- **Don't** 使用渐变文字（`background-clip: text` + gradient）。
- **Don't** 使用玻璃拟态（glassmorphism）作为默认样式。
- **Don't** 使用 SaaS 指标块布局（大数字 + 小标签 + 装饰性强调）。
- **Don't** 使用编号章节标记（01 / 02 / 03）作为默认页面结构。
- **Don't** 使用全大写 + 宽间距的"eyebrow"标题（"ABOUT" "PROCESS"）。
- **Don't** 使用 border-left 或 border-right 大于 1px 作为彩色装饰条。
- **Don't** 把竞赛荣誉放在简历角落——它们有独立的卡片展示。
- **Don't** 让文字溢出容器——测试每个断点的长标题，必要时减小 clamp 上限。
