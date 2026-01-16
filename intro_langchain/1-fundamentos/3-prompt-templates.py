from langchain_core.prompts import PromptTemplate
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
import os
load_dotenv()

template = """
Liste o website/domínio principal desta empresa em um retorno JSON com a chave "domain": {company_name}
"""

prompt = PromptTemplate(template=template, input_variables=["company_name"])

message = template.format(company_name="Amazon")

print(message)

gemini_key = os.getenv("GEMINI_API_KEY")
model = init_chat_model(
    model="gemini-2.5-flash",
    model_provider="google_genai",
    api_key=gemini_key
)

result = model.invoke(message)

print(result.content)