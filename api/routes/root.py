from fastapi import APIRouter, UploadFile, File
from api.services.openai_service import generate_chat, upload_file

router = APIRouter()


@router.get("/")
def read_root():
    return generate_chat()


@router.post("/analyze-file")
def upload(file: UploadFile = File(...)):
    file_location = f"/tmp/{file.filename}"
    with open(file_location, "wb+") as file_object:
        file_object.write(file.file.read())
    response = upload_file(file_location)
    return response


# @router.get("/analyze/{file_id}")
# def analyze(file_id: str):
#     response = analyze_file(file_id)
#     return response
