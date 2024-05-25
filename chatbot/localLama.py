from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
## Langsmith tracking
os.environ['LANGCHAIN_TRACING_V2'] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant.Please respond to the user queries"),
        ("user","Question:{question}")
    ]
)

st.title("Langchain Demo with ollama API")
input_text = st.text_input("search the topic u want")

## here we use llama2
llm = Ollama(model = "llama2")
output_parser = StrOutputParser()


chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question' : input_text}))