from gemini_client import generate_text

SYSTEM = """You are EduGenie's learning-path planner.
Create realistic, progressive educational plans.
Move from foundations to intermediate and advanced topics.
Use practical exercises and recommend resource TYPES rather than inventing URLs.
"""

def get_learning_recommendations(topic: str, level: str = "beginner") -> str:
    prompt = f"""Create a structured learning path for:

Topic: {topic}
Learner level: {level}

Include:
- Goal
- Prerequisites
- Beginner foundations
- Intermediate topics
- Advanced topics
- Suggested timeline
- Practice/projects
- Resource suggestions (books, documentation, videos, courses by type)
- A simple way to check progress

Keep it practical and easy to follow."""
    return generate_text(
        prompt,
        system_instruction=SYSTEM,
        temperature=0.4,
        max_output_tokens=3000,
    )
