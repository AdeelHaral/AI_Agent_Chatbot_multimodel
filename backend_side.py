from typing import List
from pydantic import BaseModel
from fastapi import FastAPI
from ai_agents import get_response_aiagent


class RequestState(BaseModel):
    model_name: str
    model_provider: str
    system_prompt: str
    messages: List[str]
    allow_search: bool


app = FastAPI(title="LangGraph AI AGENT")
allowed_model_names = ["gpt-4o-mini", "llama-3.3-70b-versatile", "llama3-70b-8192", "mistral-saba-24b"]


@app.post("/chat")
def chat_endpoint(request: RequestState):
    """
    API endpoint to interact with chatbot using langGraph and search tool dynamically selects
    """
    if request.model_name not in allowed_model_names:
        return {"error": "invalid AI model selected"}

    llm_id = request.model_name
    query = request.messages
    allow_search = request.allow_search
    system_prompt = request.system_prompt
    provider = request.model_provider

    response = get_response_aiagent(llm_id, query, allow_search, system_prompt, provider)
    return response


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=9999)
