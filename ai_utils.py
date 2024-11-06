# ai_utils.py
from openai import OpenAI
import openai
from config import API_KEY
from file_utils import read_file

openai.api_key = API_KEY
client = OpenAI(api_key=API_KEY)

# def ai(prompt):
#     content = read_file("index.txt")
#     completion = openai.ChatCompletion.create(
#         model="gpt-4o-mini",
#         messages=[
#             {"role": "system", "content": content},
#             {"role": "user", "content": prompt}
#         ]
#     )
#     return completion.choices[0].message.content


async def ai(prompt):
    content = read_file("index.txt")
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": content},
            {"role": "user", "content": prompt}
        ]
    )
    return completion.choices[0].message.content