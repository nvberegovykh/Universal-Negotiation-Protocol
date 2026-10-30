# Universal Negotiation Protocol — normative draft

Version: 0.1.0. Status: research proposal. Date: 2026-10-30.

Within this proposal, **MUST** describes a conformance requirement, **SHOULD** a reasoned default that may be varied with an explanation in the mandate, and **MAY** an option. These words confer no external legal authority.

## 1. Purpose and boundary

The purpose is persistent coexistence: each actor can continue to exist, retain agency and a self-defined identity, and interact under explicit reciprocal boundaries. Cooperation is available when voluntarily chosen. Cultural convergence, compelled confession, and unanimous interpretations of history are not success criteria.

A completed procedure can produce accepted terms, a limited agreement, or a precise record of unresolved disagreement. A completed round does not establish that its claims are true or its settlement will last.

The framework MUST operate within applicable law and the legal obligations identified in the conflict guidelines. Parties cannot use a protocol score, agency opinion, or mutual consent as a blanket waiver of the rights of people outside the negotiation. This draft does not determine the law applicable to any actual conflict.

## 2. Roles

| Role | Authority | Boundary |
|---|---|---|
| Side | Defines its mandate and authorizes its representative | Cannot multiply seats through controlled proxies |
| Representative | One active decision seat per side; submits and ratifies within mandate | Cannot bind others or exceed delegated authority |
| Independent agency | Prepares guidelines, administers records, commissions review | Cannot impose settlement or suppress evidence |
| Professional evaluator | Assesses a defined domain and signs reasons | Cannot certify outside competence or replace consent |
| SI/AI adviser | Retrieves, compares, calculates, tests, and documents uncertainty | Has no seat, signature authority, or autonomous enforcement power |
| Affected stakeholder | Supplies needs, evidence, objections, and impact testimony through defined channels | Inclusion does not automatically confer a conflicting side's mandate |
| Monitor | Checks accepted commitments against specified indicators | Cannot alter commitments through interpretation |

Every recognized side MUST have exactly one active representative. Substitution transfers the existing seat and its remaining opportunity; it does not restart the round. The agency MUST document selection, challenge, and replacement rules before entry.

## 3. Entry contract

Before beginning a cycle, every side MUST explicitly authorize the same version of:

- the side roster, representative mandates, and affected-stakeholder channels;
- the independent agency, its funding disclosures, evaluators, and replacement process;
- the conflict guidelines, scope, common terminology, and interpretation arrangements;
- a starting record, accessible evidence snapshot, and a set of initial proposals;
- clocks, time zones, time budgets, accommodations, equality of access, and the single correction round;
- proposal limits, doubt limits, materiality tests, stability thresholds, and evidence freshness rules;
- the procedure for neutral wording, exact-text ratification, verification, and complaints;
- any temporary fallback commitments, their duration, and termination conditions.

The entry contract MUST be recorded by content digest and authorization evidence. Failure to agree on it produces `not_started`; the agency MUST NOT invent approval.

The entry contract is version-locked for this cycle. Material changes require a separately authorized cycle. The closure checkpoint is the entry reference frame, not a rollback of history or accepted changes.

## 4. Evidence and professional SI evaluation

Every initial proposal and material revision MUST have an evaluation record tied to its exact content digest and the approved guideline version before becoming eligible for adoption. Pending submissions remain visible in the record with `review_pending`; lack of review MUST NOT be presented as approval.

Each evaluation MUST identify accountable human professionals, domain competence, agency authorization, SI/AI tools used or their unavailability, evidence dates, data gaps, methods, uncertainties, affected-party impacts, and a reasoned disposition. See [Expert evaluation](docs/EXPERT-EVALUATION.md).

“Supported by evaluation” means accompanied by a traceable assessment. An assessment may find a proposal unsupported, infeasible, inadmissible, or insufficiently evidenced. It is not a requirement that the expert endorse every submission.

For adoption, the specified professional review gates MUST pass. A `conditional` disposition is eligible only when every recorded pre-adoption condition has verifiable satisfaction evidence. These are agreed rules applied with reasons, not discretionary agency vetoes. A challenge to their application is logged and receives independent review under the pre-agreed timetable.

## 5. Doubt resolution and one correction round

### 5.1 Common starting record

All representatives MUST receive the same substantive record in an accessible form. Protected evidence may be subject to agreed confidentiality arrangements, but material conclusions must have enough accessible support to be challengeable. Relevant information gaps MUST be explicit.

Initial proposals are evaluated before the correction window. Clarification may ask what a statement means, identify a contradiction, request a source, or distinguish a value from a factual claim. It MUST NOT silently revise a party's commitments.

### 5.2 Bounded clarification

The agency maintains a doubt register with a claim, category, materiality, evidence, response owner, and disposition. Repeated questions may be linked to the existing entry; distinct material concerns must remain visible.

Clarification ends when the pre-agreed input stability conditions are met or its deadline arrives. Unresolved doubts remain in the record. Silence, fatigue, resource limits, or repetition do not establish truth.

### 5.3 Exactly one opportunity

Each side receives exactly one correction opportunity against the common record. The preferred method is sealed simultaneous submission and a common release time. A sequential alternative requires pre-agreed equal timing and explicit mitigation of the last-speaker advantage.

Each opportunity ends in one of three dispositions:

- `revised`: one final version submitted;
- `retained`: the side explicitly retains its starting position;
- `no_response`: its opportunity expires without a submission.

One complete round means all opportunities have been disposed of exactly once. It does not mean all sides were forced to change or that silence implies consent. Replacing a representative, adding an advisor, or renaming a proposal MUST NOT create another correction opportunity.

### 5.4 Final review

The final versions receive version-specific expert evaluations. A failed review does not create an extra revision round. The record may close unresolved or consider only a previously evaluated, compatible package explicitly ratified by every side whose commitments or protected interests it changes.

New obligations cannot be assembled by combining individually accepted clauses unless their combination has also been evaluated and accepted. Dependencies and third-party impacts matter.

## 6. Logic-time stability

The mathematical definition and its limits are in [Mathematical model](docs/MATHEMATICAL-MODEL.md). Stability MUST be an operational, scope-specific test established before the cycle. At minimum:

1. Every correction opportunity is complete.
2. The candidate's content and material interpretation have remained fixed for the agreed observation window.
3. Every required evaluation addresses that candidate version and passes the agreed criteria.
4. Evidence is fresh enough for the relevant domain at closure; gaps are recorded.
5. No unresolved doubt classified as material to that candidate remains.
6. No predefined legal, feasibility, or immediate safety exclusion is triggered.

Value disagreements outside the package may persist. Stability of the package does not establish agreement on those values.

If the deadline arrives before these conditions are met, the outcome MUST be `closed_unresolved` or `closed_unsafe`, as appropriate. The system MUST NOT label a timeout “stable.” An emergency may close the cycle before a full orbit as an explicitly incomplete `closed_unsafe` outcome; it cannot be called a successful full round.

After stability is recorded, fresh observations go to monitoring or a subsequent-cycle queue. A newly discovered material defect before ratification invalidates eligibility and closes this cycle unresolved or unsafe. It does not trigger an automatic second correction round.

## 7. Neutral terms as a peacemaking operator

The neutral operator translates the candidate and remaining disagreements into the shared, approved structure. It MUST preserve actors, scope, modality, quantities, deadlines, conditions, evidence status, rights, and reserved positions. It MUST NOT convert allegations into findings, preferences into obligations, or uncertainty into certainty.

The same rules apply to each actor, including the agency and evaluators. Equivalent treatment requires accessible language and context-sensitive accommodations; identical word counts are not a sufficient fairness measure.

The output includes:

- each actor's own position and the other actors' attributed positions;
- precisely accepted commitments and their verification method;
- acknowledged reasoning mistakes and correction references;
- remaining doubts, disputes, uncertainties, and reservations;
- what remains outside the agreement and which earlier obligations continue;
- review dates and any pre-consented temporary fallback terms.

A material change introduced by normalization invalidates the candidate's earlier evaluation and acceptance. If there is insufficient time for a fresh evaluation and exact-text ratification, close unresolved. Neutral wording cannot be used to negotiate an additional concession.

If no new package is accepted, neutral closure records that fact. Temporary terms apply only when authorized in advance; “neutral” does not mean automatically preserving every existing distribution of power, territory, or resources.

## 8. Mistakes, acknowledgement, and forgiveness

Known material mistakes MUST receive an append-only correction record from the responsible actor or evaluator. A challenged but unacknowledged claim remains a dispute pending the defined review; the agency cannot manufacture a personal confession.

The record distinguishes arithmetic/formal inference errors, factual errors, translation errors, model limits, value disagreements, and disputed legal interpretations. Only the first category is automatically a mathematical or logical error in the narrow sense. Culture or refusal to agree is never an error category.

A self-acknowledged mistake SHOULD be accompanied by an explanation of its effects, a repair proposal, and a culturally acceptable request for forgiveness where appropriate. Neither forgiveness nor the emotional form of an apology can be compelled. A request for forgiveness does not erase evidence, responsibility, harm, or another person's available remedies. See [Mistake and repair](docs/MISTAKE-AND-REPAIR.md).

## 9. Ratification and closure

Each side whose new commitments are necessary MUST explicitly ratify the same frozen neutral text and content digest within its mandate. Approval of the agency or procedure is not approval of a future settlement. Silence is never ratification.

Eligible terminal outcomes are:

| Status | Meaning |
|---|---|
| `not_started` | Entry authorization incomplete |
| `closed_agreed` | Stable eligible package explicitly ratified by all required sides |
| `closed_partial` | Independently workable subset evaluated and ratified by every required side for that subset; remaining issues recorded |
| `closed_unresolved` | Full cycle/deadline reached without an eligible ratified package |
| `closed_unsafe` | Predetermined exclusion or emergency prevents eligible continuation/adoption |

Closed partial agreements MUST NOT impose obligations on non-signatories or silently reallocate their protected interests. Whether a subset is independently workable is a professional review question, not a checkbox inferred from signatures.

The closing record preserves the original identity/mandate references, all modifications, reasons, dissents, evaluations, and signatures. An actor can voluntarily develop its identity; the protocol does not optimize or forcibly rewrite it.

## 10. Persistence after closure

The negotiation ends. Accepted obligations persist for their stated duration. Monitoring records performance, incidents, corrections, and whether previously authorized fallback actions are triggered. It does not invent new obligations or deploy coercive measures.

A fresh negotiation requires a new identifier, a new starting record, and fresh authorization under the agreed initiation rules. There is no automatic loop designed to wear down a refusal.
