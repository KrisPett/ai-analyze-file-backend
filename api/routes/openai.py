from fastapi import APIRouter, UploadFile, File, Form, Query
from fastapi.responses import FileResponse
from api.services.openai_service import generate_chat, list_files, retrieve_file_info, delete_file, analyze_file, generate_tts
import fitz  # Ensure PyMuPDF is installed

router = APIRouter()


@router.get("/")
def read_root():
    return generate_chat()


@router.post("/analyze-file")
def upload(file: UploadFile = File(...), additional_text: str = Form(...)):
    if file.content_type == "application/pdf":
        # Extract text from PDF
        pdf_document = fitz.open(stream=file.file.read(), filetype="pdf")
        file_content = ""
        for page_num in range(pdf_document.page_count):
            page = pdf_document.load_page(page_num)
            file_content += page.get_text()
    else:
        # Handle other file types (e.g., text files)
        file_content = file.file.read().decode('utf-8')
    
    response = analyze_file(file_content=file_content, text_prompt=additional_text)
    return response


@router.get("/files")
def get_files():
    files = list_files()
    return files


@router.get("/files/{file_id}")
def get_file_info(file_id: str):
    file_info = retrieve_file_info(file_id)
    return file_info


@router.delete("/files/{file_id}")
def remove_file(file_id: str):
    response = delete_file(file_id)
    return response

# curl "http://localhost:8000/tts?input_text=The true size of India.&file_name=speech_india.mp3"


@router.get("/tts")
def text_to_speech(input_text: str = Query(""), file_name: str = Query("")):
    speech_file_path = generate_tts(file_name=file_name, input_text=input_text)
    return FileResponse(speech_file_path)
