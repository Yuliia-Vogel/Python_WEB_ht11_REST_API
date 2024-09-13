from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers import contacts

app = FastAPI()

origins = [
    "http://localhost:3000",
    "localhost:3000"
] # це для фронту, це список, звідки можна стукатися, тут описаний локалхот 3000, це той, який має node-додаток
# (він тут є зі схемою і без схеми)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
) # для фронту, ососбливо важливо тут CORSMiddleware

app.include_router(contacts.router, prefix="/api")

@app.get("/") 
async def root(): # привітальне повідомлення за адресою http://127.0.0.1:8000/
    return {
        "message": "Hello Contact API",
        "status": "Ok"
    }
