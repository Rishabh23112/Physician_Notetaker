import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if api_key:
    genai.configure(api_key=api_key)

def call_gemini(prompt, api_key=None):
    try:
        if api_key:
            genai.configure(api_key=api_key)
            
        print(f"DEBUG: calling gemini with prompt length: {len(prompt)}")
        model = genai.GenerativeModel('gemini-2.5-flash')
        response = model.generate_content(prompt)
        print(f"DEBUG: gemini response: {response.text[:100]}...")
        return response.text.strip()
    except Exception as e:
        error_msg = f"Error communicating with Gemini: {str(e)}"
        print(error_msg)
        return error_msg
