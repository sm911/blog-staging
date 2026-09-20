# Staging status model

| Field | Who sets it | Meaning |
|---|---|---|
| Awaiting / Approved / Rejected | **Jim** (Approve/Reject click + GitHub Action on issue) | His decision |
| Live (`status: promoted`) | **SecurityMedic Content** after publish | On the target blog |

Flow:
1. Draft staged → `status: review` (Awaiting)
2. Jim Approve → instant UI + `[STAGING-APPROVE]` issue → Action sets `status: approved`
3. Agent publishes → `status: promoted` (Live)
4. Jim Reject → `status: rejected` + reason → agent revises → back to `review`
