# Autocampaign AI documentation — project instructions

## About this project

- Customer help center for **Autocampaign AI**, a multi-channel customer-engagement platform (SMS, email, WhatsApp, voice calls, advertising) with a CRM, AI Employees, scheduling and an agency layer.
- Built on [Mintlify](https://mintlify.com); pages are MDX files with YAML frontmatter.
- Navigation and settings live in `docs.json` (`navigation.tabs → groups → pages`).
- Content must reflect the **actual app** — cross-check the product repo
  (`autocampaign-platform`: `backend/src/modules/*`, `frontend/src/features/*`, routes in `frontend/src/router/constant/routes.ts`, sidebar in `frontend/src/components/layout/navbar/app-sidebar.tsx`, English UI strings in `frontend/public/locales/en/`)
  before documenting a flow. Do not document features that are not shipped.
- Use the Mintlify MCP server, `https://mcp.mintlify.com`, to edit content and settings via MCP.
- Use the Mintlify docs MCP server, `https://www.mintlify.com/docs/mcp`, to query Mintlify usage.

## Terminology

- Say **workspace** / **organization** for the tenant, **member** for a user in it.
- Say **channel** (SMS, Email, Advertising), **provider** (Twilio, Telnyx, Gmail, …).
- Say **contact** (not "lead" unless referring to ad Lead Ads), **segment**, **campaign**.
- Say **AI Employee** (never "AI agent" or "bot"), **opportunity**, **pipeline**, **stage**, **sequence** (drip), **join keyword**, **lead form**.
- Say **WhatsApp** (channel) and **Calls** (voice); **Templates** and **Tags** are top-level pages, not under Settings.
- Say **opt-in** / **opt-out** (hyphenated); **A2P 10DLC** (not "10dlc").

## Style preferences

- Use active voice and second person ("you").
- Keep sentences concise — one idea per sentence.
- Use sentence case for headings.
- Bold for UI elements and navigation: Click **Settings → Channels**.
- Code formatting for file names, commands, paths, keywords (`STOP`), and code references.
- Every module page follows: Overview → Before you start → How-to (`<Steps>`) → FAQ (`<AccordionGroup>`) → Troubleshooting.

## Content boundaries

- Document customer-facing features only. Do not document platform-admin,
  internal billing margin config, or unreleased modules.
- Never include real API keys, tokens, phone numbers, or customer data in examples.
