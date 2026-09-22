# Staging status model

| Field | Who sets it | Meaning |
|---|---|---|
| Awaiting / Approved / Rejected | **James** (Approve/Reject click + GitHub Action on issue) | His decision |
| Live (`status: promoted`) | **SecurityMedic Content** after publish | On the target blog |

Flow:
1. Draft staged → `status: review` (Awaiting). Byline must already be James Venuto / Security Medic Consulting, LLC - AI Cyber Security and Privacy. Draft date may be placeholder.
2. James Approve → instant UI + `[STAGING-APPROVE]` issue → Action sets `status: approved`
3. Agent publishes per `PROMOTE.md` → **set article date = Approve day (America/New_York)** → `status: promoted` (Live)
4. James Reject → `status: rejected` + reason → agent revises → back to `review`

See also `PROMOTE.md` and `scripts/set_approve_day_date.py`.
