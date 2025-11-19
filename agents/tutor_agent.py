# agents/tutor_agent.py

from google.adk.agents import Agent


def create_tutor_agent() -> Agent:
    """
    Tutor agent: explains topics and generates practice questions.
    """
    return Agent(
        name="tutor_agent",
        model="gemini-2.0-flash",
        description="Explains topics and generates practice questions.",
        instruction=(
            "You are a friendly tutor. Explain concepts step-by-step with simple "
            "examples. When asked, create a few short practice questions with answers."
        ),
    )
