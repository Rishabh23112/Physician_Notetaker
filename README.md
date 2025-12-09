# 🩺 Physician Notetaker

An AI-powered application for **medical transcription summarization, SOAP note generation, and sentiment analysis**.

## 🚀 Features
- **Medical Summarization**: Extracts key symptoms, diagnosis, treatment, and prognosis.
- **Sentiment & Intent Analysis**: Analyzes patient sentiment (e.g., Anxious, Reassured) and underlying intent.
- **SOAP Note Generation**: Automatically structures conversation into Subjective, Objective, Assessment, and Plan.

## 🛠 Tech Stack
- **Backend**: FastAPI
- **Frontend**: Streamlit
- **AI Model**: Google Gemini 2.5 Flash (via `google-generativeai`)



## 📦 Installation

1.  **Clone the repository**:
    ```bash
    git clone <repo-url>
    cd Physician_Notetaker-main
    ```

2.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```



## ▶️ Running the Application

1.  **Start the Backend (FastAPI)**:
    ```bash
    uvicorn main:app --reload
    ```
    *Server will start at `http://127.0.0.1:8000`*

2.  **Start the Frontend (Streamlit)**:
    ```bash
    streamlit run streamlit_app.py
    ```
    *App will open in your browser at `http://localhost:8501`*

## 🧪 Usage
1.  Open the Streamlit app.
2.  Enter your **Gemini API Key**.
3.  Upload a patient transcript (`.txt` or `.docx` or `.pdf`).
4.  View the generated **Medical Summary**, **Sentiment Analysis**, and **SOAP Note**.