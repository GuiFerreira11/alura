import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = str(os.getenv("API_KEY"))

genai.configure(api_key=api_key)

generation_config = {
  "temperature": 0.9,
  "top_p": 0.95,
  "top_k": 32,
}

safety_setting = {
  "HARASSMENT": "BLOCK_NONE",
  "HATE": "BLOCK_NONE",
  "SEXUAL": "BLOCK_NONE",
  "DANGEROUS": "BLOCK_NONE",
}

model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_setting)

chat = model.start_chat(history=[])

prompt = input("Esperando um prompt: ")

while prompt != "fim":
    response = chat.send_message(prompt)
    print(f'Resposta: {response.text}\n')
    prompt = input("Esperando um prompt: ")
