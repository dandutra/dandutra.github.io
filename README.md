# dandutra.github.io

Daniel Dutra's portfolio. Plain HTML, CSS and JS, served by GitHub Pages from `main`.

Preview locally with `python3 -m http.server` and open http://localhost:8000. Decisions and rules are in [docs/spec.md](docs/spec.md).

Before each commit, run `npm install` once, then `npm run check`. It runs html-validate, `prettier --check`, Lighthouse CI against `budget.json`, and the lychee link checker. Lychee is not an npm package, so install it with `brew install lychee`. CI runs the same command on every push and pull request.
