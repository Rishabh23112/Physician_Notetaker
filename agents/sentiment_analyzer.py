import json
import re
from utils import call_gemini

def analyze_sentiment_intent(transcript, api_key=None):
    prompt = (
        "Analyze the patient's sentiment and intent from the transcript.\n"
        "Sentiment must be a single adjective (e.g., Anxious, Neutral, Reassured).\n"
        "Intent must be a short 2-3 word phrase.\n"
        "Output strictly as a valid JSON object with this exact structure:\n"
        "{\n"
        '  "Sentiment": "Anxious",\n'
        '  "Intent": "Seeking reassurance"\n'
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
