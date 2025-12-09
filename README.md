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

## <img width="35" height="35" alt="image" src="https://github.com/user-attachments/assets/91b31014-9e0f-42ab-850c-39f95e32d581" /> Images
<img width="600" height="384" alt="phy3" src="https://github.com/user-attachments/assets/8c4bc313-1e52-422f-853e-776913d4d8db" />
<img width="600" height="384" alt="phy2" src="https://github.com/user-attachments/assets/b48c8584-7140-4d29-a693-0bbec113ec50" />
<img width="600" height="384" alt="Phy1" src="https://github.com/user-attachments/assets/32e3f00c-bc95-474b-a0d4-8354a7af9e2b" />





## 📦 Installation

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/Rishabh23112/Physician_Notetaker.git
    cd Physician_Notetaker
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
