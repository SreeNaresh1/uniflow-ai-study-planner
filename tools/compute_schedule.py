# tools/compute_schedule.py

from datetime import date, timedelta
from typing import Dict, List, Any


def compute_schedule(
    topics: List[Dict[str, Any]],
    start_date: str,
    exam_date: str,
    daily_hours: float,
) -> Dict:
    """
    Greedy scheduler that spreads topics across days
    between start_date and exam_date.

    This is the same function defined in the notebook.
    """
    start = date.fromisoformat(start_date)
    end = date.fromisoformat(exam_date)

    days = (end - start).days
    if days <= 0:
        return {"status": "error", "message": "Invalid date range"}

    schedule: List[Dict[str, Any]] = []
    day_cursor = start
    day_capacity = daily_hours
    day_topics: List[Dict[str, Any]] = []

    for topic in topics:
        hours_needed = topic["estimated_hours"]
        while hours_needed > 0:
            if day_capacity <= 0:
                schedule.append({"date": str(day_cursor), "topics": day_topics})
                day_cursor += timedelta(days=1)
                day_capacity = daily_hours
                day_topics = []
                if day_cursor > end:
                    return {
                        "status": "error",
                        "message": "Not enough days for all topics",
                    }

            allocate = min(day_capacity, hours_needed)
            day_topics.append(
                {"title": topic["title"], "hours": float(allocate)}
            )
            day_capacity -= allocate
            hours_needed -= allocate

    if day_topics:
        schedule.append({"date": str(day_cursor), "topics": day_topics})

    return {"status": "success", "schedule": schedule}
