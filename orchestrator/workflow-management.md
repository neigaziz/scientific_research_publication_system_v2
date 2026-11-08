# Workflow management

Lifecycle: `intake → plan → retrieve/design → data/QC → analyse → validate → interpret → write → integrity/reference audit → journal fit → submission (human approval) → peer review → revision`.

Every task records project/task IDs, objective, owner, required Skills, dependencies, input artifact IDs/versions, expected outputs, acceptance criteria, status, provenance, assumptions, limitations, conflicts and approvals.

Allowed states: `not_started`, `ready`, `in_progress`, `blocked`, `completed_with_warnings`, `validated`, `approved`, `failed`, `superseded`. A task is validated only when stated checks pass; human-gated tasks are approved only after a human approval record.

Parallelise independent retrieval, journal-policy checks and data intake checks. Do not write interpretation before validated analysis; do not submit before final approval. Preserve disagreements in a conflict record with positions, evidence, assumptions and decision owner.