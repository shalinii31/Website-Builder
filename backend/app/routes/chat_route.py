from fastapi import APIRouter
from pydantic import BaseModel
from app.services.chat_service import process_query

router = APIRouter()


class Query(BaseModel):
    query: str

class ChatResponse(BaseModel):
    response:str 

@router.post("/chat")
def chat(request: Query):
    print("QUERY OF USER", request.query)
    response = process_query(request.query)

    return ChatResponse(response=response)
