from ..ai_config import AI_ROOT_CAUSE_RULES


def simple_ai_suggest(description: str) -> dict:
    """Very small rule-based classifier to make the demo feel 'real'."""
    desc_lower = description.lower()
    defect_type = "General defect"
    root_cause = "General workmanship / planning issue"
    similar_ids: list[str] = []

    for rule in AI_ROOT_CAUSE_RULES:
        for keyword in rule["keywords"]:
            if keyword in desc_lower:
                defect_type = rule["defect_type"]
                root_cause = rule["root_cause"]
                similar_ids = rule.get("sample_case_ids", [])
                break

    return {
        "defect_type": defect_type,
        "possible_root_cause": root_cause,
        "similar_case_ids": similar_ids,
    }
