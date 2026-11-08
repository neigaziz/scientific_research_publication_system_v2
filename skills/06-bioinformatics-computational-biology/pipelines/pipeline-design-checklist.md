# Bioinformatics pipeline design checklist

1. State biological question, organism, assay, platform, read layout and sample design.
2. Record raw files, checksums, sample IDs, metadata and access constraints.
3. Pin reference genome, annotation and database releases; retain checksums and provenance.
4. Record software versions, command lines, parameters and environment/container.
5. Define QC gates: read quality, contamination, mapping, coverage, duplication, variant/sample metrics and batch effects.
6. Define expected inputs/outputs and failure states for each step.
7. Use a workflow manager for multi-step pipelines; make steps restartable and logs auditable.
8. Validate with controls or benchmark material where feasible.
9. Preserve raw data; write derived data to separate versioned locations.
10. Report reference build, tools, parameters, limitations and resource environment.