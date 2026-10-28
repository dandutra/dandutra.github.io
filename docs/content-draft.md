# Content draft

All page copy, for review before it goes into HTML. Rules: [spec.md](spec.md), "Principle" and "Content rules".

---

# index.html

## Header

**Daniel Dutra**
Full-stack developer · Toronto, Canada

Graduating in December 2026. Open to full-stack and back-end roles.

Resume · GitHub · LinkedIn · Email

## Projects

### Casa Escala
Shift-rotation scheduler for offshore crews

Casa Escala finds and ranks the dates that work best for a group to meet, based on everyone’s offshore work rotations. It is a Go monolith with server-rendered pages, SQLite with streaming backups, and Google or email sign-in. It has 92 users as of October 2026, and about 480 tests run in CI against a real database.

`Go` `SQLite` `htmx` `HTML/CSS/JS` `OAuth 2.0` `AWS SES` `Caddy` `systemd` `Litestream` `GitHub Actions`

Live site · Source (once public)
_UI in Brazilian Portuguese, built for Brazilian offshore crews._

[screenshot: `assets/casa-escala.webp`] Alt: "Casa Escala on a phone: the October 2026 calendar, with offshore days in red and days at home in green."

[screenshot: `assets/casa-escala-groups.webp`] Alt: "Casa Escala on a phone: the best days for a group to meet, led by Friday 30/10 with all six members available."

### Jellyfin Home Server
Self-hosted media server on a repurposed laptop

An old Dell laptop became a hardened Windows 11 media server for the home network, with nothing exposed to the internet. Jellyfin and automated media management run as low-privilege services, with downloads behind a VPN kill switch and admin access over key-only SSH. 11 decision records and 8 incident write-ups document the build, and CI runs shellcheck, PSScriptAnalyzer and secret scanning.

`PowerShell` `Bash` `Windows 11` `NSSM` `OpenSSH` `GitHub Actions` `gitleaks`

Source

More projects on GitHub

## Experience

### Systems Developer (Co-op) · HOOPP (Healthcare of Ontario Pension Plan)
May 2025 – Dec 2025 · Toronto

- Built production PowerShell automations on Azure Function Apps and Automation runbooks, including permission audits for sensitive SharePoint folders and mailbox-health alerts.
- Set up RingCentral API access with scoped roles and a JWT service account, so another team could pull call logs into Azure Data Factory.
- Administered Microsoft 365 and corporate telephony, and resolved staff support requests.
- Rolled out Copilot Studio and agents across the organization, and trained staff to use them.

Before tech: ship pilot for 5 years on offshore subsea and cargo vessels, Rio de Janeiro (2019 – 2024).

## How I Work

I build with Claude Code, and the whole setup is public in [agent-workflow](https://github.com/dandutra/agent-workflow). Every feature starts as a written plan that I question until the design is settled. Logic that matters is written test-first. Each pull request goes to three review agents, and a fourth checks their findings against the code before I see them. A hook blocks direct pushes to `main`, so every change goes through review. A new tool stays only if it passes a two-week productivity check recorded in the repo.

This site was planned the same way: [spec](https://github.com/dandutra/dandutra.github.io/blob/main/docs/spec.md).

## About

I spent five years as a ship pilot, holding vessels in position during offshore subsea operations. Writing PowerShell scripts to automate compliance work on board is what pulled me into software. I left that career to study Computer Programming at Seneca Polytechnic in Toronto, where I made the President's Honour List twice. In 2026 I also mentored six new Seneca students through the Peer Mentoring program.

## Contact

Email is the fastest way to reach me.

Email · LinkedIn · GitHub

---

# resume.html

**Daniel Dutra**
Full-stack developer · Toronto, Canada
Email · LinkedIn · GitHub

_Print preview, not a separate line: the print stylesheet adds each address after its label, as in "Email (danieldutra06@gmail.com) · LinkedIn (linkedin.com/in/daniel-dutra-489718a2) · GitHub (github.com/dandutra)"._

## Experience

### Systems Developer (Co-op), HOOPP (Healthcare of Ontario Pension Plan)
May 2025 – Dec 2025 · Toronto, ON

- Built production PowerShell automations on Azure Function Apps and Automation runbooks, including permission audits for sensitive SharePoint folders and mailbox-size alerts.
- Moved the mailbox-size check from Azure Functions to an Automation runbook after it timed out on the consumption plan.
- Built a reusable test function for a shared Microsoft Graph app registration, so its client secret can be rotated without running onboarding or offboarding automations.
- Set up RingCentral API access with scoped roles and a JWT service account, so another team could pull call logs into Azure Data Factory.
- Built a Selenium automation that connects provider phone numbers to Microsoft Teams, with step screenshots in debug mode.
- Administered Exchange Online, SharePoint, Teams and corporate telephony, and resolved staff support requests.
- Rolled out Copilot Studio and agents across the organization, and trained staff to use them.

### Ship Pilot, Oceanpact (subsea operations) and Starnav (cargo operations)
Feb 2019 – Mar 2024 · Rio de Janeiro, Brazil

- Automated regulatory compliance tasks with PowerShell scripts.
- Operated the Dynamic Positioning system during subsea operations, and led emergency drills with 100% compliance in safety audits.

## Projects

### Casa Escala, shift-rotation scheduler for offshore crews · casaescala.me
- Go web app that ranks the dates that work best for a group to meet, from each member's work rotation. 92 users as of October 2026.
- Server-rendered pages with htmx, SQLite, Google OAuth and email sign-in.
- About 480 tests against a real database, CI on GitHub Actions, deployed to a VPS with Caddy, systemd and Litestream backups for under $10 a month.

### Jellyfin Home Server · github.com/dandutra/jellyfin-home-server
- Hardened Windows 11 media server with low-privilege services, a VPN kill switch and LAN-only key-based SSH.
- 11 decision records, 8 incident write-ups, and CI with shellcheck, PSScriptAnalyzer and gitleaks.

## Skills

- **Languages:** Go, JavaScript, PowerShell, Bash, SQL, C, C++
- **Back-end and data:** HTTP servers in Go, Node.js, Express, REST APIs, SQLite, MySQL, Oracle, OAuth 2.0, JWT
- **Front-end:** HTML, CSS, JavaScript, htmx
- **Cloud and ops:** Azure Functions, Azure Automation, Microsoft Graph, Microsoft 365 administration, Linux (systemd, ufw), Caddy, Cloudflare, Windows administration
- **Tools:** Git, GitHub Actions, Azure DevOps, Jenkins, Selenium, Figma, Claude Code, Copilot Studio

## Education

### Diploma, Computer Programming, Seneca Polytechnic
Expected Dec 2026 · Toronto, ON
President's Honour List, Summer 2024 and Fall 2024.

### B.S. Nautical Sciences, EFOMM (Merchant Marine Officers School)
Feb 2014 – Jan 2019 · Rio de Janeiro, Brazil

## Leadership & Volunteering

### Peer Mentor, Seneca Peer Mentoring
May 2026 – Aug 2026
- Guided 6 new students to college resources such as career fairs, and helped them choose program paths and manage their time.
