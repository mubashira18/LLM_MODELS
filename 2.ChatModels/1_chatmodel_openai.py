from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
model = ChatOpenAI(model="gpt-4", temperature=0.9, openai_api_key=openai_api_key)
result = model.invoke('what is the capital of France?')
print(result)