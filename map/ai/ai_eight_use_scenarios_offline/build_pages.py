from __future__ import annotations

from html import escape
from pathlib import Path


OUT_DIR = Path(__file__).resolve().parent


SCENES = [
    {
        "num": "01",
        "slug": "question-learning",
        "title": "提问学习",
        "subtitle": "把 AI 当一个什么都懂、还不嫌你烦的老师",
        "minute": "2 分钟",
        "one_liner": "遇到不懂的概念、图表、行业术语，先让 AI 帮你建立知识地图。",
        "triggers": ["这是什么？", "为什么？", "怎么做？", "看不懂这张图"],
        "moves": [
            "给身份背景：我是运营 / 老师 / 产品经理，不懂技术。",
            "一次问出高密度答案：定义、类比、例子、对比。",
            "遇到新词、新产品、新政策，打开搜索或要求来源。"
        ],
        "demo_title": "现场演示：把“RAG”讲给非技术同事听",
        "demo_steps": [
            "先用菜鸟问法：“什么是 RAG？”展示答案为什么虚。",
            "再用高密度问法，要求生活类比、业务例子、相关术语。",
            "最后追问：“如果我要对接这个项目，我最该问技术同事哪 5 个问题？”"
        ],
        "prompt": """我是一个 [你的身份/背景]，我想搞懂 [概念/问题]。

请你：
1. 用一个生活类比告诉我它是什么；
2. 解释它解决了什么问题，没有它会怎样；
3. 给我一个 [我的领域] 的例子；
4. 列出 3 个相关但容易搞混的概念，并一句话说清区别。""",
        "pitfall": "AI 默认不一定知道最新事件。问实时新闻、政策、价格、版本时，必须联网搜索或人工核实。",
        "source": "01-提问学习模式.md"
    },
    {
        "num": "02",
        "slug": "summary-integration",
        "title": "总结整合",
        "subtitle": "让 AI 当信息小秘书，把长的变短、把乱的变齐",
        "minute": "2 分钟",
        "one_liner": "总结不是删字，而是按你的目标把同一份信息换一种密度呈现。",
        "triggers": ["帮我总结", "提炼成表格", "一句话讲完", "会议纪要"],
        "moves": [
            "先说给谁看：自己、老板、同事、客户。",
            "指定输出密度：一句话、要点、精读版、表格、时间线。",
            "重要内容要求原文引用，方便抽查。"
        ],
        "demo_title": "现场演示：一篇长文输出三档总结",
        "demo_steps": [
            "复制一段课程或文章内容。",
            "让 AI 同时输出 L1 一句话、L2 要点、L3 精读版。",
            "说明同一输入可以服务“发群、自己看、汇报”三种场景。"
        ],
        "prompt": """请基于以下内容，分别输出三档总结：
L1：一句话，30 字内，适合发群里勾起兴趣；
L2：3-5 个要点，每条不超过 20 字；
L3：精读版，300 字内，保留核心结论和 1-2 个关键论据。

如果涉及数字、日期、人名，请保持原文一致，并标出依据。""",
        "pitfall": "长文中段、精确数字、强烈情绪最容易被 AI 弱化或漏掉。正式外发前要核原文。",
        "source": "02-总结整合模式.md"
    },
    {
        "num": "03",
        "slug": "creative-ideation",
        "title": "创意启发",
        "subtitle": "把 AI 当一个 24 小时不嫌烦的脑暴搭子",
        "minute": "2 分钟",
        "one_liner": "没思路时不要让 AI 给唯一答案，要让它先撒一大网候选。",
        "triggers": ["给我 10 个方案", "脑暴一下", "换个方向", "再大胆一点"],
        "moves": [
            "先要数量：10 个、20 个，而不是“几个”。",
            "强制差异：温情、搞笑、高级感、反常识都要覆盖。",
            "不满意就迭代：避开刚才的方向，再来一轮。"
        ],
        "demo_title": "现场演示：为这场线下分享起 10 个开场方式",
        "demo_steps": [
            "让 AI 给 10 个完全不同的开场方式。",
            "挑一个有意思的方向，要求再扩展 5 个变体。",
            "说明创意启发的价值是“给候选”，不是“替你拍板”。"
        ],
        "prompt": """我要做 [任务/活动/内容]，背景是：[补充背景]。

请给我 10 个完全不同方向的创意，每个包含：
1. 名称；
2. 一句话说明；
3. 适合的人群或场景；
4. 一个亮点动作。

要求 10 个之间风格差异明显，避免同质化。""",
        "pitfall": "AI 默认会给安全、平均化答案。要主动要求差异、跨界、反向思考。",
        "source": "03-创意启发模式.md"
    },
    {
        "num": "04",
        "slug": "content-generation",
        "title": "创作生成",
        "subtitle": "方向已经定了，让 AI 当按规则交活的写手",
        "minute": "2 分钟",
        "one_liner": "创作生成的关键不是“帮我写”，而是把规则说清楚。",
        "triggers": ["写一篇", "生成一份", "按这个风格", "出 3 版"],
        "moves": [
            "四件套：角色、任务、规则、示例。",
            "规则越具体，输出越可用：字数、结构、平台、语气、禁忌。",
            "一次出 3 版供挑选，比一版改 10 次更快。"
        ],
        "demo_title": "现场演示：把一句“帮我写小红书”升级成四件套",
        "demo_steps": [
            "先展示一句话提示词的平庸结果。",
            "补上角色、任务、规则、示例，再让 AI 输出 3 版。",
            "让听众看到：不是 AI 变聪明了，是任务被定义清楚了。"
        ],
        "prompt": """【角色】你是一位 [角色]，擅长 [能力]。
【任务】请为 [主题/产品/活动] 生成 [内容类型]。
【规则】
- 目标读者：[人群]
- 字数/时长：[范围]
- 结构：[开头/主体/结尾]
- 调性：[口语/专业/文艺/正式]
- 禁忌：[不要出现什么]
【示例】参考这个表达：[可选样本]

请输出 3 版，每版风格略有差异。""",
        "pitfall": "AI 初稿不是终稿。要加入你的真实经历、判断和语气，否则很容易有 AI 味。",
        "source": "04-创作生成模式.md"
    },
    {
        "num": "05",
        "slug": "reference-imitation",
        "title": "模仿参考",
        "subtitle": "风格、味道说不清时，让 AI 直接看样本",
        "minute": "2 分钟",
        "one_liner": "能贴样本就别硬描述，样本比形容词更准确。",
        "triggers": ["仿照这个", "学习这个风格", "提炼模板", "保持这个感觉"],
        "moves": [
            "先让 AI 提炼风格，再让它基于风格创作。",
            "文字、图像、格式都可以模仿参考。",
            "明确只学结构和风格，不复制原文句子。"
        ],
        "demo_title": "现场演示：建立一份“我的写作风格档案”",
        "demo_steps": [
            "贴 2-3 段你自己的旧内容。",
            "让 AI 提炼语气、句式、结构、常用表达。",
            "再要求它用这份风格档案写一个新主题。"
        ],
        "prompt": """请阅读以下样本，提炼它的风格：
1. 句式特点；
2. 语气和情绪基调；
3. 结构和逻辑；
4. 高频表达；
5. 给这个风格起一个名字。

然后基于该风格，为 [新主题] 写一份新内容。
注意：只学习风格和结构，不要复制原文任何一句话。""",
        "pitfall": "模仿不是抄袭。风格可以学，整句不能搬；涉及肖像、IP、品牌商用必须考虑授权。",
        "source": "05-模仿参考模式.md"
    },
    {
        "num": "06",
        "slug": "socratic-reflection",
        "title": "深思反问",
        "subtitle": "把 AI 当一个会质疑你的导师",
        "minute": "2 分钟",
        "one_liner": "AI 最被低估的价值，不是回答，而是提问。",
        "triggers": ["挑挑毛病", "反问我", "扮演评委", "推演风险"],
        "moves": [
            "不要说“帮我看看”，要说“狠狠质疑”。",
            "让 AI 扮演多个角色：老板、用户、竞品、法务。",
            "用于演讲、答辩、方案、决策前的预演。"
        ],
        "demo_title": "现场演示：让 AI 拷问这场分享",
        "demo_steps": [
            "把本次分享主题告诉 AI。",
            "让它扮演最挑剔的线下听众提 8 个问题。",
            "现场挑 1-2 个问题回答，展示“被问倒就是盲区”。"
        ],
        "prompt": """请扮演一位 [苛刻评委/投资人/老板/目标用户]，专门挑漏洞。

我的方案是：[描述方案]

请从以下角度提出最尖锐的问题：
1. 目标是否清楚；
2. 证据是否充分；
3. 用户是否真的需要；
4. 风险在哪里；
5. 哪句话最不可信。

不要安慰我，只问真正会影响成败的问题。""",
        "pitfall": "反问是为了看清，不是为了拖延决策。给自己设定时间盒，问完要行动。",
        "source": "06-深思反问模式.md"
    },
    {
        "num": "07",
        "slug": "translation-transformation",
        "title": "翻译转化",
        "subtitle": "人话、外语、代码、图像、文档都能互相转换",
        "minute": "2 分钟",
        "one_liner": "凡是能变成信息的东西，都可以让 AI 换一种形态呈现。",
        "triggers": ["翻译成", "换种说法", "解释这段代码", "和 PDF 对话"],
        "moves": [
            "语言互译要加上下文、读者和风格要求。",
            "自然语言可以转代码，代码也能转大白话。",
            "图像、PDF、Excel 都可以变成可对话对象。"
        ],
        "demo_title": "现场演示：把专业话翻译成大白话",
        "demo_steps": [
            "拿一段专业说明或英文段落。",
            "让 AI 输出“正式版 / 口语版 / 10 岁小孩能懂版”。",
            "说明翻译不只是中英互译，而是信息形态转换。"
        ],
        "prompt": """请把下面内容从 [当前形态/语气] 转成 [目标形态/语气]。

要求：
1. 目标读者是 [人群]；
2. 保留关键信息，不要遗漏数字、日期、专有名词；
3. 表达要符合 [场景]；
4. 如有不确定术语，请保留原文并说明。

原文：[粘贴内容]""",
        "pitfall": "合同、医疗、法律、高精度技术文档只能让 AI 做初稿，正式使用必须人工审核。",
        "source": "07-翻译转化模式.md"
    },
    {
        "num": "08",
        "slug": "analysis-research",
        "title": "分析研究",
        "subtitle": "让 AI 当数据分析师和用户情绪解读员",
        "minute": "2 分钟",
        "one_liner": "分析的本质是找关系：文字里的情绪关系，数据里的变量关系。",
        "triggers": ["从数据里看出", "评论情绪", "找异常", "用户到底怎么想"],
        "moves": [
            "语言分析：情感分类、意图识别、观点聚类。",
            "数据分析：描述走势、找关联、找异常、给建议。",
            "关键数字要用代码或表格复核，相关不等于因果。"
        ],
        "demo_title": "现场演示：把 30 条评论变成洞察表",
        "demo_steps": [
            "准备一组产品评论或活动反馈。",
            "让 AI 聚类出高频观点、正负情绪、Top 5 诉求。",
            "追问每个结论的原始证据，展示可核查分析。"
        ],
        "prompt": """下面是 [产品/活动/内容] 的用户反馈。请做结构化分析：
1. 情感分类：正/负/中，并统计比例；
2. 观点聚类：归纳 5-8 个主题，每个主题给代表原话；
3. Top 5 用户诉求：按重要性排序；
4. 危险信号：投诉、退款、竞品、法律相关；
5. 一句话洞察：最大的赞和最大的痛。

反馈：[粘贴内容]""",
        "pitfall": "AI 给的是参考结论。样本偏差、因果误判、算错数字都可能发生，关键决策必须复核。",
        "source": "08-分析研究模式.md"
    },
]


CSS = """
:root {
  color-scheme: light dark;
  --bg: #faf8f5;
  --surface: #f0ede8;
  --surface-2: #fffdf9;
  --text: #2c2825;
  --muted: #746d64;
  --border: #d4cfc7;
  --clay: #d97757;
  --olive: #788c5d;
  --sky: #6a8caf;
  --ink: #141413;
  --shadow: 0 18px 60px rgba(44, 40, 37, .10);
}

[data-theme="dark"] {
  --bg: #171615;
  --surface: #23211f;
  --surface-2: #2c2926;
  --text: #f4efe8;
  --muted: #b8afa4;
  --border: #49433d;
  --clay: #e79678;
  --olive: #a9bc88;
  --sky: #9bb8d5;
  --ink: #f8f4ed;
  --shadow: 0 18px 60px rgba(0, 0, 0, .28);
}

* { box-sizing: border-box; }
html { scroll-behavior: smooth; }
body {
  margin: 0;
  background:
    radial-gradient(circle at 20% 0%, rgba(217, 119, 87, .10), transparent 30%),
    linear-gradient(135deg, var(--bg), var(--surface));
  color: var(--text);
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "PingFang SC", "Microsoft YaHei", sans-serif;
  line-height: 1.65;
}
a { color: inherit; text-decoration: none; }
button { font: inherit; }
.shell { width: min(1180px, calc(100% - 32px)); margin: 0 auto; }
.topbar {
  position: sticky;
  top: 0;
  z-index: 20;
  backdrop-filter: blur(16px);
  background: color-mix(in srgb, var(--bg) 82%, transparent);
  border-bottom: 1px solid var(--border);
}
.topbar-inner {
  min-height: 58px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
}
.brand { display: flex; align-items: center; gap: 10px; font-weight: 750; }
.brand-mark {
  width: 30px;
  height: 30px;
  border: 1px solid var(--border);
  background: var(--surface-2);
  display: grid;
  place-items: center;
  border-radius: 8px;
  color: var(--clay);
  font-family: ui-monospace, SFMono-Regular, Menlo, monospace;
  font-size: 13px;
}
.nav-actions { display: flex; align-items: center; gap: 8px; flex-wrap: wrap; justify-content: flex-end; }
.btn {
  min-height: 36px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  border: 1px solid var(--border);
  background: var(--surface-2);
  color: var(--text);
  padding: 7px 12px;
  border-radius: 8px;
  cursor: pointer;
  box-shadow: 0 1px 0 rgba(0,0,0,.03);
}
.btn:hover { border-color: var(--clay); }
.hero {
  padding: 58px 0 30px;
  display: grid;
  grid-template-columns: minmax(0, 1.2fr) minmax(320px, .8fr);
  gap: 28px;
  align-items: center;
}
.kicker {
  color: var(--clay);
  font-family: ui-monospace, SFMono-Regular, Menlo, monospace;
  font-size: 13px;
  text-transform: uppercase;
  letter-spacing: 0;
  font-weight: 700;
}
h1 {
  font-family: Georgia, "Times New Roman", "Songti SC", serif;
  font-size: clamp(40px, 7vw, 82px);
  line-height: .96;
  letter-spacing: 0;
  margin: 14px 0 18px;
}
.subtitle {
  color: var(--muted);
  font-size: clamp(17px, 2.2vw, 23px);
  max-width: 760px;
}
.hero-panel, .window, .card, .prompt-box {
  border: 1px solid var(--border);
  background: color-mix(in srgb, var(--surface-2) 88%, transparent);
  box-shadow: var(--shadow);
}
.hero-panel { border-radius: 12px; padding: 22px; }
.stat-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; margin-top: 18px; }
.stat {
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 12px;
  background: var(--surface);
}
.stat b { display: block; font-size: 24px; line-height: 1.1; }
.stat span { color: var(--muted); font-size: 13px; }
.section { padding: 28px 0; }
.section-head {
  display: flex;
  align-items: end;
  justify-content: space-between;
  gap: 20px;
  margin-bottom: 16px;
}
h2 {
  font-size: clamp(24px, 3vw, 34px);
  line-height: 1.15;
  margin: 0;
  letter-spacing: 0;
}
.section-note { color: var(--muted); max-width: 580px; }
.grid { display: grid; gap: 14px; }
.grid-2 { grid-template-columns: repeat(2, minmax(0, 1fr)); }
.grid-3 { grid-template-columns: repeat(3, minmax(0, 1fr)); }
.grid-4 { grid-template-columns: repeat(4, minmax(0, 1fr)); }
.card {
  border-radius: 10px;
  padding: 18px;
  min-height: 100%;
}
.card h3 { margin: 0 0 8px; font-size: 19px; line-height: 1.25; }
.card p { margin: 0; color: var(--muted); }
.scene-card {
  display: grid;
  gap: 12px;
  transition: transform .18s ease, border-color .18s ease;
}
.scene-card:hover { transform: translateY(-2px); border-color: var(--clay); }
.scene-num {
  width: 38px;
  height: 38px;
  display: grid;
  place-items: center;
  border-radius: 8px;
  background: var(--ink);
  color: var(--bg);
  font-family: ui-monospace, SFMono-Regular, Menlo, monospace;
}
.tag-row { display: flex; flex-wrap: wrap; gap: 8px; }
.tag {
  display: inline-flex;
  align-items: center;
  min-height: 28px;
  border: 1px solid var(--border);
  border-radius: 999px;
  padding: 4px 10px;
  color: var(--muted);
  background: var(--surface);
  font-size: 13px;
}
.tag.clay { color: var(--clay); }
.tag.olive { color: var(--olive); }
.tag.sky { color: var(--sky); }
.window { border-radius: 12px; overflow: hidden; }
.window-bar {
  height: 38px;
  display: flex;
  align-items: center;
  gap: 7px;
  padding: 0 14px;
  border-bottom: 1px solid var(--border);
  background: var(--surface);
}
.dot { width: 10px; height: 10px; border-radius: 50%; background: var(--clay); }
.dot:nth-child(2) { background: var(--olive); }
.dot:nth-child(3) { background: var(--sky); }
.window-title { margin-left: 8px; color: var(--muted); font-size: 13px; }
.window-body { padding: 18px; }
.timeline {
  display: grid;
  grid-template-columns: repeat(5, minmax(0, 1fr));
  gap: 10px;
}
.time-block {
  border-left: 3px solid var(--clay);
  background: var(--surface-2);
  border-radius: 8px;
  padding: 12px;
  border-top: 1px solid var(--border);
  border-right: 1px solid var(--border);
  border-bottom: 1px solid var(--border);
}
.time-block b { display: block; }
.time-block span { color: var(--muted); font-size: 13px; }
.matrix {
  width: 100%;
  min-height: 340px;
  border: 1px solid var(--border);
  border-radius: 12px;
  background: var(--surface-2);
}
.list { padding-left: 20px; margin: 0; }
.list li { margin: 8px 0; }
.prompt-box { border-radius: 12px; overflow: hidden; }
.prompt-head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  padding: 12px 14px;
  border-bottom: 1px solid var(--border);
  background: var(--surface);
}
pre {
  margin: 0;
  padding: 18px;
  overflow: auto;
  white-space: pre-wrap;
  color: var(--surface-2);
  background: var(--ink);
  line-height: 1.55;
}
code { font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; font-size: 14px; }
.warning {
  border-left: 4px solid var(--clay);
  padding: 14px 16px;
  background: color-mix(in srgb, var(--clay) 12%, var(--surface-2));
  border-radius: 8px;
}
.footer {
  padding: 30px 0 46px;
  color: var(--muted);
  border-top: 1px solid var(--border);
  margin-top: 34px;
}
.pager { display: flex; justify-content: space-between; gap: 12px; margin-top: 24px; flex-wrap: wrap; }
.small { color: var(--muted); font-size: 13px; }
.toc {
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
  margin-top: 18px;
}
.toc a {
  border: 1px solid var(--border);
  background: var(--surface-2);
  border-radius: 999px;
  padding: 6px 10px;
  color: var(--muted);
  font-size: 13px;
}
.toc a:hover { color: var(--clay); border-color: var(--clay); }
details {
  border: 1px solid var(--border);
  border-radius: 10px;
  padding: 14px 16px;
  background: var(--surface-2);
}
summary { cursor: pointer; font-weight: 700; }
@media (max-width: 900px) {
  .hero { grid-template-columns: 1fr; padding-top: 34px; }
  .grid-2, .grid-3, .grid-4 { grid-template-columns: 1fr; }
  .timeline { grid-template-columns: 1fr; }
  .section-head { display: block; }
  .nav-actions .optional { display: none; }
  h1 { font-size: 44px; }
}
"""


JS = """
function toggleTheme() {
  const current = document.documentElement.getAttribute('data-theme') || 'light';
  const next = current === 'dark' ? 'light' : 'dark';
  document.documentElement.setAttribute('data-theme', next);
  localStorage.setItem('ai8-theme', next);
}
function copyPrompt(id) {
  const node = document.getElementById(id);
  if (!node) return;
  navigator.clipboard.writeText(node.innerText).then(() => {
    const btn = document.querySelector('[data-copy-target="' + id + '"]');
    if (!btn) return;
    const old = btn.innerText;
    btn.innerText = '已复制';
    setTimeout(() => btn.innerText = old, 1200);
  });
}
(function initTheme() {
  const saved = localStorage.getItem('ai8-theme');
  if (saved) document.documentElement.setAttribute('data-theme', saved);
})();
"""


def page_filename(scene: dict[str, object]) -> str:
    return f"scene-{scene['num']}-{scene['slug']}.html"


def topbar(active: str = "") -> str:
    return f"""
<header class="topbar">
  <div class="shell topbar-inner">
    <a class="brand" href="index.html" aria-label="返回首页">
      <span class="brand-mark">AI</span>
      <span>八大使用场景</span>
    </a>
    <nav class="nav-actions" aria-label="页面操作">
      <a class="btn optional" href="index.html">首页</a>
      <button class="btn" type="button" onclick="toggleTheme()">明暗</button>
    </nav>
  </div>
</header>
"""


def html_doc(title: str, body: str) -> str:
    return f"""<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{escape(title)}</title>
  <style>{CSS}</style>
</head>
<body>
{body}
<script>{JS}</script>
</body>
</html>
"""


def render_index() -> str:
    cards = "\n".join(
        f"""
        <a class="card scene-card" href="{page_filename(scene)}">
          <span class="scene-num">{scene['num']}</span>
          <h3>{escape(scene['title'])}</h3>
          <p>{escape(scene['one_liner'])}</p>
          <div class="tag-row">
            <span class="tag clay">{escape(scene['minute'])}</span>
            <span class="tag">{escape(scene['triggers'][0])}</span>
          </div>
        </a>
        """
        for scene in SCENES
    )
    timeline = """
    <div class="timeline">
      <div class="time-block"><b>0-2'</b><span>开场：为什么普通人需要 AI 雷达</span></div>
      <div class="time-block"><b>2-10'</b><span>前四个场景：学、整、想、写</span></div>
      <div class="time-block"><b>10-18'</b><span>后四个场景：仿、问、转、析</span></div>
      <div class="time-block"><b>18-19'</b><span>组合拳：真实任务不是单招</span></div>
      <div class="time-block"><b>19-20'</b><span>行动清单：今天就试一个场景</span></div>
    </div>
    """
    matrix_svg = """
    <svg class="matrix" viewBox="0 0 760 420" role="img" aria-label="八大场景二维矩阵">
      <rect x="0" y="0" width="760" height="420" rx="18" fill="currentColor" opacity="0.035"></rect>
      <line x1="380" y1="58" x2="380" y2="365" stroke="currentColor" opacity=".24"></line>
      <line x1="86" y1="210" x2="690" y2="210" stroke="currentColor" opacity=".24"></line>
      <text x="235" y="36" text-anchor="middle" fill="currentColor" font-size="18" font-weight="700">目标明确</text>
      <text x="525" y="36" text-anchor="middle" fill="currentColor" font-size="18" font-weight="700">目标模糊</text>
      <text x="34" y="142" fill="currentColor" font-size="17" font-weight="700">输入端</text>
      <text x="34" y="300" fill="currentColor" font-size="17" font-weight="700">输出端</text>
      <g font-size="18" font-weight="700">
        <rect x="122" y="90" width="210" height="74" rx="12" fill="#6A8CAF" opacity=".20"></rect>
        <text x="227" y="122" text-anchor="middle" fill="currentColor">提问学习</text>
        <text x="227" y="147" text-anchor="middle" fill="currentColor" font-size="13" opacity=".68">得到理解</text>
        <rect x="122" y="242" width="210" height="74" rx="12" fill="#D97757" opacity=".20"></rect>
        <text x="227" y="274" text-anchor="middle" fill="currentColor">创作生成</text>
        <text x="227" y="299" text-anchor="middle" fill="currentColor" font-size="13" opacity=".68">产出内容</text>
        <rect x="428" y="90" width="210" height="74" rx="12" fill="#788C5D" opacity=".20"></rect>
        <text x="533" y="122" text-anchor="middle" fill="currentColor">深思反问</text>
        <text x="533" y="147" text-anchor="middle" fill="currentColor" font-size="13" opacity=".68">看见盲区</text>
        <rect x="428" y="242" width="210" height="74" rx="12" fill="#D97757" opacity=".16"></rect>
        <text x="533" y="274" text-anchor="middle" fill="currentColor">创意启发</text>
        <text x="533" y="299" text-anchor="middle" fill="currentColor" font-size="13" opacity=".68">扩展候选</text>
      </g>
      <g font-size="14" opacity=".75" fill="currentColor">
        <text x="227" y="188" text-anchor="middle">总结整合 / 翻译转化</text>
        <text x="533" y="188" text-anchor="middle">分析研究</text>
        <text x="227" y="340" text-anchor="middle">翻译转化</text>
        <text x="533" y="340" text-anchor="middle">模仿参考</text>
      </g>
    </svg>
    """
    body = f"""
{topbar()}
<main>
  <section class="shell hero">
    <div>
      <div class="kicker">Offline Talk · 20 Minutes</div>
      <h1>AI 八大使用场景</h1>
      <p class="subtitle">给小白装上“AI 雷达”：不是先背提示词，而是先识别这一刻该用哪一种 AI 姿势。</p>
      <div class="toc" aria-label="快速入口">
        <a href="#route">20 分钟路线</a>
        <a href="#matrix">判断矩阵</a>
        <a href="#scenes">八大场景</a>
        <a href="#closing">结尾行动</a>
      </div>
    </div>
    <aside class="hero-panel">
      <div class="kicker">核心判断</div>
      <h2>AI 能干，和 AI 适合干，是两回事。</h2>
      <p class="section-note">本次分享把课程压缩成 8 个“抽屉”。听众只要学会把任务放进对应抽屉，就能知道下一句话怎么对 AI 说。</p>
      <div class="stat-grid">
        <div class="stat"><b>8</b><span>使用场景</span></div>
        <div class="stat"><b>20'</b><span>分享时长</span></div>
        <div class="stat"><b>1</b><span>现场演示线</span></div>
      </div>
    </aside>
  </section>

  <section id="route" class="shell section">
    <div class="section-head">
      <h2>20 分钟讲法</h2>
      <p class="section-note">节奏上每个场景只讲一个判断点、一个提示词、一个演示动作。</p>
    </div>
    {timeline}
  </section>

  <section id="matrix" class="shell section">
    <div class="section-head">
      <h2>一张图判断该用哪种模式</h2>
      <p class="section-note">先问两个问题：我要拿信息还是出内容？目标明确还是目标模糊？</p>
    </div>
    {matrix_svg}
  </section>

  <section id="scenes" class="shell section">
    <div class="section-head">
      <h2>八大场景入口</h2>
      <p class="section-note">每个页面都是独立讲解页，适合现场点击进入，也可以直接单独打开。</p>
    </div>
    <div class="grid grid-4">{cards}</div>
  </section>

  <section id="closing" class="shell section">
    <div class="window">
      <div class="window-bar"><span class="dot"></span><span class="dot"></span><span class="dot"></span><span class="window-title">最后 60 秒</span></div>
      <div class="window-body grid grid-3">
        <div>
          <h3>带走一句话</h3>
          <p>遇到任务，先判断场景，再写提示词。</p>
        </div>
        <div>
          <h3>现场练习</h3>
          <p>回想今天做过的一件事，把它放进 8 个场景之一。</p>
        </div>
        <div>
          <h3>行动建议</h3>
          <p>不要一口气学完，今天挑一个最痛的场景试 3 轮对话。</p>
        </div>
      </div>
    </div>
  </section>
</main>
<footer class="footer">
  <div class="shell small">内容来源：方法库/AI八大使用场景-小白入门课。页面为线下 20 分钟分享重组版。</div>
</footer>
"""
    return html_doc("AI 八大使用场景线下分享", body)


def render_scene(scene: dict[str, object], prev_scene: dict[str, object] | None, next_scene: dict[str, object] | None) -> str:
    trigger_tags = "".join(f'<span class="tag sky">{escape(t)}</span>' for t in scene["triggers"])
    moves = "".join(f"<li>{escape(item)}</li>" for item in scene["moves"])
    steps = "".join(f"<li>{escape(item)}</li>" for item in scene["demo_steps"])
    prompt_id = f"prompt-{scene['num']}"
    prev_link = f'<a class="btn" href="{page_filename(prev_scene)}">上一页：{escape(prev_scene["title"])}</a>' if prev_scene else '<a class="btn" href="index.html">返回首页</a>'
    next_link = f'<a class="btn" href="{page_filename(next_scene)}">下一页：{escape(next_scene["title"])}</a>' if next_scene else '<a class="btn" href="index.html#closing">回到结尾</a>'

    flow_svg = f"""
    <svg class="matrix" viewBox="0 0 760 260" role="img" aria-label="{escape(scene['title'])}讲解路径">
      <rect x="0" y="0" width="760" height="260" rx="18" fill="currentColor" opacity="0.035"></rect>
      <g font-size="15" fill="currentColor">
        <rect x="48" y="80" width="150" height="74" rx="12" fill="#6A8CAF" opacity=".22"></rect>
        <text x="123" y="112" text-anchor="middle" font-weight="700">识别时刻</text>
        <text x="123" y="137" text-anchor="middle" opacity=".68">什么时候用</text>
        <path d="M210 117 L270 117" stroke="currentColor" opacity=".38" stroke-width="2"></path>
        <path d="M264 108 L278 117 L264 126" fill="none" stroke="currentColor" opacity=".38" stroke-width="2"></path>
        <rect x="292" y="80" width="176" height="74" rx="12" fill="#D97757" opacity=".20"></rect>
        <text x="380" y="112" text-anchor="middle" font-weight="700">套提示词</text>
        <text x="380" y="137" text-anchor="middle" opacity=".68">把任务说清</text>
        <path d="M480 117 L540 117" stroke="currentColor" opacity=".38" stroke-width="2"></path>
        <path d="M534 108 L548 117 L534 126" fill="none" stroke="currentColor" opacity=".38" stroke-width="2"></path>
        <rect x="562" y="80" width="150" height="74" rx="12" fill="#788C5D" opacity=".22"></rect>
        <text x="637" y="112" text-anchor="middle" font-weight="700">现场演示</text>
        <text x="637" y="137" text-anchor="middle" opacity=".68">让听众看见差异</text>
      </g>
      <text x="380" y="210" text-anchor="middle" fill="currentColor" font-size="18" font-weight="700">{escape(scene['one_liner'])}</text>
    </svg>
    """

    body = f"""
{topbar()}
<main>
  <section class="shell hero">
    <div>
      <div class="kicker">Scene {scene['num']} · {escape(scene['minute'])}</div>
      <h1>{escape(scene['title'])}</h1>
      <p class="subtitle">{escape(scene['subtitle'])}</p>
      <div class="tag-row">{trigger_tags}</div>
    </div>
    <aside class="hero-panel">
      <div class="kicker">这一页只讲透一句话</div>
      <h2>{escape(scene['one_liner'])}</h2>
      <p class="section-note">来源：方法库/AI八大使用场景-小白入门课/{escape(scene['source'])}</p>
    </aside>
  </section>

  <section class="shell section">
    {flow_svg}
  </section>

  <section class="shell section">
    <div class="section-head">
      <h2>讲解重点</h2>
      <p class="section-note">现场不要铺满知识点，只讲这 3 个动作。</p>
    </div>
    <div class="grid grid-2">
      <div class="card">
        <h3>小白触发词</h3>
        <div class="tag-row">{trigger_tags}</div>
      </div>
      <div class="card">
        <h3>三步动作</h3>
        <ol class="list">{moves}</ol>
      </div>
    </div>
  </section>

  <section class="shell section">
    <div class="window">
      <div class="window-bar"><span class="dot"></span><span class="dot"></span><span class="dot"></span><span class="window-title">Live Demo</span></div>
      <div class="window-body">
        <h2>{escape(scene['demo_title'])}</h2>
        <ol class="list">{steps}</ol>
      </div>
    </div>
  </section>

  <section class="shell section">
    <div class="section-head">
      <h2>可复制提示词</h2>
      <p class="section-note">现场演示时可以直接复制，替换方括号内容。</p>
    </div>
    <div class="prompt-box">
      <div class="prompt-head">
        <strong>{escape(scene['title'])}模板</strong>
        <button class="btn" type="button" data-copy-target="{prompt_id}" onclick="copyPrompt('{prompt_id}')">复制</button>
      </div>
      <pre><code id="{prompt_id}">{escape(scene['prompt'])}</code></pre>
    </div>
  </section>

  <section class="shell section">
    <div class="warning">
      <strong>误区提醒：</strong>{escape(scene['pitfall'])}
    </div>
    <details style="margin-top:14px">
      <summary>讲者备注：这一页怎么收尾</summary>
      <p>用一句话收束：“这个场景不是让 AI 替你判断，而是让 AI 帮你把任务推进到下一步。”然后点击进入下一场景。</p>
    </details>
    <div class="pager">{prev_link}{next_link}</div>
  </section>
</main>
<footer class="footer">
  <div class="shell small">独立 HTML 页面，可直接打开。内容经过 20 分钟线下分享场景重组，不是课程原文搬运。</div>
</footer>
"""
    return html_doc(f"{scene['num']} {scene['title']} - AI 八大使用场景", body)


def main() -> None:
    (OUT_DIR / "index.html").write_text(render_index(), encoding="utf-8")
    for i, scene in enumerate(SCENES):
        prev_scene = SCENES[i - 1] if i > 0 else None
        next_scene = SCENES[i + 1] if i < len(SCENES) - 1 else None
        (OUT_DIR / page_filename(scene)).write_text(render_scene(scene, prev_scene, next_scene), encoding="utf-8")


if __name__ == "__main__":
    main()
