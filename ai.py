import os
from openai import OpenAI


def ask_ai(question):

    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        return "AI service is not configured yet. Please use the college and student FAQ questions."

    try:
        client = OpenAI(api_key=api_key)

        response = client.responses.create(
            model="gpt-5-mini",
            input=f"""
You are a helpful college student assistant.

Answer the student's question clearly and simply.

The student may ask about:
- Python
- Java
- DBMS
- SQL
- Computer Networks
- Artificial Intelligence
- Machine Learning
- HTML
- CSS
- Programming
- General academic topics

Student question:
{question}
"""
        )

        return response.output_text

    except Exception:
        return "The AI service is currently unavailable. Please try again later."