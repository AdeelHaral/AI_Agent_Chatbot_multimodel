from dotenv import load_dotenv
load_dotenv()
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.prompts import PromptTemplate
from langgraph.prebuilt import create_react_agent
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages.ai import AIMessage

openai_llm = ChatOpenAI(model='gpt4-4o-mini')
groq_llm = ChatGroq(model="llama-3.3-70b-versatile")



System_prompt="Act as AI chatbot who is smart and friendly"
#setup AI Agent using LAnggraph
def get_response_aiagent(llm_id,query,allow_search,system_prompt,provider):
    if provider=="Groq":
        llm=ChatGroq(model=llm_id)
    elif provider=="OpenAI":
        llm=ChatOpenAI(model=llm_id)
    tools_sear = [TavilySearchResults(max_results=2)] if allow_search else []

    agent = create_react_agent(
        model=llm,
        tools= tools_sear,
        prompt=system_prompt
        )

    state={"messages":query}
    response = agent.invoke(state)
    messages = response.get("messages") 
    ai_messages = [message.content for message in messages if isinstance(message,AIMessage)]
    return ai_messages[-1]
