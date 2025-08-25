# Groq Chat Application with Streamlit

## Overview
This project is a simple chat application built using **Groq LLM** (via LangChain) and **Streamlit** for the user interface.  
It allows users to interact with the Llama 3.1 model hosted on Groq through a clean web-based interface.  

The application supports adjustable parameters (e.g., temperature) via a sidebar and can be extended into a more advanced chatbot.

---

## Features
- Built with **Streamlit** for a lightweight and responsive UI.
- Powered by **Groq LLM** using the `langchain_groq` integration.
- Supports **Llama 3.1 model** (`llama-3.1-8b-instant`).
- Adjustable **temperature** from sidebar for controlling creativity.
- Simple text input for asking questions and displaying responses.

---

## Tech Stack
- Python  
- Streamlit  
- LangChain  
- Groq API  

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/groq-chat-streamlit.git
   cd groq-chat-streamlit

## Create & activate virtual environment
python -m venv .venv
source .venv/Scripts/activate

## Install dependencies:
pip install -r req.txt

Add your Groq API Key:

Create a .env file in the project root.

Running the Application

Start the Streamlit app:
streamlit run app_with_UI.py



