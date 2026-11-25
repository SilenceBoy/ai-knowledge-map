# TASK-003：Personal Agent 白皮书上线

- 状态：已完成
- 负责人：Codex
- 创建日期：2026-11-25（Asia/Shanghai）
- 最近更新：2026-11-25 16:16（Asia/Shanghai）
- 关联提交：`dev` [8ba314d](https://github.com/SilenceBoy/ai-knowledge-map/commit/8ba314d7ba59bbaf1c558e0520aaa683eb5d1f1a)，生产 `main` [04067b5](https://github.com/SilenceBoy/ai-knowledge-map/commit/04067b5ed15ef547ca2173d72e100bc1c19908ed)

## 目标

将知识库中已审阅的《Personal Agent 使用与落地白皮书》v1.1 接入网站，沿用现有白皮书库和 Vercel 部署流程。

## 验收标准

- [x] 白皮书库可按名称或主题找到新条目，按日期排序时新条目排在首位。
- [x] 阅读页保留原文、7 张图解、章节目录和词条跳转，可返回白皮书库。
- [x] 本地定向回归通过，生产站列表和正文均可访问。

## 交付路径

- `whitepapers/personal-agent/index.html`
- `whitepapers/index.html`
- 生产站 [白皮书库](https://ai-map.silencebin.com/whitepapers/)和[阅读页](https://ai-map.silencebin.com/whitepapers/personal-agent/)。

## 验证记录

- 实现于 `dev`。原稿仅增加站内返回导航，去掉该导航及其样式后与源 HTML 字节一致。
- `node tests/test_whitepaper_preview.mjs` 通过。验证新增条目筛选、12 个目录入口、7 张内嵌图解、词条跳转与返回、窄屏阅读，以及既有白皮书入口。首页链接、标签测试及 `git diff --check` 通过。未运行全仓测试。
- Vercel 生产部署成功。正式域名列表和正文均返回 HTTP 200，列表显示 7 份白皮书，正文响应与发布文件字节一致。[Vercel 部署](https://vercel.com/silence52168-gmailcoms-projects/ai-knowledge-map/3GgR31k1oSVxp1VGb67eUunZorbh)
- 源稿为已审阅入库版本，本次网站发布以自动检查和线上回查验收。
