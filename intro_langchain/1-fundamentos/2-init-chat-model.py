from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
import os
load_dotenv()

gemini_key = os.getenv("GEMINI_API_KEY")

gemini = init_chat_model(
    model="gemini-2.5-flash",
    model_provider="google_genai",
    api_key=gemini_key
)

answer_gemini = gemini.invoke("Iniciando integração com Gemini!")
print(answer_gemini.content)
