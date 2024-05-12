import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = str(os.getenv("API_KEY"))

genai.configure(api_key=api_key)

# for m in genai.list_models():
#     if "generateContent" in m.supported_generation_methods:
#         print(m.name)

generation_config = {
  "temperature": 0.9,
  "top_p": 0.95,
  "top_k": 32,
  "candidate_count": 1,
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

respota = model.generate_content("Escreva um poema curto sobre química.")
print(respota.text)
