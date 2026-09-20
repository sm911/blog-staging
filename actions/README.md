# Staging action queue

Approve / Reject on the staging site open a GitHub issue:

- Title prefix `[STAGING-APPROVE]` → promote to production blog
- Title prefix `[STAGING-REJECT]` → revise using the reason body, then resubmit

SecurityMedic Content watches these issues (routine + chat) and:
1. Writes `approvals/APPROVALS.md`
2. Publishes or revises
3. Updates `drafts/manifest.json`
