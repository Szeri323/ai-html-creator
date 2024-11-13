from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()

api_key = os.getenv('API_KEY')

client = OpenAI(api_key=api_key)


completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "user",
            "content": "Write a haiku about recursion in programming."
        }
    ]
)

print(completion.choices[0].message)