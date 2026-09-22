# Security Medic — Blog Staging (unlisted)

Unlisted review site for draft blog posts. **Not linked** from securitymedic.com or the public blog index pages.

## Live staging URL
https://sm911.github.io/blog-staging/

## Byline (required on every draft)
- **Name:** James Venuto
- **Title/line:** Security Medic Consulting, LLC - AI Cyber Security and Privacy
- Do **not** use “Jim Venuto”, “Hudson Valley CISO”, or category chips in the byline.

## Publish date = Approve day
Blog publish/display date must equal the America/New_York calendar day **James Approves** the staging draft — not the research/draft day. Staging review drafts may keep a placeholder/draft date; on promote after Approve, overwrite visible byline date + meta/`blog-control-meta` date to that Approve day.

## Workflow
1. Draft lands under `blogs/<target-blog>/<category>/...html` using that blog’s house HTML format (with correct byline).
2. Appears on this staging index for James’s review (`status: review`).
3. On Approve: record row in `approvals/APPROVALS.md` (timestamp America/New_York, target blog, category, draft path).
4. Promote to the destination blog’s `main` (GitHub Pages production). **Set article date = Approve day** before/while publishing. See `actions/PROMOTE.md`.
5. Mark staging entry as promoted (`status: promoted`, `live: true`, `productionUrl`).

## Do not
- Link staging URLs from marketing sites or production blog indexes.
- Merge drafts to production blogs without an approval log entry.
- Treat chat “approve” as promote authority (staging Approve / `[STAGING-APPROVE]` only).
- Promote with the research/draft date left in the byline or meta.
