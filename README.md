# Security Medic — Blog Staging (unlisted)

Unlisted review site for draft blog posts. **Not linked** from securitymedic.com or the public blog index pages.

## Live staging URL
https://sm911.github.io/blog-staging/

## Workflow
1. Draft lands under `blogs/<target-blog>/<category>/...html` using that blog’s house HTML format.
2. Appears on this staging index for Jim’s review.
3. On approve: record row in `approvals/APPROVALS.md` (timestamp, target blog, category, draft path).
4. Promote to the destination blog’s `main` (GitHub Pages production).
5. Mark staging entry as promoted (keep file for history or archive).

## Do not
- Link staging URLs from marketing sites or production blog indexes.
- Merge drafts to production blogs without an approval log entry.
