from fastapi import FastAPI, UploadFile, File, HTTPException, Header
from fastapi.middleware.cors import CORSMiddleware
from concurrent.futures import ThreadPoolExecutor
from docx import Document
import io
import uvicorn
from contextlib import asynccontextmanager

# Import agents
from agents.medical_summarizer import medical_summarize
from agents.sentiment_analyzer import analyze_sentiment_intent
from agents.soap_generator import generate_soap_note
from agents.combiner import combine_outputs

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup logic
    yield
    # Shutdown logic
    executor.shutdown()

app = FastAPI(lifespan=lifespan)

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

executor = ThreadPoolExecutor(max_workers=3)

def read_file_content(file_content: bytes, filename: str) -> str:
    """Reads content from bytes based on extension."""
    if filename.endswith(".txt"):
        return file_content.decode("utf-8")
    elif filename.endswith(".docx"):
        try:
            doc = Document(io.BytesIO(file_content))
            return "\n".join([para.text for para in doc.paragraphs])
        except Exception as e:
            raise ValueError(f"Error reading docx: {e}")
    else:
        raise ValueError("Unsupported file format")

@app.post("/process")
async def process_file(
    file: UploadFile = File(...),
    x_gemini_api_key: str = Header(None)
):
    
    print(f"Received file upload request: {file.filename}")
    if not (file.filename.endswith(".txt") or file.filename.endswith(".docx")):
        print(f"Rejected file type: {file.filename}")
        raise HTTPException(status_code=400, detail="Invalid file type. Only .txt and .docx supported.")

    try:
        content = await file.read()
        print(f"Read {len(content)} bytes from file.")
        text = read_file_content(content, file.filename)
        print("Successfully extracted text content.")
    except Exception as e:
        print(f"Error processing file: {e}")
        raise HTTPException(status_code=400, detail=str(e))

    future_medical = executor.submit(medical_summarize, text, x_gemini_api_key)
    future_sentiment = executor.submit(analyze_sentiment_intent, text, x_gemini_api_key)
    future_soap = executor.submit(generate_soap_note, text, x_gemini_api_key)

    medical_summary = future_medical.result()
    sentiment_intent = future_sentiment.result()
    soap_note = future_soap.result()

    final_output = combine_outputs(medical_summary, sentiment_intent, soap_note)
    return final_output

@app.get("/health")
def health_check():
    return {"status": "ok", "service": "Physician Notetaker Backend"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
