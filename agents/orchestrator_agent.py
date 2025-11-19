# agents/orchestrator_agent.py

from google.adk.agents import Agent
from tools.parse_syllabus import parse_syllabus
from .planner_agent import create_planner_agent
from .tutor_agent import create_tutor_agent
from .review_agent import create_review_agent


def create_root_agent() -> Agent:
    """
    Root 'UniFlow' orchestrator agent.

    In the notebook we instantiated this directly;
    here we expose it as a factory to reuse in both
    the runner script and the Cloud Run app.
    """
    # Sub-agents are not yet wired via A2A, but the instruction
    # describes their roles and behaviours.
    _ = create_planner_agent()
    _ = create_tutor_agent()
    _ = create_review_agent()

    return Agent(
        name="uniflow_orchestrator",
        model="gemini-2.0-flash",
        description="Main UniFlow interface for students.",
        instruction=(
            "You are UniFlow, a study & exam copilot.\n"
            "You can help with:\n"
            "- Creating a study plan (when user gives syllabus and exam date).\n"
            "- Suggesting what to study today.\n"
            "- Explaining topics and giving practice questions.\n\n"
            "When the user gives syllabus and exam info, you should call the "
            "parse_syllabus tool directly to build a plan. "
            "Assume today's date is the planning start date unless the user says otherwise.\n"
            "When the user asks doubts ('explain', 'I don't understand'), act like a tutor.\n"
            "Keep responses concise and student-friendly."
        ),
        tools=[parse_syllabus],
    )
