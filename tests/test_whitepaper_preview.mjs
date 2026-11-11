import assert from 'node:assert/strict';
import { createRequire } from 'node:module';
import { join } from 'node:path';

const require = createRequire(import.meta.url);
const { chromium } = require('playwright');
const baseUrl = process.env.TEST_BASE_URL || 'http://127.0.0.1:8766';
const executablePath = process.env.PLAYWRIGHT_CHROME_PATH
  || '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';
const screenshotDir = process.env.TEST_SCREENSHOT_DIR;

const browser = await chromium.launch({ headless: true, executablePath });
try {
  const page = await browser.newPage({ viewport: { width: 1440, height: 1080 }, colorScheme: 'light' });
  const errors = [];
  page.on('pageerror', error => errors.push(error.message));
  page.on('response', response => {
    if (response.url().startsWith(baseUrl) && response.status() >= 400
      && !response.url().endsWith('/favicon.ico')) {
      errors.push(`${response.status()} ${response.url()}`);
    }
  });

  async function screenshot(name) {
    if (!screenshotDir) return;
    await page.evaluate(() => document.fonts.ready);
    await page.screenshot({ path: join(screenshotDir, name) });
  }

  const visibleEntries = () => page.locator('#paper-grid .paper-entry:not([hidden])');
  await page.goto(baseUrl);
  assert.equal(await page.getByRole('heading', { name: '精选白皮书' }).count(), 1);
  assert.equal(await page.locator('.paper-card').count(), 3);
  await screenshot('blog-home-desktop.png');

  await page.getByRole('link', { name: '浏览白皮书' }).click();
  assert.equal(new URL(page.url()).pathname, '/whitepapers/');
  assert.equal(await visibleEntries().count(), 6);
  await screenshot('whitepaper-library-desktop.png');

  await page.getByRole('combobox', { name: '白皮书排序' }).selectOption('recent');
  assert.match(await visibleEntries().first().innerText(), /AI 写真自动化白皮书/);
  await page.getByRole('combobox', { name: '白皮书排序' }).selectOption('featured');
  assert.match(await visibleEntries().first().innerText(), /AI 时代超级个体白皮书/);

  await page.getByRole('button', { name: 'AI 应用', exact: true }).click();
  assert.equal(await visibleEntries().count(), 1);
  assert.match(await visibleEntries().first().innerText(), /小白能学会的提示词技巧/);
  const search = page.getByRole('searchbox', { name: '搜索白皮书' });
  await search.fill('PROMPT 模板');
  assert.equal(await visibleEntries().count(), 1);
  await search.fill('跨 Agent');
  assert.equal(await visibleEntries().count(), 0);
  assert.equal(await page.locator('#paper-empty').isVisible(), true);
  await page.getByRole('button', { name: '清除筛选' }).click();
  assert.equal(await visibleEntries().count(), 6);
  assert.equal(await search.inputValue(), '');

  await page.getByRole('button', { name: 'AI 写真', exact: true }).click();
  assert.equal(await visibleEntries().count(), 2);
  await search.fill('三帧');
  assert.equal(await visibleEntries().count(), 1);
  assert.match(await visibleEntries().first().innerText(), /AI 写真自动化白皮书/);
  await search.fill('');
  await page.getByRole('button', { name: '全部', exact: true }).click();

  for (const [href, title] of [
    ['coding-methodology/', '编程方法论白皮书'],
    ['ai-portrait-creation/', 'AI 写真创作白皮书'],
    ['ai-portrait-automation/', 'Bin哥AI写真自动化白皮书'],
    ['task-ledger/v3.html', 'AI 任务账本白皮书'],
  ]) {
    await page.locator(`#paper-grid a[href="${href}"]`).click();
    assert.equal(new URL(page.url()).pathname, `/whitepapers/${href}`);
    assert.ok((await page.title()).includes(title));
    const sourceAnchors = page.locator('a[href^="#"]');
    const brokenAnchors = await sourceAnchors.evaluateAll(links => links
      .map(link => decodeURIComponent(link.hash.slice(1)))
      .filter(id => !document.getElementById(id)));
    assert.ok(await sourceAnchors.count() > 0, '原版应保留章节导航');
    assert.deepEqual(brokenAnchors, []);
    assert.ok(await page.locator('img[src^="data:"]').count() > 0, '原版应保留内嵌插图');
    await page.setViewportSize({ width: 390, height: 844 });
    assert.equal(await page.evaluate(() => document.documentElement.scrollWidth > innerWidth), false, href);
    await page.setViewportSize({ width: 1440, height: 1080 });
    const navigation = page.getByRole('navigation', { name: '白皮书导航' });
    if (href === 'task-ledger/v3.html') {
      await navigation.getByRole('link', { name: '阅读 v2.0' }).click();
      assert.equal(new URL(page.url()).pathname, '/whitepapers/task-ledger/');
      await page.getByRole('link', { name: /阅读 v3.0 原版网页/ }).click();
      assert.equal(new URL(page.url()).pathname, '/whitepapers/task-ledger/v3.html');
    }
    await navigation.getByRole('link', { name: /返回白皮书库/ }).click();
  }

  for (const [paper, sections] of [
    ['super-individual', 8],
    ['task-ledger', 49],
    ['prompting', 19],
  ]) {
    if (paper === 'task-ledger') {
      await page.locator('#paper-grid a[href="task-ledger/v3.html"]').click();
      await page.getByRole('link', { name: '阅读 v2.0' }).click();
    } else {
      await page.locator(`#paper-grid a[href="${paper}/"]`).click();
    }
    assert.equal(new URL(page.url()).pathname, `/whitepapers/${paper}/`);
    const chapterLinks = page.locator('.whitepaper-toc a');
    assert.equal(await chapterLinks.count(), sections);
    const brokenAnchors = await chapterLinks.evaluateAll(links => links
      .map(link => link.hash.slice(1))
      .filter(id => !document.getElementById(id)));
    assert.deepEqual(brokenAnchors, [], '目录应链接到正文标题');
    const lastHash = await chapterLinks.last().getAttribute('href');
    await chapterLinks.last().click();
    assert.equal(new URL(page.url()).hash, lastHash);
    if (paper === 'prompting') {
      const figures = page.locator('.whitepaper-body img');
      assert.equal(await figures.count(), 23, '提示词白皮书包含全部随文图');
      const failedImages = await figures.evaluateAll(async images => {
        const failed = [];
        for (const image of images) {
          image.loading = 'eager';
          try {
            await image.decode();
          } catch {
            failed.push(image.src);
          }
        }
        return failed;
      });
      assert.deepEqual(failedImages, [], '随文图应可加载和解码');
    }
    await page.setViewportSize({ width: 390, height: 844 });
    assert.equal(await page.evaluate(() => document.documentElement.scrollWidth > innerWidth), false);
    await page.setViewportSize({ width: 1440, height: 1080 });
    if (paper === 'super-individual') {
      await page.getByRole('link', { name: /查看原版演示/ }).click();
      await page.keyboard.press('ArrowRight');
      assert.equal(new URL(page.url()).hash, '#2', '保留原版演示翻页');
      await page.getByRole('link', { name: /返回白皮书库/ }).click();
    } else {
      await page.locator('.whitepaper-header').getByRole('link', { name: /返回白皮书库/ }).click();
    }
    assert.equal(new URL(page.url()).pathname, '/whitepapers/');
  }

  for (const width of [320, 390, 768]) {
    await page.setViewportSize({ width, height: 844 });
    for (const path of ['', '/whitepapers/']) {
      await page.goto(baseUrl + path);
      const overflow = await page.evaluate(() => document.documentElement.scrollWidth > innerWidth);
      assert.equal(overflow, false, `${path || '/'} 在 ${width}px 不应横向溢出`);
      if (width === 390) {
        await screenshot(path ? 'whitepaper-library-mobile.png' : 'blog-home-mobile.png');
      }
    }
  }
  assert.deepEqual(errors, [], '本地资源与页面脚本应无报错');
  console.log('PASS: 六份白皮书、主题与搜索、原版目录和插图、账本版本互链、窄屏布局');
} finally {
  await browser.close();
}
