# runner/run_uniflow.py

import asyncio

import nest_asyncio
from google.adk.runners import InMemoryRunner
from google.genai import types as genai_types

from agents.orchestrator_agent import create_root_agent

nest_asyncio.apply()

APP_NAME = "uniflow_app"
USER_ID = "student"


def build_runner():
    root_agent = create_root_agent()
    runner = InMemoryRunner(agent=root_agent, app_name=APP_NAME)

    loop = asyncio.get_event_loop()
    session = loop.run_until_complete(
        runner.session_service.create_session(
            app_name=APP_NAME,
            user_id=USER_ID,
        )
    )
    return runner, session


def ask(runner: InMemoryRunner, session_id: str, msg: str) -> str:
    """
    Helper function similar to the notebook's ask().
    """
    content = genai_types.Content(
        role="user",
        parts=[genai_types.Part.from_text(text=msg)],
    )

    full_text_parts = []
    for event in runner.run(
        user_id=USER_ID,
        session_id=session_id,
        new_message=content,
    ):
        if event.content and event.content.parts:
            part = event.content.parts[0]
            if getattr(part, "text", None):
                full_text_parts.append(part.text)

    return "".join(full_text_parts)


if __name__ == "__main__":
    runner, session = build_runner()
    print("✅ UniFlow runner ready. Session ID:", session.id)

    # Simple manual tests (mirroring the notebook demo)
    print("\n--- Study Plan Demo ---")
    print(
        ask(
            runner,
            session.id,
            "Here is my syllabus:\n"
            "Binary Trees\n"
            "AVL Trees\n"
            "Heaps\n"
            "My exam is on 2025-11-25. I can study 2 hours per day.",
        )
    )

    print("\n--- Daily Guidance Demo ---")
    print(ask(runner, session.id, "What should I study today?"))

    print("\n--- Explanation Demo ---")
    print(ask(runner, session.id, "Explain AVL tree rotations with an example."))
