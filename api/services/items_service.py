# src/services/items_service.py
from typing import Union
from api.models.item import Item

def get_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}