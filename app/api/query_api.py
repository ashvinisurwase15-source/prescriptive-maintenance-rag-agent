from fastapi import APIRouter
from app.models.query_request import QueryRequest
from app.rag.retriever import search_documents

router = APIRouter()

@router.post("/query")
def query_documents(request: QueryRequest):

    results = search_documents(request.query)

    return {
        "results": results
    }