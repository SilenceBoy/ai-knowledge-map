# Bin哥的知识地图

把读过、想过、用过的东西整理成可以复读的地方。

## 缘起

这个项目受 Anthropic Claude Code 团队成员 Thariq（[@trq212](https://x.com/trq212)）的一篇帖子启发——[《HTML 的不合理有效性》](https://x.com/trq212/status/2052809885763747935)。

核心观点是：**在 AI Agent 时代，Markdown 已不再是最佳的人机沟通格式，HTML 才是。**

原因很直接：当 AI 输出的内容超过 100 行，人几乎不会认真读完。而 HTML 能把同样的信息组织成图表、标签页、交互控件和可分享页面，让人真正愿意读进去，并能把反馈重新带回给 AI，形成闭环。

这个知识库就是对这个理念的实践——**用 HTML 来沉淀学习内容，而不是 Markdown 笔记或文档平台**。

## 是什么

一个静态 HTML 知识库。每篇笔记是一个独立的 `.html` 文件，通过首页 `index.html` 统一导航。不依赖任何构建工具，浏览器直接打开即可阅读。

## 分类

| 分类 | 目录 | 内容方向 |
|------|------|----------|
| 🤖 AI & 工程 | `map/ai/` | AI 工具、Agent 工程、提示词方法论 |
| 🧭 管理 | `map/management/` | 团队协作、决策框架、组织效能 |
| ⚙️ 运营 | `map/ops/` | 业务运营、增长、流程优化 |
| 🌱 个人成长 | `map/growth/` | 学习方法、思维模型、职业发展 |

## 文章列表

| 标题 | 分类 | 日期 |
|------|------|------|
| [为什么 Agent 输出正在从 Markdown 转向 HTML](map/ai/html-as-agent-output-format.html) | AI & 工程 | 2025-05-13 |
| [AI 团队怎么组（多智能体协作小白版）](map/ai/multi-agent-collaboration-methodology.html) | AI & 工程 | 2026-05-18 |
| [代码作为 Agent Harness — 极致工程化探索](map/ai/code-as-agent-harness-visual.html) | AI & 工程 | 2026-05-20 |

## 目录结构

```
ai-knowledge-map/
├── index.html          # 首页（分类导航 + 搜索）
└── map/
    ├── ai/             # AI & 工程
    ├── management/     # 管理
    ├── ops/            # 运营
    └── growth/         # 个人成长
```

每个子目录最多三层深度：`map/<分类>/<子主题>/<文章>.html`

## 如何使用

**本地阅读**

直接用浏览器打开 `index.html`，点击卡片跳转对应文章。

**添加新文章**

1. 在对应分类目录下新建 `.html` 文件
2. 在 `index.html` 对应的 `card-grid` 中添加一个卡片：

```html
<a href="map/<分类>/<文件名>.html" class="card"
   data-category="<分类>"
   data-title="文章标题"
   data-desc="简短描述">
  <span class="card-category">分类名</span>
  <div class="card-title">文章标题</div>
  <p class="card-desc">简短描述</p>
  <div class="card-footer">
    <span class="card-date">YYYY-MM-DD</span>
    <span class="card-arrow">→</span>
  </div>
</a>
```

3. 更新首页的「最近更新」侧边栏和文章计数。

## 设计风格

所有页面遵循同一套设计语言：

- 暖米色背景（`#faf8f5`）+ 衬线大标题（Georgia）
- 橙赭色强调色（`#d97757`）
- 支持系统暗色模式
- 无外部依赖，纯 HTML + CSS + 少量原生 JS
