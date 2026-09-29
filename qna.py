from gemini_client import generate_text

SYSTEM = """You are EduGenie, a careful educational assistant.
Answer academic questions accurately and concisely.
Explain unfamiliar terms briefly when useful.
If a question is ambiguous, state the assumption you are making.
Do not invent citations or sources.
"""

def answer_question(question: str) -> str:
    prompt = f"""Answer this student's question.

Question:
{question}

Give the direct answer first, then a short explanation when appropriate.
Use simple language suitable for a learner."""
    return generate_text(prompt, system_instruction=SYSTEM, temperature=0.2)
