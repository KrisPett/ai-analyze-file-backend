from typing import Union
from fastapi import APIRouter
from api.models.item import Item
from api.services.items_service import get_item, update_item

router = APIRouter()

@router.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return get_item(item_id, q)

@router.put("/items/{item_id}")
def update_item_route(item_id: int, item: Item):
    return update_item(item_id, item)