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

Shift-rotation matcher for offshore crews

Casa Escala solves a real problem for 92 users as of October 2026: it finds and ranks the dates that work best for a group to meet, based on everyone’s offshore work rotations. I wished this had existed when I was planning my wedding. It's a Go monolith with server-rendered pages, SQLite with streaming backups, Google or email sign-in, and about 480 tests that run in CI against a real database.

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
- Administered Exchange hybrid, SharePoint, Power Platform, Microsoft Teams Rooms, and RingCentral services, and resolved staff support requests.
- Supported the organization-wide rollout of Copilot Studio and agents with user guides, licensing and support requests.

Before tech: ship pilot for 5 years on offshore subsea and cargo vessels, Rio de Janeiro (2019 – 2024).

## How I Work

I build with Claude Code, and the whole setup is public in [agent-workflow](https://github.com/dandutra/agent-workflow). I pressure-test ideas, reach a common understanding, slice the plan and implement each part test-first. I record every decision, gotcha and runbook in Google's [Open Knowledge Format](https://github.com/GoogleCloudPlatform/open-knowledge-format). Each pull request goes to three review agents, and a fourth checks their findings against the code before I see them. A hook blocks direct pushes to `main`, so every change goes through review. A new tool stays only if it passes a two-week productivity check recorded in the repo. All of this runs on a US$20/month Claude Pro plan, with no extra usage credits or paid API calls.

This site was planned the same way: [spec](https://github.com/dandutra/dandutra.github.io/blob/main/docs/spec.md).

## About

I like starting from a blank page. The part I enjoy most comes before the code: working out what the problem is, then deciding how the system should be shaped. I'm still learning to make those decisions well, and AI has made me faster at it. I ask Claude to argue against my plans and explain the trade-offs I missed, then I write down what I chose and why. I've never been good at accepting "that's just how it's done" as an answer, and a tool that keeps asking "why?" suits me.

Before tech, I spent five years as a ship pilot, holding vessels in position during offshore subsea operations. Writing PowerShell scripts to automate compliance work on board is what first got me into programming. I eventually traded the offshore life for a Computer Programming diploma at Seneca Polytechnic in Toronto, where I made the President's Honour List twice. In 2026 I also mentored six new students through Seneca's Peer Mentoring program.

Outside of work I'm usually doing CrossFit or playing video games. My only problem is that my game backlog grows faster than my project backlog.

## Contact

Email is the fastest way to reach me.

Email · LinkedIn · GitHub

---

# resume.html

**Daniel Dutra**
Full-stack developer · Toronto, Canada
Email · LinkedIn · GitHub
Download PDF · Back to the portfolio _(screen only, not printed)_

_Print preview, not a separate line: the print stylesheet adds each address after its label, as in "Email (danieldutra06@gmail.com) · LinkedIn (linkedin.com/in/daniel-dutra-489718a2) · GitHub (github.com/dandutra)"._

## Experience

### Systems Developer (Co-op), HOOPP (Healthcare of Ontario Pension Plan)

May 2025 – Dec 2025 · Toronto, ON

- Automated weekly quota monitoring for about 4,000 Exchange mailboxes using PowerShell, alerting the team at 80% capacity. Migrated the solution from Azure Functions to Azure Automation after repeated execution timeouts. It was still in production in October 2026, 10 months after my term ended.
- Automated the final step of RingCentral phone provisioning with PowerShell and Selenium, linking phones to Microsoft Teams. Deployed the script to an Azure Automation Hybrid Worker with step-by-step screenshot debugging.
- Established RingCentral API access for a department for the first time, configuring custom roles and a JWT-authenticated service account with call-log access for integration with Azure Data Factory.
- Developed a reusable Microsoft Graph app-registration validation function to verify shared credentials without triggering dependent onboarding, offboarding, or licensing automations. Renewed client secrets one automation at a time, because each stored its secret differently.
- Delivered onboarding, offboarding, licensing, and telephony automation changes through 2-week Agile sprints, contributing to Azure DevOps tickets, pull requests, code reviews, testing, and deployments. Adapted Azure Pipelines YAML for new automations, deployed through dev and production approval steps.
- Built a PnP PowerShell permission report covering about 5,000 SharePoint files and folders after HR raised concerns about pay-stub confidentiality. Combined it with access testing to confirm that users granted Limited Access could not open the files, which closed the question.
- Partnered with a senior engineer to restrict third-party Outlook and Teams add-ins in two phases: blocking new installations and removing existing ones. Researched and tested the approach, then presented the ServiceNow change request for approval before production deployment.
- Administered Exchange hybrid, SharePoint, Power Platform, Microsoft Teams Rooms, and RingCentral services for about 3,000 users, resolving more than 300 support tickets over 8 months.

### Ship Pilot, Oceanpact (subsea operations) and Starnav (cargo operations)

Feb 2019 – Mar 2024 · Rio de Janeiro, Brazil

- Automated regulatory compliance tasks with PowerShell scripts.
- Operated the Dynamic Positioning system during subsea operations, and led emergency drills with 100% compliance in safety audits.

## Projects

### Casa Escala, shift-rotation matcher for offshore crews · casaescala.me

- Go web app that ranks the dates that work best for a group to meet, from each member's work rotation. 92 users as of October 2026.
- Server-rendered pages with htmx, SQLite, Google OAuth and email sign-in.
- About 480 tests against a real database, CI on GitHub Actions, deployed to a VPS with Caddy, systemd and Litestream backups for under $10 a month.

### Jellyfin Home Server · github.com/dandutra/jellyfin-home-server

- Hardened Windows 11 media server with low-privilege services, a VPN kill switch and LAN-only key-based SSH.
- 11 decision records, 8 incident write-ups, and CI with shellcheck, PSScriptAnalyzer and gitleaks.

## Skills

- **Languages:** Go, JavaScript, PowerShell, Bash, SQL, C, C++
- **Back-end and data:** HTTP servers in Go, Node.js, Express, REST APIs, SQLite, Oracle, OAuth 2.0, JWT
- **Front-end:** HTML, CSS, JavaScript, htmx
- **Cloud and ops:** Azure Functions, Azure Automation, Azure Key Vault, Application Insights, Microsoft Graph, Exchange Online, SharePoint, Microsoft 365 administration, Linux (systemd, ufw), Caddy, Cloudflare, Windows administration
- **Tools:** Git, GitHub Actions, Azure DevOps, Azure Pipelines, Jenkins, Selenium, PnP PowerShell, ServiceNow, Claude Code, Copilot Studio

## Education

### Diploma, Computer Programming, Seneca Polytechnic

Expected Dec 2026 · Toronto, ON
President's Honour List, Summer 2024 and Fall 2024.

### B.S. Nautical Sciences, EFOMM (Merchant Marine Officers School)

Feb 2014 – Jan 2019 · Rio de Janeiro, Brazil

## Leadership & Volunteering

### Peer Mentor, Seneca Peer Mentoring

May 2026 – Aug 2026

- Guided 6 new students to college resources such as career fairs, and helped them choose program paths and manage their time, about 3 hours a week.
