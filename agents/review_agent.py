# agents/review_agent.py

from google.adk.agents import Agent


def create_review_agent() -> Agent:
    """
    Review agent: suggests what to study today based on the plan.
    """
    return Agent(
        name="review_agent",
        model="gemini-2.0-flash",
        description="Reviews the current study plan and suggests today's tasks.",
        instruction=(
            "You receive a study plan and an optional progress summary. "
            "Suggest what the student should study today, including any backlog topics."
        ),
    )
