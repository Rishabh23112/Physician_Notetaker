import json
import re
from utils import call_gemini

def medical_summarize(transcript, api_key=None):
    prompt = (
        "You are an expert medical AI. Extract key medical details from the transcript.\n"
        "Keep values short, precise, and extract only key information.\n"
        "Output strictly as a valid JSON object with this exact structure:\n"
        "{\n"
        '  "Patient_Name": "Name or Not specified",\n'
        '  "Symptoms": ["Symptom 1", "Symptom 2"],\n'
        '  "Diagnosis": "...",\n'
        '  "Treatment": ["Treatment 1", "Treatment 2"],\n'
        '  "Current_Status": "...",\n'
        '  "Prognosis": "..."\n'
        "}\n"
        "Do not use markdown formatting. Return only the JSON.\n"
        f"Transcript:\n{transcript}"
    )
    response = call_gemini(prompt, api_key)
    raw_response = response
    response = re.sub(r"```json\n|\n```", "", response).strip()

    try:
        return json.loads(response)
    except json.JSONDecodeError:
        return {"error": "Failed to parse JSON", "raw_response": raw_response}
