from langchain_openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

llm = OpenAI(model="gpt-3.5-turbo", temperature=0.9, openai_api_key=openai_api_key)
response = llm.invoke("What is the capital of France?")
print(response)