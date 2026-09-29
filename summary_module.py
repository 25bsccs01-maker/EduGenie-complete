from gemini_client import generate_text

SYSTEM = """You are EduGenie's summarization module.
Create accurate, concise educational summaries.
Preserve important facts, relationships, definitions, and conclusions.
Do not add facts that are absent from the input.
"""

def summarize_text(text: str) -> str:
    prompt = f"""Summarize the following educational passage.

PASSAGE:
{text}

Return:
1. A short summary paragraph.
2. 3-6 key points as bullet points."""
    return generate_text(
        prompt,
        system_instruction=SYSTEM,
        temperature=0.2,
        max_output_tokens=1800,
    )
