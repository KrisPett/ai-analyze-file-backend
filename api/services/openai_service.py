import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def upload_file(file_path):
    with open(file_path, 'rb') as file:
        response = client.files.create(file=file, purpose='user_data')
    return response

# def analyze_file(file_id):
#     response = client.answers.create(
#         model="gpt-4o-mini",
#         file=file_id,
#         question="Analyze the content of the file.",
#         examples_context="In 2017, U.S. life expectancy was 78.6 years.",
#         examples=[["What is human life expectancy in the United States?", "78 years."]],
#         max_tokens=100
#     )
#     return response

def generate_chat():
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": "what is google?"
            }
        ]
    )
    return completion.choices[0].message
