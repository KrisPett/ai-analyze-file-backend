from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes import root, items

app = FastAPI()

# Allow CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"], 
)

app.include_router(root.router)
app.include_router(items.router)