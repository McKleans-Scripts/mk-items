(() => {
  const $ = (selector) => document.querySelector(selector);
  const grid = $('#grid');
  const search = $('#search');
  const categoryBar = $('#categories');
  const sort = $('#sort');
  const selected = new Set();
  let items = [];
  let activeCategory = 'All';
  let toastTimer;

  const titleCase = (value) => value.replace(/[_-]+/g, ' ').replace(/\b\w/g, (letter) => letter.toUpperCase());
  const imageUrl = (path) => path.split('/').map(encodeURIComponent).join('/');

  function filteredItems() {
    const term = search.value.trim().toLocaleLowerCase();
    return items.filter((item) => {
      const matchesCategory = activeCategory === 'All' || item.category === activeCategory;
      const matchesTerm = !term || `${item.name} ${item.filename} ${item.category}`.toLocaleLowerCase().includes(term);
      return matchesCategory && matchesTerm;
    }).sort((a, b) => {
      if (sort.value === 'name-desc') return b.name.localeCompare(a.name);
      if (sort.value === 'category') return a.category.localeCompare(b.category) || a.name.localeCompare(b.name);
      return a.name.localeCompare(b.name);
    });
  }

  function renderCategories() {
    const categories = ['All', ...new Set(items.map((item) => item.category).sort((a, b) => a.localeCompare(b)))];
    categoryBar.replaceChildren(...categories.map((category) => {
      const button = document.createElement('button');
      button.type = 'button';
      button.className = `category-chip${activeCategory === category ? ' active' : ''}`;
      button.textContent = category;
      button.setAttribute('aria-pressed', String(activeCategory === category));
      button.addEventListener('click', () => { activeCategory = category; renderCategories(); render(); });
      return button;
    }));
    $('#total-count').textContent = items.length.toLocaleString();
    $('#category-count').textContent = (categories.length - 1).toLocaleString();
  }

  function render() {
    const visible = filteredItems();
    $('#result-count').textContent = `${visible.length.toLocaleString()} ${visible.length === 1 ? 'image' : 'images'}${activeCategory !== 'All' ? ` in ${activeCategory}` : ''}`;
    $('#empty-state').hidden = visible.length > 0;
    grid.hidden = visible.length === 0;
    grid.replaceChildren(...visible.map((item) => {
      const card = document.createElement('article');
      const isSelected = selected.has(item.path);
      card.className = `image-card${isSelected ? ' selected' : ''}`;
      card.setAttribute('role', 'checkbox');
      card.setAttribute('aria-checked', String(isSelected));
      card.setAttribute('tabindex', '0');
      card.title = `${item.name} · ${item.category}`;
      const stage = document.createElement('div'); stage.className = 'image-stage';
      const image = document.createElement('img'); image.src = imageUrl(item.path); image.alt = item.name; image.loading = 'lazy'; image.decoding = 'async';
      image.addEventListener('error', () => { image.alt = `${item.name} (image unavailable)`; image.style.opacity = '.25'; });
      const check = document.createElement('span'); check.className = 'check'; check.setAttribute('aria-hidden', 'true'); check.textContent = isSelected ? '✓' : '';
      stage.append(image, check);
      const meta = document.createElement('div'); meta.className = 'image-meta';
      const name = document.createElement('div'); name.className = 'image-name'; name.textContent = item.name;
      const category = document.createElement('div'); category.className = 'image-category'; category.textContent = item.category;
      meta.append(name, category); card.append(stage, meta);
      const toggle = () => { selected.has(item.path) ? selected.delete(item.path) : selected.add(item.path); updateSelection(); render(); };
      card.addEventListener('click', toggle);
      card.addEventListener('keydown', (event) => { if (event.key === 'Enter' || event.key === ' ') { event.preventDefault(); toggle(); } });
      return card;
    }));
  }

  function updateSelection() {
    const count = selected.size;
    $('#selection-bar').hidden = count === 0;
    $('#selected-count').textContent = count.toLocaleString();
    $('#download-size').textContent = `(${count.toLocaleString()})`;
  }

  function showToast(message) {
    const toast = $('#toast'); toast.textContent = message; toast.classList.add('show');
    clearTimeout(toastTimer); toastTimer = setTimeout(() => toast.classList.remove('show'), 2800);
  }

  function makeItemCodeDocs(chosen) {
    const used = new Set();
    const entries = chosen.map((item) => {
      const stem = item.filename.replace(/\.[^.]+$/, '');
      let key = stem.toLowerCase().replace(/[^a-z0-9_]+/g, '_').replace(/^_+|_+$/g, '') || 'item';
      if (used.has(key)) key = `${item.category.toLowerCase().replace(/[^a-z0-9_]+/g, '_')}_${key}`;
      const baseKey = key;
      let suffix = 2;
      while (used.has(key)) key = `${baseKey}_${suffix++}`;
      used.add(key);
      const label = item.name.replace(/["'\\]/g, '').trim() || titleCase(stem);
      const image = item.archiveName || item.filename;
      return { key, label, image };
    });

    const qb = [
      '# QB-Core Item Codes',
      '',
      'Add these entries to `qb-core/shared/items.lua`. Update weight, useable, and other settings to fit your server.',
      'All selected images are together in `images/`. Duplicate filenames are prefixed with their category. The same images are organized under `categories/`.',
      'Copy the matching image files from `images/` into your inventory image folder.',
      '',
      '```lua',
      ...entries.map(({ key, label, image }) => `['${key}'] = { ['name'] = '${key}', ['label'] = '${label}', ['weight'] = 100, ['type'] = 'item', ['image'] = '${image}', ['unique'] = false, ['useable'] = false, ['shouldClose'] = true, ['description'] = '${label}', ['combinable'] = nil },`),
      '```',
      ''
    ].join('\n');
    const ox = [
      '# ox_inventory Item Codes',
      '',
      'Add these entries to your ox_inventory items definition. Update weight and other settings to fit your server.',
      'All selected images are together in `images/`. Duplicate filenames are prefixed with their category. The same images are organized under `categories/`.',
      'Copy the matching image files from `images/` into your inventory image folder.',
      '',
      '```lua',
      ...entries.map(({ key, label, image }) => `['${key}'] = { label = '${label}', weight = 100, stack = true, close = true, description = '${label}', client = { image = '${image}' } },`),
      '```',
      ''
    ].join('\n');
    return { qb, ox };
  }

  search.addEventListener('input', render);
  sort.addEventListener('change', render);
  $('#select-visible').addEventListener('click', () => {
    const visible = filteredItems();
    if (visible.length && visible.every((item) => selected.has(item.path))) visible.forEach((item) => selected.delete(item.path));
    else visible.forEach((item) => selected.add(item.path));
    updateSelection(); render();
  });
  $('#clear-selection').addEventListener('click', () => { selected.clear(); updateSelection(); render(); });
  $('#download-zip').addEventListener('click', async (event) => {
    if (!selected.size) return;
    if (!window.JSZip) { showToast('ZIP tool did not load. Refresh and try again.'); return; }
    const button = event.currentTarget; button.disabled = true; button.firstChild.textContent = 'Preparing… ';
    try {
      const zip = new JSZip();
      const chosen = items.filter((item) => selected.has(item.path));
      const usedFilenames = new Set();
      for (const item of chosen) {
        let filename = item.filename;
        if (usedFilenames.has(filename.toLocaleLowerCase())) {
          filename = `${item.category.replace(/[^a-z0-9_-]+/gi, '_')}_${item.filename}`;
        }
        const original = filename;
        let suffix = 2;
        while (usedFilenames.has(filename.toLocaleLowerCase())) {
          const dot = original.lastIndexOf('.');
          filename = dot > 0 ? `${original.slice(0, dot)}_${suffix++}${original.slice(dot)}` : `${original}_${suffix++}`;
        }
        item.archiveName = filename;
        usedFilenames.add(filename.toLocaleLowerCase());
      }
      const results = await Promise.all(chosen.map(async (item) => {
        const response = await fetch(imageUrl(item.path));
        if (!response.ok) throw new Error(item.filename);
        return [item, await response.blob()];
      }));
      for (const [item, blob] of results) {
        zip.file(`images/${item.archiveName}`, blob);
        zip.file(`categories/${item.path}`, blob);
      }
      const docs = makeItemCodeDocs(chosen);
      zip.file('QB-Items.md', docs.qb);
      zip.file('OX-Items.md', docs.ox);
      const content = await zip.generateAsync({ type: 'blob' });
      const link = document.createElement('a'); link.href = URL.createObjectURL(content); link.download = 'mk-items-images.zip'; link.click();
      setTimeout(() => URL.revokeObjectURL(link.href), 1000);
      showToast(`Downloaded ${chosen.length} ${chosen.length === 1 ? 'image' : 'images'}.`);
    } catch (error) {
      console.error(error); showToast(`Could not download ${error.message || 'one or more images'}.`);
    } finally { button.disabled = false; button.firstChild.textContent = '↓ Download ZIP '; }
  });

  document.addEventListener('keydown', (event) => {
    if ((event.metaKey || event.ctrlKey) && event.key.toLowerCase() === 'k') { event.preventDefault(); search.focus(); }
    if (event.key === 'Escape' && document.activeElement === search) { search.value = ''; render(); search.blur(); }
  });

  fetch('catalog.json').then((response) => { if (!response.ok) throw new Error('catalog.json unavailable'); return response.json(); }).then((catalog) => {
    items = catalog.map((item) => ({ ...item, name: item.name || titleCase(item.filename.replace(/\.[^.]+$/, '')) }));
    renderCategories(); render();
  }).catch((error) => { console.error(error); $('#result-count').textContent = ''; $('#load-error').hidden = false; });
})();
