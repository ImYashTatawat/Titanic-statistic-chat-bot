import streamlit as st
import pandas as pd
import os
from langchain_experimental.agents import create_pandas_dataframe_agent
from langchain_groq import ChatGroq

st.title("Titanic Statistics Chatbot")

df = pd.read_csv("Titanic-Dataset.csv")

groq_api_key = st.secrets["GROQ_API_KEY"]

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    groq_api_key=groq_api_key
)
agent = create_pandas_dataframe_agent(
    llm,
    df,
    verbose=True,
    allow_dangerous_code=True
)
question = st.text_input("Ask a question about Titanic dataset")

if st.button("Ask"):
    answer = agent.run(question)
    st.write(answer)





