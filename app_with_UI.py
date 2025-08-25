# Imports
from dotenv import load_dotenv
from langchain_groq import ChatGroq
import streamlit as st

load_dotenv() 


llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.0,
    max_retries=2
)

st.set_page_config(page_title="Chat App", page_icon="*")
st.title("Chat Application using Groq")

st.sidebar.header("Settings")
temp = st.sidebar.slider("Temperature", 0.0, 1.0, 0.1)

llm.temperature = temp

user_input = st.text_input('Ask me anything...', "")
user_input = user_input.strip()

if user_input:
  messages = [
      ("system", "You are a helpful knowledge assistant."),
      ("human", f"{user_input}"),
  ]

  with st.spinner("Thinking..."):
    result = llm.invoke(messages)

  st.markdown("### Answer: ")
  st.write(result.content)
