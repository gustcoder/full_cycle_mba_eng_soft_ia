from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
load_dotenv()

question_template = """
Retorne quantos títulos este piloto tem: {rider_name}
"""

prompt = PromptTemplate(template=question_template, input_variables=["rider_name"])

openai_key = os.getenv("OPENAI_API_KEY")
model = ChatOpenAI(
    model="gpt-4o-mini",
    api_key=openai_key
)

chain = prompt | model
result = chain.invoke(
    {
        "rider_name": "Ricky Carmichael"
    }
)

print(result.content)