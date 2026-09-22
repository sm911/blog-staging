# Staging Approvals Log

| Event at (America/New_York) | Event | Draft id / path | Promote to blog | Category | Notes / reject reason | Promoted at | Production URL |
|---|---|---|---|---|---|---|---|
| 2026-09-22 17:05 America/New_York | reject | identity-perimeter-ir-8587-sep-2026 | leadership-blog | identity-governance | Staging Reject issue #6 — too narrowly federal/state + insider speak; revised & resubmitted same run (broader SMB / plain-language / MSP-friendly). Staging: https://sm911.github.io/blog-staging/blogs/leadership-blog/identity-perimeter-ir-8587-sep-2026.html | — | — |
| 2026-09-21 08:36 America/New_York | approve | cyber-insurance-renewal-banks-cpa-sep-2026 (SMB rewrite) | compliance-blog | us-state | Staging Approve issue #4 | 2026-09-21 08:36 America/New_York | https://sm911.github.io/compliance-blog/us-state/cyber-insurance-renewal-banks-cpa-sep-2026.html |
| 2026-09-20 12:35 America/New_York | approve | cyber-insurance-renewal-banks-cpa-sep-2026 (byline) | compliance-blog | us-state | Staging Approve issue #2 | 2026-09-20 12:35 America/New_York | https://sm911.github.io/compliance-blog/us-state/cyber-insurance-renewal-banks-cpa-sep-2026.html |
| 2026-09-20 12:35 America/New_York | approve | nydfs-risk-assessment-guidance-sep-2026 (byline) | compliance-blog | us-state | Staging Approve issue #3 | 2026-09-20 12:35 America/New_York | https://sm911.github.io/compliance-blog/us-state/nydfs-risk-assessment-guidance-sep-2026.html |
| 2026-09-20 12:25 America/New_York | approve | cyber-insurance-renewal-banks-cpa-sep-2026 | compliance-blog | us-state | Jim approved in chat | 2026-09-20 12:25 America/New_York | https://sm911.github.io/compliance-blog/us-state/cyber-insurance-renewal-banks-cpa-sep-2026.html |

## Convention
- **approve** — from staging UI / `[STAGING-APPROVE]` issue / chat “approve”
- **reject** — from staging UI with reason / `[STAGING-REJECT]` issue — agent revises and resubmits

## Byline & date on promote
- Visible byline name/title must be **James Venuto** / **Security Medic Consulting, LLC - AI Cyber Security and Privacy** (never “Jim Venuto”, “Hudson Valley CISO”, or category in the byline).
- **Event at** (Approve timestamp, America/New_York) is authoritative for the article publish date.
- On promote, set visible byline date + any meta/`blog-control-meta` `date:` to the **Approve calendar day** (America/New_York), not the draft/`stagedAt` day.
- Chat approval is not promote authority.
