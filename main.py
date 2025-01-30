# main.py
import os
from dotenv import load_dotenv
import requests
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Load environment variables from .env file
load_dotenv()

# API key from environment
API_KEY = os.getenv("APIKEY")
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"  

# FastAPI app initialization
app = FastAPI()

# Pydantic model for input data
class TranslationRequest(BaseModel):
    text: str

# Function to call the Groq API for translation
def translate_text(text: str) -> str:
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }
    data = {
        "model": "llama-3.3-70b-versatile",
        "messages": [
            {
                "role": "system",
                "content": "Translate the following text to Finnish:"
            },
            {
                "role": "user",
                "content": text
            }
        ],
    }
    response = requests.post(GROQ_API_URL, json=data, headers=headers)
    
    if response.status_code == 200:
        return response.json().get("choices")[0].get("message").get("content")
    else:
        raise HTTPException(status_code=response.status_code, detail="Translation failed")

# FastAPI endpoint for translation
@app.post("/translate/")
async def translate(request: TranslationRequest):
    translated_text = translate_text(request.text)
    return {"original_text": request.text, "translated_text": translated_text}

# To run the FastAPI server with: uvicorn main:app --reload