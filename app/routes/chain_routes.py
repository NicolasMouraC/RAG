from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from app.utils.chain import chain

class QueryRequest(BaseModel):
    query: str

chain_routes = APIRouter()

@chain_routes.post("/get-response", status_code=status.HTTP_200_OK)
def get_response(request: QueryRequest):
    from app.utils.vector_store import db
    if db is None:
        raise HTTPException(status_code=500, detail="Vector store is not initialized.")

    response = chain(request.query, db)
    if not response:
        raise HTTPException(status_code=500, detail="Model error.")

    return {"response": response}
