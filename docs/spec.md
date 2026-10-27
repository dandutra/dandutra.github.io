# Portfolio spec

Daniel Dutra's portfolio at `dandutra.github.io`. It shows the work done so far to recruiters, for roles in this order of preference: full-stack, back-end, front-end, ops/support.

## Principle: respect the recruiter's time

Every rule below is checkable in review.

1. The first screen on a laptop answers four questions: who, which role, where, and how to reach Daniel or get the resume.
2. Every claim on a card has a link or a number behind it ("~480 tests", "11 ADRs"). No adjectives about Daniel ("passionate", "detail-oriented").
3. One idea per sentence. Card summaries are three sentences at most.
4. Dates sit in the same place and use one format: `May 2025 – Dec 2025`.
5. Page weight stays under budget: `index.html` + CSS + JS under 30 KB, plus one screenshot under 40 KB.
6. Nothing needs a click, hover or JS to be read. No `<details>`, tabs or modals.

## Constraints

- Plain HTML, CSS and JS on GitHub Pages, served from `main`. No build step and no framework. `package.json` holds dev tooling only.
- No on-scroll animations, videos or heavy images.
- English only. `<html lang="en">`, all text as real HTML text, so browser translation works for Portuguese-speaking family. Only the name and product names ("Jellyfin", "Casa Escala") get `translate="no"`.
- Accessibility: WCAG AA contrast in both themes, visible focus styles, a skip link, the theme toggle exposes its state with `aria-pressed`.

## Look

- Single column about 65 characters wide. System font stack; a monospace stack for tech tags.
- One muted blue accent for links. No icons except the theme toggle; links are text ("GitHub", "LinkedIn").
- Light and dark themes through CSS custom properties. The default follows `prefers-color-scheme`. A two-state toggle overrides it and saves the choice to `localStorage`.
- A small inline script in `<head>` applies the saved theme before first paint. Without JS the page follows the OS theme and the toggle is hidden.
- `<meta name="color-scheme" content="light dark">` and a `theme-color` meta per scheme.
- One shared `style.css` for both pages, so the second page loads from cache.
- New pages start as a Claude Design mock, built in HTML only after Daniel approves the look (per the `static-site` profile in agent-workflow).

## Pages

### `index.html`

1. **Header**: "Daniel Dutra", "Full-stack developer", Toronto, Canada. Status line: graduating Dec 2026, open to full-stack and back-end roles. Links: Resume, GitHub, LinkedIn, Email.
2. **Projects**
   - **Casa Escala**, subtitle "Shift-rotation scheduler for offshore crews". Repo `schedule-matcher`. One screenshot (WebP, under 40 KB, `loading="lazy"`, explicit width and height). Note: UI in Brazilian Portuguese, built for Brazilian offshore crews. Links: Live (`casaescala.me`); Source once the repo is public.
   - **Jellyfin Home Server**. Repo `jellyfin-home-server`. Framed as a self-hosted media server; the download stack is described neutrally ("automated media management behind a VPN kill switch").
   - Each card: summary of up to 3 sentences, a row of tech tags, links.
   - Closes with a "More on GitHub" link. No list of smaller repos.
3. **Experience**: HOOPP, Systems Developer (Co-op), May 2025 – Dec 2025, as one entry. Then one line: five years as a ship pilot (offshore and cargo), Rio de Janeiro.
4. **How I Work**: the AI-assisted workflow, with the `agent-workflow` repo as evidence. A section, not a project card.
5. **About**: the switch from ship pilot to developer, education, one clause on peer mentoring.
6. **Contact**: one line and the same links as the header. Doubles as the footer.

### `resume.html`

1. Header: name, headline, Toronto, contact links.
2. Experience: HOOPP, then one merged Ship Pilot entry for Oceanpact and Starnav (Feb 2019 – Mar 2024). The merged entry has two bullets: the PowerShell compliance automation first, then one bullet for the maritime work.
3. Projects: Casa Escala, Jellyfin Home Server.
4. Skills, grouped: Languages; Back-end and data; Front-end; Cloud and ops; Tools. This list is what ATS keyword matching reads.
5. Education: Diploma, Computer Programming, Seneca Polytechnic, Dec 2026, President's Honour List (Summer 2024, Fall 2024). B.S. Nautical Sciences, EFOMM, Rio de Janeiro, 2014 – 2019.
6. Leadership & Volunteering: Seneca Peer Mentoring, May 2026 – Aug 2026. Guided 6 new students to college resources such as career fairs, and helped them with program choices and time management, about 3 h/week.

No summary or objective paragraph. A print stylesheet makes "Save as PDF" produce a clean text-based PDF. The committed `resume.pdf` comes from that print and is linked next to the HTML version.

This is the general resume. Tailored versions for applications live outside this repo.

### Other files

- `404.html`: one line and a link home.
- Favicon: inline SVG of "DD".
- Open Graph and Twitter tags on both pages, with a 1200×630 preview image under 50 KB (name and headline).
- GoatCounter script, `async`. No cookies, so no consent banner. Daniel excludes his own browsers via `#toggle-goatcounter`.

## Content rules

- The copy is drafted in `docs/content-draft.md` and reviewed there before it goes into HTML. The unslop rules apply.
- Published: name, Toronto, `danieldutra06@gmail.com` (plain `mailto:`), GitHub `dandutra`, LinkedIn `https://www.linkedin.com/in/daniel-dutra-489718a2/`. Never a phone number.
- GPA is not shown until it is back to 4.0.
- HOOPP work is described at the level of services, APIs and outcomes. Never internal system names, data or hostnames.
- Casa Escala copy never includes the OAuth client ID, the backup bucket name or SSH host aliases.
- The old Node/Express/MySQL version of schedule-matcher is not mentioned.
- The job-hunting copilot is added only once its repo exists with a README.
- `index.html` and `resume.html` are maintained by hand. When one changes, check the other and regenerate `resume.pdf`.

## Checks

`npm run check` runs html-validate, `prettier --check`, Lighthouse CI with `budget.json` (the weight budget above), and lychee for links. CI runs the same command on every push and PR.

## Workflow

Each plan step is a branch and a PR. `/review` runs the Standards axis only. Daniel merges. UI fixes requested after a PR opens are counted for the "UI preview routes" trial in agent-workflow's `experiments.md`.

## Decisions

| Decision | Rejected | Why |
|---|---|---|
| One page plus a separate HTML resume page | Single page; per-project pages | Recruiters skim one page. The resume page prints to PDF and links straight from an application. |
| Hand-maintained HTML for both pages | Build script from one data file; JS rendering from JSON | The overlap is a few lines that change rarely. JS rendering breaks printing, translation and crawlers. |
| "How I Work" as a section | Project card for agent-workflow | The repo has no tests or CI. It reads as process, and a card would show it twice. |
| Copy before design | Mock with placeholder text | Text length drives card height and layout. |
| GoatCounter | No analytics | Shows whether application links get opened. About 3.5 KB, no cookies. |
| Live link before public source for Casa Escala | Wait for the scrub | The scrub is separate work in another repo and should not block launch. |

## Plan

Tracked as GitHub Issues on `dandutra/dandutra.github.io`. The repo exists with Pages on from `main`.

1. **Prerequisites (Daniel).** Create a GoatCounter account and site code. Take a signed-in Casa Escala screenshot.
2. **Tooling.** `package.json` with `npm run check`, `budget.json`, html-validate and prettier configs, lychee config, CI workflow.
3. **Copy draft.** Write all copy in `docs/content-draft.md`: header and status line, both project cards, HOOPP entry, How I Work, About, Contact, full resume. Daniel reviews.
4. **Design mock.** Claude Design mock of both pages in light and dark, using the approved copy. Daniel approves. Blocked by 3.
5. **Main page.** `index.html`, `style.css`, theme script and toggle, favicon, meta and Open Graph tags. Blocked by 2 and 4.
6. **Resume page.** `resume.html`, print styles, `resume.pdf`. Blocked by 5 (shared CSS).
7. **Assets and 404.** Preview image, compressed screenshot, `404.html`. Blocked by 1 and 5.
8. **Launch.** GoatCounter tag, Lighthouse pass within budget, browser-translation check to Portuguese, contrast check in both themes. Blocked by 6 and 7.
9. **Casa Escala source link.** Add once schedule-matcher is scrubbed and public. Blocked by the scrub in the schedule-matcher repo: rotate the OAuth client ID in `deploy/casaescala.env.example`, replace it with a placeholder, check git history.
10. **Copilot card.** Add once the job copilot repo exists with a README.
