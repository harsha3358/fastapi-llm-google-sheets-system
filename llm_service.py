from transformers import pipeline

# Load lightweight open-source model
generator = pipeline(
    "text-generation",
    model="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    max_new_tokens=120
)

def generate_user_insight(email: str, role: str) -> str:
    prompt = f"""
    Analyze the following user:
    Email: {email}
    Role: {role}

    Provide a short professional insight and recommendation.
    """

    response = generator(prompt)[0]["generated_text"]
    return response