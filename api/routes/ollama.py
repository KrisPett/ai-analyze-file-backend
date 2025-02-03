from fastapi import APIRouter, UploadFile, File, Form, Query
from fastapi.responses import FileResponse, StreamingResponse
from api.services.ollama_service import generate_chat, analyze_file
import fitz

router = APIRouter()

@router.get("/ollama")
def ollama_chat():
    def chat_generator():
        for message in generate_chat():
            yield message + "\n"

    return StreamingResponse(chat_generator(), media_type="text/event-stream")

@router.post("/ollama/analyze-file")
def upload(file: UploadFile = File(...), additional_text: str = Form(...)):
    print("ollama")
    if file.content_type == "application/pdf":
        pdf_document = fitz.open(stream=file.file.read(), filetype="pdf")
        file_content = ""
        for page_num in range(pdf_document.page_count):
            page = pdf_document.load_page(page_num)
            file_content += page.get_text()
    else:
        file_content = file.file.read().decode('utf-8')
    
    response = analyze_file(file_content=file_content, text_prompt=additional_text)
    return response

