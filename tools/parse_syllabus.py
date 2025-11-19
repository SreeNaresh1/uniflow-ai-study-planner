# tools/parse_syllabus.py

from typing import Dict, List


def parse_syllabus(raw_text: str) -> Dict:
    """
    Very simple parser: each non-empty line is treated as a topic.

    This is the same logic used in the Kaggle notebook.
    """
    lines: List[str] = [l.strip() for l in raw_text.splitlines() if l.strip()]
    topics = [{"title": line, "estimated_hours": 2} for line in lines]
    return {"status": "success", "topics": topics}
