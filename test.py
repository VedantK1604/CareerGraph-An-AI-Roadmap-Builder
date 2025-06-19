from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st
import os

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash-lite")
result = llm.invoke("Generate a roadmap to become a IAS officer in India.").content

st.title("Demo Site")

st.markdown(result)
