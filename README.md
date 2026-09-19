# Autocampaign AI Documentation

Customer-facing help center for the Autocampaign AI customer-engagement platform, built with
[Mintlify](https://mintlify.com). Every page is grounded in the actual product
modules (backend `src/modules/*`, frontend `src/features/*`).

## Local preview

```bash
npm i -g mint      # Mintlify CLI
mint dev           # serves docs at http://localhost:3000
```

Validate links and structure before pushing:

```bash
mint broken-links
```

Publishing is automatic: pushing to the default branch deploys via the Mintlify
GitHub app.

## Information architecture

Navigation lives in [`docs.json`](./docs.json) as `navigation.tabs → groups → pages`.
Each nav leaf maps to one `.mdx` file (extensionless, root-relative).

| Tab | Covers | Backing modules |
| --- | --- | --- |
| Getting Started | Onboarding checklist, workspace, team, auth (incl. Google/Microsoft sign-in), navigating the app | `auth`, `organization`, `invitation`, `onboarding`, `user/role/permission`, `search` |
| Channels | SMS / Email / WhatsApp / Advertising + providers (Twilio, Telnyx, email domains & senders, Google/Meta Ads) | `channel-core`, `sms-channel`, `email-channel`, `whatsapp-channel`, `advertising` |
| Compliance | A2P 10DLC, toll-free, opt-in, opt-out | `channels` 10DLC, `opt-in`, `opt-out` |
| CRM | Contacts, import, custom fields, tags, segments; opportunities & pipelines; lead forms, join links, join keywords | `contacts`, `contact-import`, `tags`, `segments`, `opportunities`, `lead-forms`, `join-links`, `join-keywords` |
| Communication | Unified inbox, quick messages, calls, tickets, website chat widget | `inbox`, `quick-messages`, `voice-channel`, `tickets`, `chat-widget` |
| Marketing | Campaigns, sequences, experiments, polls, text links; templates & template library | `campaigns`, `sequences`, `polls`, `short-links`, `*-templates`, `marketplace`, `media-library` |
| Automation & AI | Workflow builder, module builder, AI Employees, knowledge base | `workflows`, `module-builder`, `ai-agents`, `knowledge-base` |
| Scheduling | Calendar, meeting types, availability, bookings, integrations | `scheduling`, `calendar-integrations` |
| Analytics & Billing | Dashboard, custom dashboards, reports, campaign analytics, attribution, notifications; plans & trials, credits | `dashboard`, `dashboards`, `analytics`, `notifications`, `platform-billing` |
| Agency | Agency console: clients, setups, branding, pricing & rebilling | `agency` |
| Developers | API keys, webhooks, API reference | `api-keys`, `webhooks` |
| Support | FAQ, troubleshooting, release notes | — |

## Page template

Every module page follows the same shape so customers learn one layout:

1. **Overview** — what it is, when to use it (+ difficulty/time hints).
2. **Before you start** — prerequisites and permissions.
3. **How-to** — `<Steps>` grounded in the real UI route.
4. **FAQ** — `<AccordionGroup>`.
5. **Troubleshooting** — common errors and fixes.

## Screenshots

Images are referenced as `/images/<section>/<name>.png` inside `<Frame>` blocks.
Drop real captures into `images/` matching those paths and they resolve. Pages
currently ship without images; add them incrementally — see `images/README.md`.

## Content status

Pages carrying a `This guide is being expanded` `<Note>` are structural stubs
awaiting full content. Track progress by phase in the project plan.
