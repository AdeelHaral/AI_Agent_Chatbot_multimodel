# 🤖 AI Agent using LangChain, LangGraph & FastAPI

An intelligent and customizable AI chatbot agent built using [LangChain](https://www.langchain.com/), [LangGraph](https://github.com/langchain-ai/langgraph), and [FastAPI](https://fastapi.tiangolo.com/). This project supports multi-provider LLMs like **OpenAI** and **Groq**, and includes optional **agentic web search** via the **Tavily API**.

---

## 🧠 Features

✅ Supports LLM providers: **OpenAI** and **Groq**  
✅ Dynamic web search integration using **TavilySearch**  
✅ Fully customizable **system prompts**  
✅ Agent-based reasoning using **LangGraph’s ReAct architecture**  
✅ Lightweight **FastAPI** backend  
✅ Interactive **Streamlit** frontend  
✅ Easy to extend and deploy

---

## 📸 UI Preview

![Streamlit UI Screenshot](https://github.com/your-username/ai-agent-langgraph/assets/example-ui.png) <!-- Replace with actual screenshot URL -->

---

## 🧰 Tech Stack

- **LangChain** & **LangGraph** for LLM orchestration
- **OpenAI GPT-4o** and **Groq LLaMA 3.3 70B**
- **TavilySearch Tool** for external web search
- **FastAPI** for backend service
- **Streamlit** for frontend UI
- **Pydantic**, **Uvicorn**, and **Requests**

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/ai-agent-langgraph.git
cd ai-agent-langgraph
2. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
Note: You will need API keys for OpenAI, Groq, and Tavily. Add them to a .env file in the root directory:

bash
Copy
Edit
OPENAI_API_KEY=your_openai_api_key
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
3. Start the Backend
bash
Copy
Edit
uvicorn main:app --reload --port 9999
4. Launch the Frontend
bash
Copy
Edit
streamlit run app.py
📡 API Endpoint
POST /chat
Send a chat request with model, provider, prompt, and search preference.

Example JSON:
json
Copy
Edit
{
  "model_name": "gpt-4o-mini",
  "model_provider": "OpenAI",
  "system_prompt": "Act as a smart travel assistant.",
  "messages": ["Plan a 3-day trip to Berlin."],
  "allow_search": true
}
🎯 Use Cases
🧑‍🏫 AI Language Tutor

🧠 Knowledge Expert with Web Access

🤖 Task-oriented Custom Agent

📈 Business Assistant or Data Query Bot

🛠️ Customize It
You can easily plug in:

New models (e.g., Claude, Gemini)

Custom tools or APIs

Advanced LangGraph workflows

Memory or long-term context management

📝 License
This project is licensed under the MIT License.
See LICENSE for details.

💡 Acknowledgments
LangChain

LangGraph

Tavily API

OpenAI

Groq


