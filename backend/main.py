from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
import google.generativeai as genai
from fastapi.responses import FileResponse
import os

from backend.parser import extract_text_from_pdf
from backend.analyzer import analyze_resume
from backend.report import generate_pdf_report

app = FastAPI(title="AI Resume Analyser")

# Enable CORS for frontend to talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def health_check():
    return {"status": "running"}

@app.get("/debug-models")
def list_available_models():
    try:
        models = [m.name for m in genai.list_models()]
        return {"models": models}
    except Exception as e:
        return {"error": str(e)}

@app.post("/analyze")
async def analyze_endpoint(
    resume: UploadFile = File(...),
    job_description: str = Form(...)
):
    # Read PDF bytes
    file_bytes = await resume.read()
    
    # Parse PDF text
    try:
        resume_text = extract_text_from_pdf(file_bytes)
    except Exception as e:
        return {"error": f"Failed to read PDF file: {str(e)}"}
    
    # Analyze using Gemini
    result_json = analyze_resume(resume_text, job_description)
    
    return result_json

@app.post("/download-report")
async def download_report(result: dict):
    # Call report generator
    pdf_path = generate_pdf_report(result)
    
    return FileResponse(
        path=pdf_path,
        filename="resume_analysis_report.pdf",
        media_type="application/pdf"
    )
