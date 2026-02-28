from fastapi import FastAPI
from pydantic import BaseModel
from agent import ask_agent

app = FastAPI()

class Query(BaseModel):
    question: str
@app.post("/ask")
def ask(query: Query):
    try:
        answer = ask_agent(query.question)
        return {"response": answer}
    except Exception as e:
        return {"error": str(e)}


@app.get("/")
def home():
    return {"message": "Titanic Chatbot API is running 🚢"}