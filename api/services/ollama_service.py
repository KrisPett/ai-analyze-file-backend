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
    for message in response:
        yield message['message']['content']


def analyze_file(file_content, text_prompt=""):
    response = client.chat(
        model='deepseek-r1:32b',
        messages=[
            {
                'role': 'user',
                'content': f"{text_prompt}\n\nAnalyze the following content:\n\n{file_content}",
            },
        ],
    )
    return response

