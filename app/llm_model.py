import os
import sys
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.prompt_template import get_prompt
load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-pro", temperature=1, google_api_key=os.getenv("GEMINI_API_KEY"))
def model_response(weather:str, money:str, money_value:str, location:str, dates:str) -> str:
    prompt = get_prompt(weather, money, money_value, location, dates)
    return model.invoke(prompt).content