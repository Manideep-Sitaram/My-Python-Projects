import getpass
import os
from langchain_google_genai import ChatGoogleGenerativeAI

import streamlit as st


if "GOOGLE_API_KEY" not in os.environ:
    os.environ["GOOGLE_API_KEY"] = getpass.getpass(os.getenv("GOOGLE_API_KEY"))

st.title("Langchain Demo with Gemini API")
input_text = st.text_input("Search the topic you want")

llm = ChatGoogleGenerativeAI(model="gemini-pro")

if input_text:
    st.write(llm.invoke(input_text))
