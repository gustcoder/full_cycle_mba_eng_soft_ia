from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
load_dotenv()

openai_key = os.getenv("OPENAI_API_KEY")

model = ChatOpenAI(model="gpt-4o-mini", api_key=openai_key)

result = model.invoke("Começando intro a LangChain!")

print(result.content)
