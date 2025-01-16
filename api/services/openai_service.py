import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def upload_file(file_path):
    with open(file_path, 'rb') as file:
        response = client.files.create(file=file, purpose='user_data')

    return response


def list_files():
    response = client.files.list()
    return response


def retrieve_file_info(file_id):
    response = client.files.retrieve(file_id)
    return response


def delete_file(file_id):
    response = client.files.delete(file_id)
    return response


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


def analyze_file(file_id):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Analyze the content of the file with ID {file_id}."}
        ],
        max_tokens=100
    )
    return response
