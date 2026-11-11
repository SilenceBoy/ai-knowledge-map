const toolbar = document.querySelector('.library-toolbar');
const search = document.getElementById('paper-search');
const sort = document.getElementById('paper-sort');
const topicButtons = [...toolbar.querySelectorAll('[data-filter-topic]')];
const grid = document.getElementById('paper-grid');
const entries = [...grid.querySelectorAll('.paper-entry')];
const count = document.getElementById('paper-count');
const empty = document.getElementById('paper-empty');
let topic = 'all';

function render() {
  const words = search.value.trim().toLowerCase().split(/\s+/).filter(Boolean);
  const orderedEntries = sort.value === 'recent'
    ? [...entries].sort((a, b) => b.dataset.date.localeCompare(a.dataset.date))
    : entries;
  let visible = 0;

  for (const entry of orderedEntries) {
    const text = (entry.querySelector('.paper-copy').textContent + ' ' + entry.dataset.keywords).toLowerCase();
    const matches = (topic === 'all' || topic === entry.dataset.topic)
      && words.every(word => text.includes(word));
    entry.hidden = !matches;
    if (matches) visible += 1;
    grid.append(entry);
  }

  for (const button of topicButtons) {
    button.setAttribute('aria-pressed', String(button.dataset.filterTopic === topic));
  }
  count.textContent = `显示 ${visible} / ${entries.length} 份白皮书`;
  grid.hidden = visible === 0;
  empty.hidden = visible > 0;
}

search.addEventListener('input', render);
sort.addEventListener('change', render);
for (const button of topicButtons) {
  button.addEventListener('click', () => {
    topic = button.dataset.filterTopic;
    render();
  });
}
document.getElementById('paper-reset').addEventListener('click', () => {
  topic = 'all';
  search.value = '';
  render();
  search.focus();
});

toolbar.hidden = false;
render();
