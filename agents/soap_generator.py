import json
import re
from utils import call_gemini

def generate_soap_note(transcript, api_key=None):
    prompt = (
        "You are an expert medical scribe. Generate a professional SOAP note from the following physician-patient conversation.\n"
        "Keep the content short, precise, and clinical. Avoid unnecessary words.\n"
        "Output strictly as a valid JSON object with this exact structure:\n"
        "{\n"
        '  "Subjective": {\n'
        '    "Chief_Complaint": "...",\n'
        '    "History_of_Present_Illness": "..."\n'
        '  },\n'
        '  "Objective": {\n'
        '    "Physical_Exam": "...",\n'
        '    "Observations": "..."\n'
        '  },\n'
        '  "Assessment": {\n'
        '    "Diagnosis": "...",\n'
        '    "Severity": "..."\n'
        '  },\n'
        '  "Plan": {\n'
        '    "Treatment": "...",\n'
        '    "Follow-Up": "..."\n'
        '  }\n'
        "}\n"
        "Do not use markdown formatting. Return only the JSON.\n"
        f"Transcript:\n{transcript}"
    )
    response = call_gemini(prompt, api_key)
    
    raw_response = response
    
    # Clean markdown json
    response = re.sub(r"```json\n|```", "", response).strip()

    try:
        return json.loads(response)
    except json.JSONDecodeError:
        print(f"JSON Decode Error in SOAP. Raw: {raw_response}")
        return {"error": "Failed to parse JSON", "raw_response": raw_response}
