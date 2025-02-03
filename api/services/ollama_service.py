import os
from dotenv import load_dotenv
from ollama import chat
from ollama import ChatResponse
from pathlib import Path
from ollama import Client

load_dotenv()

client = Client(
    host='http://localhost:11434',
)


def generate_chat():
    response = client.chat(
        model='llama3.2',
        messages=[
            {
                'role': 'user',
                'content': 'Why is the sky blue?',
            },
        ],
        stream=True
    )
    return response


def analyze_file(file_content, text_prompt=""):
    response = client.chat(model='llama3.2', messages=[
        {
            'role': 'user',
            'content': 'Why is the sky blue?',
        },
    ])
    return response
