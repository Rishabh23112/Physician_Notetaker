import streamlit as st
import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

BACKEND_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="Physician Notetaker",
    page_icon="🩺",
    layout="wide"
)

def main():
    st.title("🩺 Physician Notetaker")
    st.markdown("### AI-Powered Medical Summarization & SOAP Note Generator")

    # Sidebar for API Key 

    api_key = st.sidebar.text_input("Enter Gemini API Key", type="password")
    if api_key:
        os.environ["GEMINI_API_KEY"] = api_key
    else:
        st.warning("Please provide a Gemini API Key to proceed.")
        st.stop()
    
    # File Upload
    uploaded_file = st.file_uploader("Upload Patient Transcript", type=["txt", "docx", "pdf"])

    if uploaded_file is not None:
        st.info("File uploaded successfully. Processing...")
        
        if st.button("Generate Reports"):
            with st.spinner("Analyzing conversation..."):
                try:
                    files = {"file": (uploaded_file.name, uploaded_file.getvalue(), "multipart/form-data")}
                    
                    st.write(f"Sending file: {uploaded_file.name} to {BACKEND_URL}/process") # Debug info
                    
                    headers = {}
                    if api_key:
                        headers["x-gemini-api-key"] = api_key

                    response = requests.post(f"{BACKEND_URL}/process", files=files, headers=headers)
                    
                    if response.status_code == 200:
                        data = response.json()
                        display_results(data)
                    else:
                        st.error(f"Backend Error ({response.status_code}): {response.text}")
                except requests.exceptions.ConnectionError:
                    st.error(f"Could not connect to backend at {BACKEND_URL}. Is 'uvicorn main:app' running?")
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")

def display_results(data):
    # Tabs
    tab1, tab2, tab3 = st.tabs(["📄 SOAP Note", "📊 Medical Summary", "🧠 Sentiment Analysis"])

    with tab1:
        st.header("SOAP Note")
        soap = data.get("SOAP_Note", {})
        
        if isinstance(soap, dict) and "error" in soap:
             st.error(f"SOAP Generation Error: {soap['error']}")
             with st.expander("Raw Response"):
                 st.code(soap.get("raw_response", "No response data"))
        else:
            st.code(json.dumps(soap, indent=2), language="json")

    with tab2:
        st.header("Medical Summary")
        summary = data.get("Medical_Summary", {})
        st.code(json.dumps(summary, indent=2), language="json")

    with tab3:
        st.header("Sentiment & Intent")
        sentiment = data.get("Sentiment_Intent", {})
        st.code(json.dumps(sentiment, indent=2), language="json")

if __name__ == "__main__":
    main()
