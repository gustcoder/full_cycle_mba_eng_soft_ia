from langchain.chat_models import init_chat_model
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os
load_dotenv()

gemini_key = os.getenv("GEMINI_API_KEY")

gemini = init_chat_model(
    model="gemini-2.5-flash",
    model_provider="google_genai",
    api_key=gemini_key
)

template = """
Você é um Especialista em Prospecção de Empresas. Gere informações de Nome Fantasia,
Faturamento Anual, CNPJ, Data de Função e LinkedIn sobre a seguinte empresa {company_name} 
e retorne-as em um JSON como o modelo abaixo:
{{
    "fantasyName": "",
    "annualRevenue": "",
    "cnpj": "",
    "foundedIn": "",
    "linkedinUrl": ""
}}
"""

prompt = PromptTemplate(template=template, input_variables=["company_name"])

message = template.format(company_name="AMAZON")

answer_gemini = gemini.invoke(message)
print(answer_gemini.content)
