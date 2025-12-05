# Very small demo rule set. In a real implementation you would replace this with
# a model or external AI service.

AI_ROOT_CAUSE_RULES = [
    {
        "name": "Concrete honeycombing",
        "keywords": ["honeycomb", "honeycombing", "voids in concrete"],
        "defect_type": "Concrete surface defect",
        "root_cause": "Insufficient vibration and poor compaction during concrete placement.",
        "sample_case_ids": ["NCR-0003", "NCR-0010"],
    },
    {
        "name": "Rebar cover issue",
        "keywords": ["insufficient cover", "rebar exposed", "steel visible"],
        "defect_type": "Reinforcement cover issue",
        "root_cause": "Incorrect bar placement or inadequate spacer usage before casting.",
        "sample_case_ids": ["NCR-0021", "NCR-0034"],
    },
    {
        "name": "Crack issue",
        "keywords": ["crack", "cracking", "shrinkage"],
        "defect_type": "Cracking",
        "root_cause": "Shrinkage, thermal movement or loading exceeding design assumptions.",
        "sample_case_ids": ["NCR-0005", "NCR-0042"],
    },
]
