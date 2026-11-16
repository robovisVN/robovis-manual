/* Reuse Material's search index, results and keyboard handling. */
document.querySelector('[data-rv-search]')?.addEventListener('click', () => {
  const toggle = document.querySelector('[data-md-toggle="search"]');
  const input = document.querySelector('[data-md-component="search-query"]');
  if (!toggle || !input) return;
  toggle.checked = true;
  toggle.dispatchEvent(new Event('change', { bubbles: true }));
  input.focus();
});
