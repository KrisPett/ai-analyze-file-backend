import os
from dotenv import load_dotenv
from openai import OpenAI
from pathlib import Path

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def upload_file(file_path):
    with open(file_path, 'rb') as file:
        response = client.files.create(file=file, purpose='fine-tune')
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


def analyze_file(file_content, text_prompt=""):
    analysis_response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"{text_prompt}\n\nAnalyze the following content:\n\n{file_content}"}
        ],
        max_tokens=10000
    )
    return analysis_response


def generate_tts(input_text="The true size of India.", file_name="speech.mp3"):
    speech_file_path = Path(__file__).parent / file_name
    response = client.audio.speech.create(
        model="tts-1-hd",
        voice="nova",
        input=input_text,
        speed=.80
    )
    response.stream_to_file(speech_file_path)
    return speech_file_path