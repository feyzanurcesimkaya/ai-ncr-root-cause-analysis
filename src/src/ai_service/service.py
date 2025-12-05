from typing import Dict, Any


def evaluate_image_clarity(image_bytes: bytes) -> float:
    """Return a fake clarity score for the given image (demo only)."""
    return 0.9


def suggest_root_cause(ncr_description: str) -> Dict[str, Any]:
    """Simple keyword-based suggestion, to be kept in sync with backend.ai_config."""
    text = ncr_description.lower()
    if "honeycomb" in text or "honeycombing" in text:
        return {
            "defect_type": "Concrete surface defect",
            "possible_root_cause": "Insufficient vibration during concrete placement.",
        }
    if "crack" in text:
        return {
            "defect_type": "Cracking",
            "possible_root_cause": "Shrinkage or thermal movement.",
        }
    return {
        "defect_type": "General defect",
        "possible_root_cause": "General workmanship / planning issue.",
    }
