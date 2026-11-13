// Menu dạng accordion cho Material for MkDocs.
// Khi mở một nhóm, các nhóm cùng cấp đang mở sẽ tự đóng.

document.addEventListener("change", function (event) {
  const openedToggle = event.target;

  if (
    !openedToggle.matches(".md-nav__item--nested > input.md-nav__toggle") ||
    !openedToggle.checked
  ) {
    return;
  }

  const openedItem = openedToggle.parentElement;
  const siblingList = openedItem?.parentElement;

  if (!siblingList) {
    return;
  }

  Array.from(siblingList.children).forEach(function (siblingItem) {
    if (
      siblingItem === openedItem ||
      !siblingItem.classList.contains("md-nav__item--nested")
    ) {
      return;
    }

    siblingItem
      .querySelectorAll("input.md-nav__toggle:checked")
      .forEach(function (toggle) {
        toggle.checked = false;
      });
  });
});
