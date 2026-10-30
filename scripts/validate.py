#!/usr/bin/env python3
"""Check selected UNP closed-record invariants; never certify facts or signatures."""
from __future__ import annotations

import hashlib
import json
import math
from datetime import datetime
from pathlib import Path
import sys


def digest(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def timestamp(value: str) -> datetime:
    result = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if result.tzinfo is None:
        raise ValueError("timestamps must include a UTC offset")
    return result


def validate(record: dict) -> list[str]:
    """Return structural errors. Authenticity and semantic accuracy are out of scope.

    Checks: unique sides/representatives; unanimous agency mandate; single-round
    opportunity accounting; common baseline; time bounds; exact text digests;
    proposal-bound professional review records; evidence freshness; material
    doubts; declared stability window; and exact-version explicit ratification.
    """
    errors: list[str] = []

    def require(condition: bool, message: str) -> None:
        if not condition:
            errors.append(message)

    def index(items: list, key: str, label: str) -> dict:
        result = {}
        for item in items:
            identifier = item[key]
            require(isinstance(identifier, str) and bool(identifier.strip()),
                    f"{label}: identifiers must be nonempty strings")
            require(identifier not in result, f"{label}: duplicate {identifier}")
            result[identifier] = item
        return result

    try:
        require(record["schema_version"] == "0.1.0", "unsupported schema version")
        require(isinstance(record["synthetic"], bool), "synthetic must be boolean")
        sides = index(record["sides"], "id", "sides")
        require(len(sides) >= 2, "at least two sides required")
        ids = set(sides)
        representatives = [s["representative_id"] for s in sides.values()]
        require(all(isinstance(x, str) and x.strip() for x in representatives),
                "one nonempty representative identifier is required per side")
        require(len(set(representatives)) == len(ids),
                "a representative cannot occupy multiple sides' seats")
        require(all(s["mandate_ref"] for s in sides.values()), "mandate references required")
        agency = record["agency"]
        require(set(agency["approved_by"]) == ids and len(agency["approved_by"]) == len(ids),
                "every side must approve the agency exactly once")
        require(bool(agency["guidelines_ref"]) and bool(agency["guidelines_sha256"]),
                "guideline version and digest required")

        cycle = record["cycle"]
        require(type(cycle["correction_round_limit"]) is int and
                cycle["correction_round_limit"] == 1, "exactly one correction round required")
        start = timestamp(cycle["starts_at"])
        cutoff = timestamp(cycle["correction_deadline"])
        deadline = timestamp(cycle["deadline_at"])
        window = cycle["stability_window_seconds"]
        require(type(window) in (int, float) and math.isfinite(window) and window > 0,
                "stability window must be positive and finite")
        require(start < cutoff < deadline, "invalid cycle time ordering")
        closure = record["closure"]
        closed = timestamp(closure["at"])
        status = closure["status"]
        require(status in {"closed_agreed", "closed_partial", "closed_unresolved", "closed_unsafe"},
                "unsupported closed-session outcome")
        require(start <= closed <= deadline, "closure must fall within the cycle time budget")
        require(type(closure["stable"]) is bool and type(closure["exclusion_triggered"]) is bool,
                "stability and exclusion flags must be boolean")

        corrections = index(record["corrections"], "side_id", "corrections")
        require(set(corrections) <= ids, "correction from unknown side")
        if status != "closed_unsafe":
            require(set(corrections) == ids, "full round requires one disposed opportunity per side")
            require(closed >= cutoff, "full round cannot close before common release deadline")
        else:
            require(closure["exclusion_triggered"] is True, "unsafe closure requires an exclusion record")
        for correction in corrections.values():
            mode = correction["disposition"]
            at = timestamp(correction["at"])
            require(mode in {"revised", "retained", "no_response"}, "invalid correction disposition")
            require(start <= at <= closed, "correction outside active session")
            require(correction["baseline_sha256"] == record["baseline"]["sha256"],
                    "corrections must use the same frozen baseline")
            if mode == "no_response":
                require(at >= cutoff, "no response cannot be declared before opportunity expires")
            else:
                require(at <= cutoff, "correction submitted after opportunity deadline")

        proposals = index(record["proposals"], "id", "proposals")
        reviews = index(record["reviews"], "id", "reviews")
        doubts = index(record["doubts"], "id", "doubts")
        for proposal in proposals.values():
            require(proposal["content_sha256"] == digest(proposal["terms"]),
                    "proposal content digest mismatch")
            affected = proposal["affected_side_ids"]
            require(bool(affected) and set(affected) <= ids and len(set(affected)) == len(affected),
                    "proposal affected-side roster is invalid")
        for doubt in doubts.values():
            require(doubt["status"] in {"open", "resolved"}, "invalid doubt status")
            require(set(doubt["material_to"]) <= set(proposals), "doubt refers to unknown proposal")

        adopted = closure["adopted_proposal_ids"]
        candidates = closure["candidate_proposal_ids"]
        require(len(set(adopted)) == len(adopted), "duplicate adopted proposal")
        require(len(set(candidates)) == len(candidates), "duplicate candidate proposal")
        require(set(adopted) <= set(candidates) <= set(proposals), "unknown or unlisted candidate")
        ratifications = closure["ratifications"]
        ratification_index = {}
        for consent in ratifications:
            key = (consent["side_id"], consent["proposal_id"])
            require(key not in ratification_index, "duplicate ratification")
            ratification_index[key] = consent
            require(consent["side_id"] in ids, "ratification from unknown side")
            require(consent["proposal_id"] in adopted, "ratification must refer to an adopted package")
            require(bool(consent["evidence_ref"]), "explicit consent evidence reference required")

        if status in {"closed_agreed", "closed_partial"}:
            require(bool(adopted), "agreed/partial outcome requires adopted terms")
            require(closure["stable"] is True, "adoption requires demonstrated operational stability")
            require(closure["exclusion_triggered"] is False, "excluded package cannot be adopted")
        else:
            require(not adopted and not ratifications, "unresolved/unsafe closure cannot impose new terms")
        if closure["exclusion_triggered"]:
            require(not closure["stable"], "excluded outcome cannot be labeled stable")

        if closure["stable"]:
            require(bool(candidates), "stability must identify a candidate")
            since = timestamp(closure["stable_since"])
            require(since >= cutoff, "stability starts after complete correction round release")
            require((closed - since).total_seconds() >= window, "stability observation window incomplete")
            require(set(corrections) == ids, "stable result requires a complete round")
            for pid in candidates:
                proposal = proposals[pid]
                require(proposal["neutral_operator_applied"] is True, "neutral normalization record required")
                review = reviews[proposal["review_id"]]
                require(review["proposal_sha256"] == proposal["content_sha256"],
                        "evaluation does not bind exact proposal version")
                require(review["agency_id"] == agency["id"] and
                        review["guidelines_sha256"] == agency["guidelines_sha256"],
                        "evaluation uses wrong agency or guideline version")
                require(bool(review["responsible_professionals"]) and
                        all(isinstance(p, str) and p.strip() for p in review["responsible_professionals"]),
                        "accountable professional review record required")
                require(bool(review["signoff_ref"]), "professional signoff reference required")
                require(review["disposition"] in {"supported", "conditional"}, "evaluation does not support eligibility")
                if review["disposition"] == "conditional":
                    require(review["conditions_satisfied"] is True and bool(review["condition_evidence_refs"]),
                            "conditional review needs satisfaction evidence")
                issued = timestamp(review["issued_at"])
                require(start <= issued <= since <= closed <= timestamp(review["valid_until"]),
                        "review is not valid throughout the stability/closure period")
                require(bool(review["sources"]), "evidence provenance required")
                for source in review["sources"]:
                    observed = timestamp(source["observed_at"])
                    retrieved = timestamp(source["retrieved_at"])
                    require(observed <= retrieved <= issued, "invalid source observation/retrieval time")
                    require(closed <= timestamp(source["fresh_until"]), "evidence expired before closure")
                require(not any(d["status"] == "open" and pid in d["material_to"] for d in doubts.values()),
                        "unresolved material doubt prevents stable adoption")
                if pid in adopted:
                    for side in proposal["affected_side_ids"]:
                        consent = ratification_index.get((side, pid))
                        require(consent is not None, "missing explicit ratification from an affected side")
                        if consent:
                            require(consent["proposal_sha256"] == proposal["content_sha256"],
                                    "ratification digest differs from final text")
                            at = timestamp(consent["at"])
                            require(since <= at <= closed and (at - since).total_seconds() >= window,
                                    "ratification must follow the stability window and precede closure")
        return errors
    except (KeyError, TypeError, ValueError, AttributeError, OverflowError) as error:
        errors.append(f"malformed or incomplete record: {error}")
        return errors


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python3 scripts/validate.py SESSION.json", file=sys.stderr)
        return 2
    try:
        record = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    except (OSError, ValueError) as error:
        print(f"Cannot read record: {error}", file=sys.stderr)
        return 2
    errors = validate(record)
    if errors:
        for error in errors:
            print(f"FAIL: {error}")
        return 1
    print("PASS: selected UNP structural checks. Facts, credentials, signatures, and real-world stability are not verified.")
    if record["synthetic"]:
        print("SYNTHETIC EXAMPLE: no actual professional approval or SI evaluation.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
