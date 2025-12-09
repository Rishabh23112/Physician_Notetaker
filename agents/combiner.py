def combine_outputs(medical_summary, sentiment_intent, soap_note):
    return {
        "Medical_Summary": medical_summary,
        "Sentiment_Intent": sentiment_intent,
        "SOAP_Note": soap_note,
    }
