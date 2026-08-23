# TASK-001：迁移我的课程入口

- 状态：待验证
- 负责人：Codex
- 创建时间：2026-08-23 16:31（Asia/Shanghai）
- 最近更新：2026-08-23 16:35（Asia/Shanghai）
- 关联全局任务：TASK-20260823-163130
- 验收人：人工

## 目标

将“普通人用 AI 的八个日常场景”离线课件迁入本项目的`我的课程`目录，并从知识地图首页进入该课程目录。

## 验收标准

- [x] 源课件完整复制到`我的课程/ai_eight_use_scenarios_offline/index.html`。
- [x] `我的课程/index.html`可展示并链接到该课件。
- [x] 首页课程入口链接到`我的课程/`。
- [x] 链接校验和可运行的现有自动化测试通过。
- [ ] 人工在浏览器确认页面展示正常。

## 已完成

- 已核对源目录仅有一个自包含的`index.html`，无额外静态资源依赖。
- 已记录源文件 SHA-256：`f6af3aeffe38f84ce0ff0e802af00251f892141544bd1f526abd5aeabde49271`。
- 已创建`我的课程/index.html`并迁移课件；首页导航已增加“我的课程”入口。
- 首页入口测试先在缺少课程目录页时按预期失败，恢复页面后通过。
- 已通过 5 个 Python 页面测试、`tests/test_serve_background.sh`、源/目标字节一致性检查和临时静态服务器 HTTP 200 访问检查。

## 正在进行

等待人工在浏览器确认课程目录页和课件页的视觉展示。

## 下一步

1. 人工打开首页“我的课程”入口并确认视觉展示。
2. 人工打开课件并确认展示正常后，将任务标为“已完成”。

## 风险与阻塞

- 浏览器筛选测试`node tests/test_homepage_tag_filters.mjs`未执行：当前项目未安装`playwright`，命令在加载模块前失败；不影响本次静态链接与迁移内容校验，但不能替代浏览器端筛选回归。
- 仓库原有`map/ai/ai_eight_use_scenarios_offline/index.html`与源文件内容不同；本任务不删除该历史文件。

## 交付物

- `我的课程/index.html`
- `我的课程/ai_eight_use_scenarios_offline/index.html`
- `index.html`
- `tests/test_homepage_links.py`

## 验证记录

- RED：暂时移除`我的课程/index.html`后运行`python3 tests/test_homepage_links.py`，按预期报“首页“我的课程”入口或课程目录页缺失”。
- GREEN：恢复目录页后运行`python3 tests/test_homepage_links.py`，通过；其余`test_homepage_tags.py`、`test_scene_navigation.py`、`test_ai_coding_client_perspective.py`、`test_growth_ppt_integration.py`与`tests/test_serve_background.sh`均通过。
- 完整性：源/目标课件字节一致；临时静态服务器访问`/我的课程/`及`/我的课程/ai_eight_use_scenarios_offline/`均为 HTTP 200；`git diff --check`通过。
