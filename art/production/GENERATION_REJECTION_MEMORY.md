# Asset generation rejection-memory policy

The production system records recurring, evidence-backed rejection patterns in `generation-rejection-ledger.json`.

The ledger may alter prompts, retry strategy and technical candidate selection. It **must not** mark assets DONE or bypass semantic review.

Current high-value lessons:
- front-load hard constraints in the short CLIP prompt;
- place descriptive/negative detail in T5 `prompt_2` to avoid CLIP truncation;
- keep a shared identity anchor across animations of the same role;
- adapt retries to the actual failure class rather than repeating the same generation;
- keep known family-specific building failure patterns available to future prompt compilers.
