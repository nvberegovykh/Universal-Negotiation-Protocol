# Mathematical model

This is a proposed formalization of the author's sketch. Definitions below are design choices, not theorems that diplomacy must obey. The model specifies a procedure; it does not prove peace, fairness, honesty, or convergence.

## 1. Actors, visual chamber, and agreement space

Let \(I=\{1,\ldots,n\}\) be the recognized sides, with one active representative \(r_i\) per side. A displayed seat position \(p_i=(u_i,v_i)\) lies in the fixed chamber:

\[
B=\{(u,v):u^2+v^2<0.25\}.
\]

The chamber radius is \(0.5\). Seat positions do not encode a person's worth, legal status, military strength, or number of votes. The chamber persists even when there is no acceptable settlement. Its display is independent of the agreement radius.

A proposal is a vector \(z\) of actual terms: quantities, schedules, obligations, conditions, verification methods, and reservations. It will generally have more than two dimensions and may contain discrete choices. A circle is only a visual summary.

Let \(D\) be a fixed reference domain of candidate packages, \(P_t\) the implementable subset, \(L\) the subset consistent with the applicable legal constraints identified in the guidelines, and \(A_{i,t}\) the packages side \(i\) currently authorizes as acceptable for consideration. Define:

\[
F_t=D\cap P_t\cap L\cap\bigcap_{i\in I}A_{i,t}.
\]

Membership means that a package is a candidate; exact-text ratification is a separate act. Estimated or confidential acceptability must be marked as estimated or unknown. The evaluator cannot infer actual consent from predicted utility.

For a visual summary, agree in advance on a finite nonzero measure \(\mu(D)\). Then one optional normalized radius is:

\[
R_t=\sqrt{\frac{\mu(F_t)}{\mu(D)}},\qquad
x^2+y^2=R_t^2,\qquad
\operatorname{Area}_t=\pi R_t^2.
\]

The axes, domain, weighting, and measure must remain fixed during the cycle. Otherwise changing units can create the illusion of progress. Discrete proposal catalogs may use a declared counting measure; a continuous measure can assign zero area to a nonempty set, including a single acceptable package. Consequently \(R_t=0\) alone is not proof that no agreement exists. Unknown membership produces an unknown radius or an interval, not a fabricated number.

Actors control this space through authorized changes in terms and acceptability. Guarantees, resources, and evidence may change feasibility. Enlarging the drawn circle by hand does not make additional packages real. Volume is descriptive and MUST NOT be used as the sole optimization target: a small safe agreement may be preferable to many poor ones.

The standard circumference parameterization is \(x=R\cos\phi\), \(y=R\sin\phi\). This separates radius from angle and replaces the sketch's informal squared sine/cosine notation.

## 2. One orbit and persistent memory

Let \(k\in\{0,\ldots,n\}\) count disposed correction opportunities. Let \(q_i\in\{0,1\}\) indicate whether side \(i\)'s opportunity is complete. Then:

\[
k=\sum_i q_i,\qquad
\theta_k=2\pi k/n.
\]

At full closure \(k=n\), so \(\theta_n=2\pi\equiv0\pmod{2\pi}\). Each opportunity is used once through revision, explicit retention, or recorded expiration. Time may advance through the procedure, but it cannot grant a second opportunity under the same negotiation identifier.

With simultaneous submissions, the angular ordering is a bookkeeping order applied at release, not unequal speaking priority. The end state includes accumulated records:

\[
S_{\mathrm{end}}=(\theta=0,\ M_{\mathrm{start}}\mathbin{\Vert}\Delta M,\ C_{\mathrm{accepted}},\ U_{\mathrm{unresolved}}).
\]

Here \(\Vert\) denotes appending an auditable record. Returning to the checkpoint preserves history. Identity and mandate references remain attributable; new self-descriptions are recorded rather than imposed. An emergency closure before \(k=n\) is explicitly an incomplete orbit.

## 3. Logic-time function

Use a monotone elapsed clock \(\tau\) for deadlines and a separate UTC timestamp for audit. Wall-clock changes must not restart an opportunity. Let \(T\) be the final time budget and \(W>0\) the agreed observation window.

Define the operational logic-time state:

\[
\ell(\tau)=(h, q, d, e, f, b),
\]

where \(h\) identifies the exact candidate and interpretation, \(q\) records completed opportunities, \(d\) records material doubts, \(e\) records version-bound expert review status, \(f\) records freshness/coverage, and \(b\) records legal, feasibility, and safety exclusions.

For any numeric quantities used to test stability, define units, individual distance functions \(\delta_j\), and tolerances \(\varepsilon_j\) before entry. Categorical commitments require exact equality. A generic stability test is:

\[
\operatorname{Stable}(\tau)=
\left[\tau\ge W\right]
\land\left[\forall j,\ \sup_{s\in[\tau-W,\tau]}\delta_j(\ell_j(s),\ell_j(\tau))\le\varepsilon_j\right]
\land\left[\sum_iq_i=n\right]
\land\operatorname{ReviewPass}
\land\operatorname{FreshEnough}
\land\left[|d_{\mathrm{material,open}}|=0\right]
\land\neg\operatorname{Excluded}.
\]

The exact candidate text and material interpretation must remain fixed throughout \(W\). Hash equality checks unchanged bytes; it cannot prove shared understanding. Accessible-language confirmation and professional interpretation review supply the separate semantic checks.

Operational stability ends active doubt discussion for this cycle. It does not erase unresolved out-of-scope disagreements or forbid later observations. A new material problem before ratification invalidates eligibility; it cannot be silenced by citing a previously stable score.

If \(\tau=T\) and the test has not passed, close unresolved or unsafe. Limited time establishes a stopping boundary, not a proof. Stable eligible text still requires explicit ratification. Ending early is allowed only after the complete correction round, required reviews, stability window, and the pre-agreed consent-check window have been disposed of.

## 4. Neutral operator

Let \(G\) be the locked conflict guidelines. The neutral operator \(N_G\) maps attributed statements and proposed commitments to a common record format:

\[
N_G:S\longrightarrow S_{\mathrm{neutral}}.
\]

Required design properties:

- **Meaning preservation:** obligations, beneficiaries, quantities, conditions, reservations, and epistemic status remain unchanged.
- **Actor symmetry:** relabeling actors relabels the result without changing their procedural rights.
- **Idempotence:** \(N_G(N_G(S))=N_G(S)\) once normalized. A production implementation must define what counts as equal text or structure.
- **Traceability:** each normalized clause links to its source, evaluation, and accepting actors.
- **No invented consensus:** disagreement remains attributed disagreement.

These properties are requirements to test, not capabilities established by calling an AI “neutral.” If normalization materially alters terms, it is a new proposal version and requires a new evaluation and explicit ratification; no extra correction opportunity is created.

## 5. Coexistence rather than a single utility maximum

Let \(C_i(z)\) be the side-specific conditions for continued existence, agency, identity continuity, and legitimate security under the agreed framework. Candidate outcomes should satisfy:

\[
z\in P_t\cap L,\qquad C_i(z)=\mathrm{true}\ \text{for every affected side},
\]

with impacts on people outside the participating sides separately reviewed. No universal numeric utility function is asserted. An actor's claimed identity does not itself establish the permissibility of a proposed action. Claims, rights, and consequences require contextual assessment.

Enduring stability depends on behavior, institutions, credible commitments, and changing conditions after the session. The one-orbit rule establishes bounded procedure only.
