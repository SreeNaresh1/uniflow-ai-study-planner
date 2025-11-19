# memory/memory_store.py

from typing import Dict, Any, List, Optional

STUDY_PLANS: Dict[str, Any] = {}
PROGRESS_LOGS: Dict[str, List[Any]] = {}


def save_plan(user_id: str, plan: Any) -> None:
    STUDY_PLANS[user_id] = plan


def get_plan(user_id: str) -> Optional[Any]:
    return STUDY_PLANS.get(user_id)


def log_progress(user_id: str, entry: Any) -> None:
    PROGRESS_LOGS.setdefault(user_id, []).append(entry)


def get_progress(user_id: str) -> Optional[List[Any]]:
    return PROGRESS_LOGS.get(user_id)
