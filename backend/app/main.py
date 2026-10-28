from fastapi import FastAPI
from pydantic import BaseModel #provides data vlaidation



app = FastAPI() #creates a fastapi application object and stores it in app
class QuestionRequest(BaseModel):
    question: str

@app.get("/health")
def health_check():
    return {                     #returns a dictionary
        "status": "healthy"
    }

@app.get("/documents")
def list_documents(limit: int = 10):
    return {
        "limit" : limit,
        "documents": ["README.md", "api_docs.md"]
    }

@app.get("/documents/{document_id}")
def get_document(document_id: int):
    return {
        "document_id" : document_id,
        "filename" : "README.md"
    }

@app.post("/ask")
def ask_question(request: QuestionRequest):
    return {
        "recieved_question": request.question
    }