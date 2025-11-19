# agents/planner_agent.py

from google.adk.agents import Agent
from tools.parse_syllabus import parse_syllabus


def create_planner_agent() -> Agent:
    """
    Planner agent: same instructions as in the notebook.
    """
    return Agent(
        name="planner_agent",
        model="gemini-2.0-flash",
        description="Creates study plans from syllabus and dates.",
        instruction=(
            "You receive syllabus text, exam date, and available daily hours. "
            "Call the tools parse_syllabus and compute_schedule to create a plan. "
            "Return:\n"
            "1) A friendly overview of the schedule.\n"
            "2) A short JSON-like summary of the main schedule."
        ),
        tools=[parse_syllabus],  # compute_schedule can be added later if needed
    )
