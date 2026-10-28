// The inline script in <head> applies the saved theme before first paint; this file wires the toggles.
const root = document.documentElement;
const osDark = matchMedia("(prefers-color-scheme: dark)");
const toggles = document.querySelectorAll(".theme-toggle");

const isDark = () =>
  root.dataset.theme ? root.dataset.theme === "dark" : osDark.matches;

const syncToggles = () => {
  for (const button of toggles) {
    button.setAttribute("aria-pressed", String(isDark()));
  }
};

for (const button of toggles) {
  button.hidden = false;
  button.addEventListener("click", () => {
    const next = isDark() ? "light" : "dark";
    root.dataset.theme = next;
    try {
      localStorage.setItem("theme", next);
    } catch {
      // Storage can be blocked; the theme still applies for this visit.
    }
    syncToggles();
  });
}

osDark.addEventListener("change", syncToggles);
syncToggles();

// A popover stays open after an in-page link is followed, which would hide the section.
const menu = document.getElementById("site-menu");
if (menu) {
  for (const link of menu.querySelectorAll("a")) {
    link.addEventListener("click", () => menu.hidePopover());
  }
}
