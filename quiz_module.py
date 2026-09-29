import json
import re
from gemini_client import generate_text

SYSTEM = """You are EduGenie's quiz generator.
Generate exactly 3 multiple-choice questions from the supplied text.
Each question must have exactly 4 options and one correct answer.
The correct_answer must exactly match one option.
Return JSON only. No Markdown fences. No commentary.
"""

def clean_json_block(raw: str) -> str:
    raw = raw.strip()
    raw = re.sub(r"^```(?:json)?\s*", "", raw, flags=re.IGNORECASE)
    raw = re.sub(r"\s*```$", "", raw)
    return raw.strip()

def _validate_quiz(data):
    if not isinstance(data, list) or len(data) != 3:
        raise ValueError("Quiz must contain exactly 3 questions.")

    cleaned = []
    for item in data:
        if not isinstance(item, dict):
            raise ValueError("Each quiz item must be an object.")

        question = item.get("question")
        options = item.get("options")
        correct = item.get("correct_answer")

        if not isinstance(question, str) or not question.strip():
            raise ValueError("A quiz question is missing.")
        if not isinstance(options, list) or len(options) != 4:
            raise ValueError("Each question must have exactly 4 options.")
        if not all(isinstance(x, str) and x.strip() for x in options):
            raise ValueError("All options must be non-empty strings.")
        if correct not in options:
            raise ValueError("correct_answer must match one option.")

        cleaned.append({
            "question": question.strip(),
            "options": [x.strip() for x in options],
            "correct_answer": correct.strip(),
        })

    return cleaned

def generate_quiz(text: str):
    prompt = f"""Create a 3-question MCQ quiz from this passage.

PASSAGE:
{text}

Required JSON shape:
[
  {{
    "question": "Question text",
    "options": ["A", "B", "C", "D"],
    "correct_answer": "One exact option"
  }}
]"""

    raw = generate_text(
        prompt,
        system_instruction=SYSTEM,
        temperature=0.2,
        max_output_tokens=1800,
    )

    try:
        data = json.loads(clean_json_block(raw))
        return _validate_quiz(data)
    except (json.JSONDecodeError, ValueError) as exc:
        raise RuntimeError(f"Could not parse a valid quiz from Gemini: {exc}") from exc
