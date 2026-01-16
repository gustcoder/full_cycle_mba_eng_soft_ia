from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
load_dotenv()

system = ("system", "Você é um especialista em {subject}.")
user = ("user", "{question}")

chat_prompt = ChatPromptTemplate([system, user])

messages = chat_prompt.format_messages(
    subject="Resident Evil", 
    question="Quando lança RE Requiem?"
)

for msg in messages:
    print(f"{msg.type}: {msg.content}")

openai_key = os.getenv("OPENAI_API_KEY")    

model = ChatOpenAI(model="gpt-4o-mini", api_key=openai_key)

result = model.invoke(messages)

print(result.content)
