import requests
import streamlit as st

def get_openai_response(input_text):
    response = requests.post("http://localhost:8000/essay/invoke",
    json={'input':{'topic':input_text}})

    return response.json()['output']['content']


def get_ollama_response(input_text):
    response = requests.post("http://localhost:8000/poem/invoke",
    json={'input':{'topic':input_text}})
    print(response)
    return response.json()['output']['content']

st.title("Langchain Demo with LLAMA2 api")
input_text_1 = st.text_input("Write an essay on")
input_text_2 = st.text_input("Write a poem on")

if input_text_1:
    st.write(get_OpenAI_response(input_text_1))
if input_text_2:
    st.write(get_ollama_response(input_text_2))