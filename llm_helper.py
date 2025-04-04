from dotenv import load_dotenv
from langchain_groq import ChatGroq
import os

load_dotenv()

llm = ChatGroq(groq_api_key = os.getenv("GROQ_API_KEY"), model_name = "llama-3.3-70b-specdec")

if __name__ == "__main__":
    response = llm.invoke("What is the ranking of UT Dallas in the US for Computer Engineering program?")
    print(response.content)