from openai import OpenAI
import openai
from dotenv import load_dotenv
import os
load_dotenv()

file_path = "index.txt"
api_key = os.getenv("AI_API")

client = OpenAI(api_key=api_key)


def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def write_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)


prompt = "I'm testing a feature if you can read this it's working write some short message"

def ai(prompt):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    return completion.choices[0].message.content

Ai_res = ai(prompt)


write_file(file_path, Ai_res)

