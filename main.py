import os
from dotenv import load_dotenv
from openai import OpenAI
from gpts_roles import create_gpts
from prompt import create_prompt
from content_manager import read_from_file,write_to_file

load_dotenv()

api_key = os.getenv('API_KEY')

client = OpenAI(api_key=api_key)

content = read_from_file()

gpts = create_gpts()
prompt = create_prompt(content)


completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        gpts,
        prompt
    ]
)

write_to_file(completion.choices[0].message,"", "")









# completion = client.chat.completions.create(
#     model="gpt-4o-mini",
#     messages=[
#         {"role": "system", "content": "You are a helpful assistant."},
#         {
#             "role": "user",
#             "content": "Write a haiku about recursion in programming."
#         }
#     ]
# )

# print(completion.choices[0].message)    