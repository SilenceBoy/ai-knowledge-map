# 多页静态站点 — 统一悬浮返回按钮方案

## 背景与决策

### 问题

静态多页站点（没有框架路由）的子页面打开后，没有统一的返回首页入口。

### 方案对比

| 方案 | 解耦程度 | 改动量 | 主要问题 |
|---|---|---|---|
| 每页手写返回链接 | 高 | 大，多处维护 | 样式散落各页 |
| **JS 注入悬浮按钮（本方案）** | **高** | **小，统一维护** | 依赖 JS |
| iframe 外框 | 中 | 中 | URL/后退键/SEO 全乱 |

选择 JS 注入方案的原因：子页面只引一行 `<script>`，样式和逻辑全部集中在 `nav.js`，以后改一处即全站生效。

---

## 使用方法

### 给新页面接入

在页面 `</body>` 前加一行：

```html
<script src="/nav.js" defer></script>
```

> `/nav.js` 使用绝对路径，需要通过 HTTP 服务访问（`http://localhost:xxxx` 或线上域名）。直接用 `file://` 打开 HTML 文件时脚本不会加载。

### 本地预览

```bash
# 在项目根目录执行
python3 -m http.server 8765
# 访问 http://localhost:8765
```

---

## 功能说明

- **悬浮按钮**：固定在页面上，不随滚动消失
- **样式统一**：对齐首页 `.nav-home` 风格（Inter 字体、橙色 `#d97757` pill 按钮）
- **深色模式**：同时兼容 `prefers-color-scheme: dark`（媒体查询）和 `data-theme="dark"`（属性切换），两种写法均支持
- **可拖动**：鼠标/触屏均可拖动到任意位置，移动距离 < 4px 视为点击不触发拖拽
- **位置记忆**：拖动结束后位置写入 `localStorage`，下次打开自动恢复

---

## 关键代码解析

### 1. 样式注入（不依赖任何页面的 CSS 变量）

```js
var style = document.createElement('style');
style.textContent = `
  #_nav_home {
    position: fixed;
    z-index: 9999;
    height: 38px;
    padding: 0 18px;
    background: #d97757;
    border-radius: 99px;
    color: #fff;
    font: 600 13px/1 "Inter", ui-sans-serif, sans-serif;
    /* ... */
  }
  /* 拖拽中状态 */
  #_nav_home._dragging {
    cursor: grabbing;
    transform: scale(1.06);
  }
`;
document.head.appendChild(style);
```

用 `id` 而非 `class` 避免与页面已有样式冲突，变量名加 `_` 前缀降低命名碰撞风险。

### 2. 拖拽核心：区分点击与拖动

```js
var DRAG_THRESHOLD = 4; // px，移动距离低于此视为点击

function onDown(e) {
  dragging = true;
  moved = false;
  startX = clientX; startY = clientY;
  startLeft = btn.offsetLeft; startTop = btn.offsetTop;
  e.preventDefault(); // 阻止文字被选中
}

function onMove(e) {
  var dx = clientX - startX, dy = clientY - startY;
  // 超过阈值才标记为"已拖动"
  if (!moved && Math.sqrt(dx*dx + dy*dy) > DRAG_THRESHOLD) {
    moved = true;
    btn.classList.add('_dragging');
  }
  // 边界限制：距屏幕边缘至少 8px
  var newLeft = clamp(startLeft + dx, 8, window.innerWidth  - btn.offsetWidth  - 8);
  var newTop  = clamp(startTop  + dy, 8, window.innerHeight - btn.offsetHeight - 8);
  applyPos(newTop, newLeft);
}

function onUp(e) {
  btn.classList.remove('_dragging');
  if (moved) {
    savePos(btn.offsetTop, btn.offsetLeft);
    // 关键：阻止拖动结束后误触 click 跳转
    e.preventDefault();
    btn.addEventListener('click', stopOnce, true);
  }
}
```

### 3. 位置持久化

```js
var STORE_KEY = '_nav_home_pos';

function loadPos() {
  try {
    var saved = JSON.parse(localStorage.getItem(STORE_KEY));
    if (saved && typeof saved.top === 'number') return saved;
  } catch (e) {}
  return { top: 16, left: 24 }; // 默认左上角
}

function savePos(top, left) {
  try {
    localStorage.setItem(STORE_KEY, JSON.stringify({ top, left }));
  } catch (e) {}
}
```

`try/catch` 包裹防止隐私模式下 `localStorage` 抛错导致脚本中断。

### 4. 安全初始化

```js
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', init);
} else {
  init(); // 脚本在 DOM 已就绪后加载（如 defer）时直接执行
}
```

---

## 复用到其他项目

复制 `nav.js` 到目标项目根目录，修改以下两处即可：

```js
// 1. 按钮链接目标
btn.href = '/';           // 改为目标 URL

// 2. 按钮文字
label.textContent = '知识地图';  // 改为目标名称
```

颜色如需更换，全局替换 `#d97757`（默认色）和 `#b8602a`（hover 色）。
