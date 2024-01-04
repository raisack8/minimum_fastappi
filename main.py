from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.apis import test_api

app = FastAPI()
origins = [
    "http://localhost:3000",
]

# CORSミドルウェアの設定
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"], 
)

app.include_router(test_api.router, tags=["tests"])