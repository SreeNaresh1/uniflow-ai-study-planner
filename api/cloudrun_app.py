# api/cloudrun_app.py

import os
import asyncio

import nest_asyncio
from flask import Flask, request, jsonify
from google.adk.runners import InMemoryRunner
from google.genai import types as genai_types

from agents.orchestrator_agent import create_root_agent

# Ensure GOOGLE_API_KEY is set via environment, but do not hard-code it
if "GOOGLE_API_KEY" not in os.environ:
    # In Cloud Run, this must be set in the service configuration.
    # We don't raise here to allow local testing with Application Default Credentials.
    pass

nest_asyncio.apply()

APP_NAME = "uniflow_app"
USER_ID = "api_user"

# Build global runner + session (simple, like in the notebook)
root_agent = create_root_agent()
runner = InMemoryRunner(agent=root_agent, app_name=APP_NAME)

loop = asyncio.get_event_loop()
session = loop.run_until_complete(
    runner.session_service.create_session(
        app_name=APP_NAME,
        user_id=USER_ID,
    )
)

app = Flask(__name__)


def run_message(message: str) -> str:
    """
    Send a message through the orchestrator and collect the text response.
    """
    content = genai_types.Content(
        role="user",
        parts=[genai_types.Part.from_text(text=message)],
    )

    parts = []
    for event in runner.run(
        user_id=USER_ID,
        session_id=session.id,
        new_message=content,
    ):
        if event.content and event.content.parts:
            part = event.content.parts[0]
            if getattr(part, "text", None):
                parts.append(part.text)

    return "".join(parts)


@app.route("/uniflow", methods=["POST"])
def uniflow():
    """
    Cloud Run endpoint. Expects JSON:

      { "message": "..." }

    Returns:

      { "response": "..." }
    """
    data = request.get_json(silent=True) or {}
    msg = data.get("message", "").strip()
    if not msg:
        return jsonify({"error": "Missing 'message' field"}), 400

    try:
        reply = run_message(msg)
        return jsonify({"response": reply})
    except Exception as e:
        # Basic error handling; in production you'd have better logging.
        return jsonify({"error": str(e)}), 500


@app.route("/", methods=["GET"])
def health():
    return "UniFlow API is running.", 200


if __name__ == "__main__":
    # Local dev; Cloud Run will use gunicorn.
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
