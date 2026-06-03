(function () {
  // ── Google Fonts: Inter ──────────────────────────────────────
  if (!document.querySelector('link[href*="Inter"]')) {
    var link = document.createElement('link');
    link.rel = 'stylesheet';
    link.href = 'https://fonts.googleapis.com/css2?family=Inter:wght@500;600&display=swap';
    document.head.appendChild(link);
  }

  // ── Styles ───────────────────────────────────────────────────
  var style = document.createElement('style');
  style.textContent = [
    '#_nav_home {',
    '  position: fixed;',
    '  z-index: 9999;',
    '  display: inline-flex;',
    '  align-items: center;',
    '  gap: 6px;',
    '  padding: 0 18px;',
    '  height: 38px;',
    '  background: #d97757;',
    '  border: 1px solid #d97757;',
    '  border-radius: 99px;',
    '  color: #fff;',
    '  font: 600 13px/1 "Inter", ui-sans-serif, system-ui, -apple-system, sans-serif;',
    '  text-decoration: none;',
    '  white-space: nowrap;',
    '  user-select: none;',
    '  box-shadow: 0 2px 8px rgba(217, 119, 87, .15);',
    '  transition: background .2s, border-color .2s, box-shadow .2s, transform .2s;',
    '}',
    '#_nav_home:hover {',
    '  background: #b8602a;',
    '  border-color: #b8602a;',
    '  box-shadow: 0 6px 16px rgba(217, 119, 87, .35);',
    '}',
    '#_nav_home._dragging {',
    '  cursor: grabbing;',
    '  transform: scale(1.06);',
    '  box-shadow: 0 10px 28px rgba(217, 119, 87, .4);',
    '  transition: box-shadow .15s, transform .15s;',
    '}',
    '#_nav_home ._nav_arrow {',
    '  font-size: 12px;',
    '  display: inline-block;',
    '  transition: transform .2s;',
    '}',
    '#_nav_home:not(._dragging):hover ._nav_arrow { transform: translateX(-3px); }',
    '@media (prefers-color-scheme: dark) {',
    '  #_nav_home { box-shadow: 0 2px 8px rgba(217, 119, 87, .3); }',
    '  #_nav_home:hover { box-shadow: 0 6px 20px rgba(217, 119, 87, .5); }',
    '}',
    '[data-theme="dark"] #_nav_home { box-shadow: 0 2px 8px rgba(217, 119, 87, .3); }',
    '[data-theme="dark"] #_nav_home:hover { box-shadow: 0 6px 20px rgba(217, 119, 87, .5); }',
  ].join('\n');
  document.head.appendChild(style);

  // ── DOM ──────────────────────────────────────────────────────
  var btn = document.createElement('a');
  btn.id = '_nav_home';
  btn.href = '/';
  btn.setAttribute('aria-label', '返回首页知识地图');

  var arrow = document.createElement('span');
  arrow.className = '_nav_arrow';
  arrow.textContent = '←';

  var label = document.createElement('span');
  label.textContent = '知识地图';

  btn.appendChild(arrow);
  btn.appendChild(label);

  // ── Position (persist via localStorage) ─────────────────────
  var STORE_KEY = '_nav_home_pos';
  var DEFAULT = { top: 16, left: 24 };

  function clamp(val, min, max) { return Math.min(Math.max(val, min), max); }

  function applyPos(top, left) {
    btn.style.top  = top  + 'px';
    btn.style.left = left + 'px';
    btn.style.right  = '';
    btn.style.bottom = '';
  }

  function loadPos() {
    try {
      var saved = JSON.parse(localStorage.getItem(STORE_KEY));
      if (saved && typeof saved.top === 'number') return saved;
    } catch (e) {}
    return DEFAULT;
  }

  function savePos(top, left) {
    try { localStorage.setItem(STORE_KEY, JSON.stringify({ top: top, left: left })); } catch (e) {}
  }

  // ── Drag logic ───────────────────────────────────────────────
  var dragging = false;
  var startX, startY, startLeft, startTop;
  var moved = false;
  var DRAG_THRESHOLD = 4; // px，低于此视为点击

  function onDown(e) {
    var clientX = e.touches ? e.touches[0].clientX : e.clientX;
    var clientY = e.touches ? e.touches[0].clientY : e.clientY;
    dragging = true;
    moved = false;
    startX = clientX;
    startY = clientY;
    startLeft = btn.offsetLeft;
    startTop  = btn.offsetTop;
    e.preventDefault(); // 阻止文字选中
  }

  function onMove(e) {
    if (!dragging) return;
    var clientX = e.touches ? e.touches[0].clientX : e.clientX;
    var clientY = e.touches ? e.touches[0].clientY : e.clientY;
    var dx = clientX - startX;
    var dy = clientY - startY;

    if (!moved && Math.sqrt(dx * dx + dy * dy) > DRAG_THRESHOLD) {
      moved = true;
      btn.classList.add('_dragging');
    }

    if (!moved) return;

    var maxLeft = window.innerWidth  - btn.offsetWidth  - 8;
    var maxTop  = window.innerHeight - btn.offsetHeight - 8;
    var newLeft = clamp(startLeft + dx, 8, maxLeft);
    var newTop  = clamp(startTop  + dy, 8, maxTop);
    applyPos(newTop, newLeft);
  }

  function onUp(e) {
    if (!dragging) return;
    dragging = false;
    btn.classList.remove('_dragging');

    if (moved) {
      savePos(btn.offsetTop, btn.offsetLeft);
      // 阻止拖动结束后触发 click 跳转
      e.preventDefault();
      btn.addEventListener('click', stopOnce, true);
    }
  }

  function stopOnce(e) {
    e.preventDefault();
    e.stopPropagation();
    btn.removeEventListener('click', stopOnce, true);
  }

  btn.addEventListener('mousedown',  onDown, { passive: false });
  btn.addEventListener('touchstart', onDown, { passive: false });
  document.addEventListener('mousemove',  onMove);
  document.addEventListener('touchmove',  onMove, { passive: false });
  document.addEventListener('mouseup',  onUp);
  document.addEventListener('touchend', onUp);

  // ── Init ─────────────────────────────────────────────────────
  function init() {
    var pos = loadPos();
    applyPos(pos.top, pos.left);
    document.body.appendChild(btn);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
