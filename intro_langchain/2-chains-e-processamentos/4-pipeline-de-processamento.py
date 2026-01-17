from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os
load_dotenv()

template_translate = PromptTemplate(
    input_variables=["original_text"],
    template="Traduza a seguinte frase para japonês e retorne apenas a tradução: {original_text}"
)

summarized_template = PromptTemplate(
    input_variables=["translated_text"],
    template="Resuma a seguinte frase em 5 palavras: {translated_text}"
)

openai_key = os.getenv("OPENAI_API_KEY")
model = ChatOpenAI(model="gpt-4o-mini", temperature=0.3, api_key=openai_key)

# StrOutputParser pega o resultado do modelo e transforma em uma string "runnable"
# ou seja, uma string que pode ser repassada para outra cadeia da pipeline
translate = template_translate | model | StrOutputParser()
pipeline = {"translated_text": translate} | summarized_template | model | StrOutputParser()

result = pipeline.invoke({"original_text": "Pretendo aprender japonês até o fim deste ano."})
print(result)
