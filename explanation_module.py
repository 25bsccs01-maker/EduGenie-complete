import os

# The documentation specifies LaMini-Flan-T5 for concept explanation.
# Loading it is optional because the model is large and first-run download
# can be slow. Set USE_LOCAL_EXPLAINER=true to enable it.
_local_pipeline = None
_local_load_attempted = False

def _load_local_model():
    global _local_pipeline, _local_load_attempted
    if _local_load_attempted:
        return _local_pipeline

    _local_load_attempted = True
    if os.getenv("USE_LOCAL_EXPLAINER", "false").lower() != "true":
        return None

    try:
        from transformers import pipeline
        _local_pipeline = pipeline(
            "text2text-generation",
            model=os.getenv(
                "LOCAL_EXPLAINER_MODEL",
                "MBZUAI/LaMini-Flan-T5-783M"
            ),
            max_new_tokens=300,
        )
    except Exception:
        _local_pipeline = None

    return _local_pipeline


def explain_concept(topic: str) -> str:
    pipe = _load_local_model()

    if pipe is not None:
        prompt = (
            "Explain this concept to a beginner in simple language. "
            "Use a short definition, a simple example, and key points: "
            f"{topic}"
        )
        result = pipe(prompt)[0]["generated_text"].strip()
        if result:
            return result

    # Cloud fallback keeps the endpoint functional when the optional
    # local model is disabled or unavailable.
    from gemini_client import generate_text
    return generate_text(
        f"""Explain the following concept to a beginner:

{topic}

Use:
- Simple definition
- How it works
- One easy example
- 3 key points
- One common misconception, if relevant""",
        system_instruction=(
            "You are an educational explainer. Prefer clarity and "
            "simple language. Do not assume advanced background knowledge."
        ),
        temperature=0.25,
        max_output_tokens=1600,
    )
