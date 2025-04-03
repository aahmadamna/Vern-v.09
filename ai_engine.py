import openai
import os
from dotenv import load_dotenv

load_dotenv()

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_math_expression(instruction):
    prompt = f"""
You are an AI that converts natural language math instructions into valid Python expressions.
Only return the raw expression (no explanation or comments).

Instruction: {instruction}
Expression:
"""

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0,
    )

    return response.choices[0].message.content.strip()
