import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

from langchain_experimental.agents import create_pandas_dataframe_agent
from langchain_groq import ChatGroq

# Load dataset
df = pd.read_csv(r"E:\\internshala\\Titanic BOT\\Titanic-Dataset.csv")

# Use Groq LLaMA model
llm = ChatGroq(
  model="llama-3.3-70b-versatile",
    temperature=0
)

agent = create_pandas_dataframe_agent(
    llm,
    df,
    verbose=True,
    allow_dangerous_code=True,
    handle_parsing_errors=True
)

def ask_agent(question):
    result = agent.invoke({"input": question})
    return result["output"]