import streamlit as st
import ollama
st.title("💬 CodeLess - Your Personalized Coding Assistant")
prompt = st.text_input('Enter your prompt')
response = ollama.generate(model='codeless',prompt=prompt)
st.write(response['response'])