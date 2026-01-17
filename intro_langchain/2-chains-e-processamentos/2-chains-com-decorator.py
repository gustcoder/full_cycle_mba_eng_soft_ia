from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.runnables import chain
from dotenv import load_dotenv
import os
load_dotenv()

@chain
def select_winspector_hero(color:str) -> dict:
    hero = ""
    match color:
        case "red": hero = "Fire"
        case "yellow": hero = "Biker"
        case "green": hero = "Highter"
        case _:
            hero = "Junko"
    return {"hero": hero}    

question_template = """
Resuma em 1 frase o personagem {hero} de Tokkei Winspector.
"""

prompt = PromptTemplate(template=question_template, input_variables=["hero"])

openai_key = os.getenv("OPENAI_API_KEY")
model = ChatOpenAI(
    model="gpt-4o-mini",
    api_key=openai_key
)

chain = select_winspector_hero | prompt | model
result = chain.invoke("red")

print(result.content)