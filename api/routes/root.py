from fastapi import APIRouter

from api.services.openai_service import generate_chat

router = APIRouter()


@router.get("/")
def read_root():
    return generate_chat()
