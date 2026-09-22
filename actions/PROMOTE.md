# Promote after staging Approve

Triggered only by James’s staging Approve (dashboard → `[STAGING-APPROVE]` issue), **not** by chat.

## Required steps
1. Confirm draft `decision`/`status` is approved (or treat the new Approve issue as authority).
2. **Set article date = Approve day (America/New_York)** on the HTML before copying to the live blog:
   - Visible byline/meta date string (e.g. `September 22, 2026`)
   - `blog-control-meta` `date: YYYY-MM-DD` when present
   - `<meta name="date">` / OG article times if present
3. Confirm byline:
   - Name: **James Venuto**
   - Title/line: **Security Medic Consulting, LLC - AI Cyber Security and Privacy**
   - No “Jim Venuto”, “Hudson Valley CISO”, or category chips in the byline
4. Copy HTML to target repo `main` at the production path; update that blog’s index if required.
5. Update staging `drafts/manifest.json`: `status: promoted`, `live: true`, `productionUrl`, `decidedAt` if needed.
6. Append `approvals/APPROVALS.md` with Event at = Approve time (America/New_York) and Production URL.
7. Close the Approve issue; report the live URL.

## Helper
`scripts/set_approve_day_date.py` — given an HTML file and an Approve day (`YYYY-MM-DD` or `Month DD, YYYY`), rewrites common date slots. Run on the staging HTML (or a copy) **before** pushing to the live blog.
