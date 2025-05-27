import streamlit as st
import requests





#step 1 is establishing our UI to interact with backend
st.set_page_config(page_title="AI AGENT USING LANGCHAIN AND LANGGRAPH",layout='centered')
st.title("AI AGENT USING LANGCHAIN (LLMS) AND LANGGRAPH")
st.write("Create and interact with AI Agents")
system_prompt = st.text_area("Define your AI Agent",height=70,placeholder="Eg Act as Language Expert.....")
grog_model=['llama-3.3-70b-versatile']
openai_model = ['gpt-4o-mini']

Provider=st.radio("Select Provider:",("Groq","OpenAI"))
if Provider=="Groq":
    selected_model = st.selectbox("selected Groq Model",grog_model)
elif Provider=="OpenAI":
    selected_model = st.selectbox("Select OpenAI Model", openai_model)
#setup connect with URL that is my local host
allow_search = st.checkbox("Allow Websearch Using the Model (AGentic Search Functionality )")
user_query = st.text_area("Enter you query what you want to know : ",height=150, placeholder="enter anything I am here to help....")
Api_URL= 'http://127.0.0.1:9999/chat'
if st.button("Ask Agent"):
    if user_query.strip():
        st.subheader("Agentic Response")
        payload={
            "model_name": selected_model,
            "model_provider": Provider,
            "system_prompt":system_prompt,
            "messages":[user_query],
            "allow_search": allow_search}
        response=requests.post(Api_URL,json=payload)
        if response.status_code==200:
            response_data = response.json()
            if "error" in response_data:
                st.error(response_data['error'])
            else:
                st.subheader(response_data)
        else:
            st.subheader("error with FastAPI post Request")
        
    else:
        response="Enter You valid Query"