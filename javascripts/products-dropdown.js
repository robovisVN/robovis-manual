// Native <details> keeps the product selector usable without JavaScript.
// One delegated handler also works after Material instant navigation.
(() => {
  if (window.__robovisProductDropdown) return;
  window.__robovisProductDropdown = true;
  const openMenus = () => document.querySelectorAll('.rv-products__disclosure[open]');
  const close = (menu, restoreFocus = false) => {
    menu.open = false;
    if (restoreFocus) menu.querySelector('summary').focus();
  };
  document.addEventListener('click', event => {
    openMenus().forEach(menu => {
      if (!menu.contains(event.target) || event.target.closest('a[href]')) close(menu);
    });
  });
  document.addEventListener('focusin', event => {
    openMenus().forEach(menu => { if (!menu.contains(event.target)) close(menu); });
  });
  document.addEventListener('keydown', event => {
    const menu = event.target.closest('.rv-products__disclosure');
    if (!menu) return;
    if (event.key === 'Escape' && menu.open) {
      event.preventDefault();
      close(menu, true);
    } else if (['ArrowDown', 'ArrowUp'].includes(event.key)) {
      event.preventDefault();
      menu.open = true;
      const links = Array.from(menu.querySelectorAll('a[href]'));
      if (!links.length) return;
      const index = links.indexOf(document.activeElement);
      const next = event.key === 'ArrowDown' ? (index + 1) % links.length : (index <= 0 ? links.length - 1 : index - 1);
      links[next].focus();
    }
  });
  window.addEventListener('resize', () => openMenus().forEach(menu => close(menu)));
})();
