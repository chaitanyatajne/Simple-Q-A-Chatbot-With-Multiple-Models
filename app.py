# Importing Required Libraries
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain.prompts import ChatPromptTemplate
import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
LANGCHAIN_API_KEY = st.secrets['LANGCHAIN_API_KEY']
LANGCHAIN_TRACING_V2 = "true"
LANGCHAIN_PROJECT = "Simple Q&A Chatbot with Multiple Models"

# Setting Up Environment Variables
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "Simple Q&A Chatbot with Multiple Models"

# Creating Prompt Template
prompt = ChatPromptTemplate.from_messages([
    ("system", "Answer the following questions"),
    ("user", "Question:{question}")
])

# Function to Generate Response
def generate_response(question, api_key, engine, temperature):
    llm = ChatGroq(model=engine, api_key=api_key, temperature=temperature)
    output = StrOutputParser()
    chain = prompt | llm | output
    answer = chain.invoke({"question":question})
    return answer

# List of Available Models
model_list = ["gemma-7b-it", "llama-3.1-8b-instant", "mixtral-8x7b-32768", "whisper-large-v3-turbo"]

# Streamlit Web App Setup
st.title("Simple Q&A Chatbot with Multiple Models")

# Sidebar Settings
st.sidebar.title("Settings")
api_key = st.sidebar.text_input("Enter API Key:", type='password')
model = st.sidebar.selectbox("Select Model", options=model_list)
temperature = st.sidebar.slider("Select Temperature", min_value=0.00, max_value=1.00, step=0.01)

# Main Content
st.write("Ask your question")
user_input = st.text_input("Enter Text")

# Displaying Response
if user_input and api_key:
    response = generate_response(user_input, api_key, model, temperature)
    st.write(response)
elif user_input:
    st.warning('Please enter API key')
else:
    st.warning("Please enter your question")
