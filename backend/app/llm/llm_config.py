from langchain_google_genai import ChatGoogleGenerativeAI

import os
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(

    model="gemini-2.5-flash",

    temperature=1.0,  # Gemini 3.0+ defaults to 1.0

    api_key=os.getenv("GEMINI_API_KEY")



)