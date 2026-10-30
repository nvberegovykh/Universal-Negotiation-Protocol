# Validation record — v0.1.0

Date: 2026-10-30.

Completed checks:

- The synthetic session passes the standard-library Python structural validator.
- All 25 adversarial/unit tests pass, covering extra rounds, duplicate representation, missing agency approval, divergent starting records, premature no-response declarations, missing consent, changed text, mismatched reviews/signatures, expired evidence, unresolved material doubts, incomplete stability windows, exclusions, and unresolved/emergency closure.
- Every local Markdown file link resolves.
- Both JSON files parse successfully.

The JSON Schema contract was authored alongside the example. A separate general-purpose JSON Schema validation was not completed because the available runtimes did not include the attempted `jsonschema` or `ajv/dist/2020` libraries. The Python script checks the documented cross-field invariants and is explicitly not a general JSON Schema validator.

No test verifies the existence or independence of an agency, actual professional competence, authentic signatures, source truth, absence of coercion, semantic neutrality, legal applicability, or durable peace. The example is synthetic, and this version has no independent professional certification.

Reproduce the executable checks from the repository root:

```sh
python3 scripts/validate.py examples/session.json
python3 -m unittest discover -s tests -v
```
