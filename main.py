from fastapi import FastAPI
from api.routes import root, items

app = FastAPI()

app.include_router(root.router)
app.include_router(items.router)