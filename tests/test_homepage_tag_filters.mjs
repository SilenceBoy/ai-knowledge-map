import assert from 'node:assert/strict';
import { createRequire } from 'node:module';

const require = createRequire(import.meta.url);
const { chromium } = require('playwright');

const baseUrl = process.env.TEST_BASE_URL || 'http://127.0.0.1:8877';
const executablePath = process.env.PLAYWRIGHT_CHROME_PATH
  || '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';
const browser = await chromium.launch({ headless: true, executablePath });

try {
  const page = await browser.newPage({ viewport: { width: 1280, height: 900 } });
  const pageErrors = [];
  const failedResources = [];
  page.on('pageerror', error => pageErrors.push(error.message));
  page.on('response', response => {
    if (response.status() >= 400) {
      failedResources.push(`${response.status()} ${response.url()}`);
    }
  });
  await page.goto(baseUrl, { waitUntil: 'networkidle' });

  if (process.env.TEST_SCREENSHOT) {
    await page.screenshot({ path: process.env.TEST_SCREENSHOT, fullPage: true });
  }

  const visibleHrefs = () => page
    .locator('.card:not([data-hidden])')
    .evaluateAll(cards => cards.map(card => card.getAttribute('href')).sort());

  assert.equal((await visibleHrefs()).length, 21, '默认应展示全部 21 张卡片');

  await page.getByRole('button', { name: /课件PPT/ }).click();
  assert.deepEqual(await visibleHrefs(), [
    'map/ai/ai-fullstack-dev-talk.html',
    'map/ai/ai-requirement-to-launch-talk-ppt.html',
    'map/ai/ai_eight_use_scenarios_offline/index.html',
    'map/ai/codex-mvp-workshop-ppt.html',
    'map/ai/single-point-replication-deck.html',
    'map/ai/课件-像甲方一样做AICoding-口播优化版.html',
    'map/growth/ai-era-super-individual-capabilities-deck.html',
  ]);

  await page.locator('[data-filter="ops"]').click();
  assert.equal((await visibleHrefs()).length, 0, '运营分类与课件PPT组合后应无结果');

  await page.getByRole('button', { name: /图文/ }).click();
  assert.deepEqual(await visibleHrefs(), [
    'map/ops/parasite-to-symbiosis.html',
  ]);

  await page.locator('#search-input').fill('穷');
  assert.equal((await visibleHrefs()).length, 1, '标签、分类与搜索应可组合');

  await page.setViewportSize({ width: 390, height: 844 });
  const hasHorizontalOverflow = await page.evaluate(
    () => document.documentElement.scrollWidth > window.innerWidth,
  );
  assert.equal(hasHorizontalOverflow, false, '移动端不应出现横向溢出');

  await page.goto(
    `${baseUrl}/map/growth/ai-era-super-individual-capabilities-deck.html`,
    { waitUntil: 'networkidle' },
  );
  const returnMapButton = page.locator('#_nav_home');
  assert.equal(await returnMapButton.count(), 1, '新增课件应显示左上角返回地图按钮');
  assert.equal(await returnMapButton.isVisible(), true, '返回地图按钮应可见');
  assert.match(await returnMapButton.innerText(), /知识地图/);

  const unexpectedResources = failedResources.filter(item => !item.endsWith('/favicon.ico'));
  assert.deepEqual(pageErrors, [], '页面不应产生 JavaScript 运行错误');
  assert.deepEqual(unexpectedResources, [], '页面资源不应加载失败');

  console.log('PASS: 标签、分类、搜索组合筛选及移动端布局正常');
} finally {
  await browser.close();
}
