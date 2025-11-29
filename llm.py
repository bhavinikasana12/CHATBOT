
import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_questions(tech_stack):
    """
    Generate 3-5 technical interview questions based on the tech stack
    """
    prompt = f"Generate 3 interview questions for the following tech stack: {tech_stack}."

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a hiring assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response['choices'][0]['message']['content']
