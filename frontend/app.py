import streamlit as st
import requests

st.title("🚢 Titanic Dataset Chatbot")

question = st.text_input("Ask a question about Titanic dataset")

if st.button("Ask"):
    response = requests.post(
        "http://127.0.0.1:8000/ask",
        json={"question": question}
    )

    if response.status_code == 200:
        # st.write(response.json()["response"])
        st.write(response.json())