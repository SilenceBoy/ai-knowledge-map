# TASK-002：白皮书博客改版预览

- 状态：已完成
- 负责人：Codex
- 创建时间：2026-11-11 16:49（Asia/Shanghai）
- 最近更新：2026-11-11 22:31（Asia/Shanghai）
- 关联分支：`dev`，基线 `3af88ec`
- 验收人：Bin

## 目标

从知识库选取代表性白皮书，在本地 `dev` 分支制作博客首页与白皮书列表页，交由 Bin 预览后再决定发布。

## 验收标准

- [x] 首页展示推荐白皮书、精选列表、文章和课程入口。
- [x] 白皮书列表支持搜索、主题筛选和排序，样本有可用的阅读入口。
- [x] 桌面与移动端通过浏览器检查，原有文章检索和课程链接可用。
- [x] 三份白皮书接入知识库正文，保留原文结构和随文图片。
- [x] 补充三份独立原创白皮书和任务账本 v3.0 原版网页。
- [x] Bin 确认页面视觉与白皮书范围。

## 素材

- 《AI 时代超级个体白皮书》：知识库成品库方法库同名目录，总览与 7 章转为静态正文，保留原稿待审状态。原版 HTML 演示从正文进入。
- 《AI 任务账本方法论与商业落地白皮书》：v2.0 Markdown 原稿及附录，49 个目录项。
- 《小白能学会的提示词技巧》：按知识库目录接入 18 章、1 个附章及 23 张随文图。
- 扩展盘点覆盖 NAS 知识库和 AI_OS 培训课程制作项目。课程项目找到三份独立白皮书：《编程方法论白皮书》v1.0、《AI 写真创作白皮书》v0.1、《AI 写真自动化白皮书》入门版 v1.0。写真创作源稿待用户审阅，两份写真白皮书正文与目标不同。
- 任务账本 v3.0 原版来自 AI 工作台设计课程，作为同一条目的默认阅读页，与原 v2.0 双向链接。来源库行业报告和 Wiki 摘要属于外部材料；旧账本版本、教学草案和课件不新增卡片。

## 交付与验证

- 交付路径：`index.html`、`whitepapers/index.html`、`assets/portal.css`、`whitepapers/library.js` 和三份阅读样本目录。
- 本地预览：[首页](http://127.0.0.1:8766/) · [白皮书库](http://127.0.0.1:8766/whitepapers/)。复用已运行的 8766 静态服务。
- Playwright：`tests/test_whitepaper_preview.mjs` 验证搜索、主题、排序、清除筛选、三个阅读与返回入口、原演示翻页，以及 320、390、768px 宽度无横向溢出。已检查桌面和手机截图。
- 回归：`tests/test_homepage_tag_filters.mjs`、`tests/test_homepage_links.py`、`tests/test_homepage_tags.py` 通过。首页、白皮书库、三个阅读路径与课程目录均返回 HTTP 200。未运行全仓测试。
- 正文补齐验证：`tests/test_whitepaper_preview.mjs` 通过。三份目录共 76 项均对应正文锚点，章节可跳转，23 张随文图浏览器解码通过且与知识库原件字节一致，390px 正文页无横向溢出。
- 扩展交付：`whitepapers/coding-methodology/index.html`、`whitepapers/ai-portrait-creation/index.html`、`whitepapers/ai-portrait-automation/index.html`、`whitepapers/task-ledger/v3.html`。原版 HTML 除新增返回导航和账本页手机端换行样式外，与来源文件字节一致。
- 扩展验证：`tests/test_whitepaper_preview.mjs` 通过六项入口、主题筛选和排序、原版目录及内嵌插图、390px 正文布局与 v2.0/v3.0 互链。首页链接、标签与 `git diff --check` 通过。
- 人工验收：2026-11-11 22:31 Bin 确认本地预览通过，并授权提交和推送 `dev`。网站部署不在本次范围内。
