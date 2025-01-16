from fastapi import APIRouter, UploadFile, File
from api.services.openai_service import generate_chat, upload_file, list_files, retrieve_file_info, delete_file

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
