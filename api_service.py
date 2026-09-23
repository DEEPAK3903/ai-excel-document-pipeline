from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
import shutil
import os
from pdf_extractor import extract_pdf_text
from ai_parser import AIDocumentParser
from excel_builder import build_excel_report

app = FastAPI(
    title="AI Document Intelligence & Excel Automation Pipeline",
    description="REST API service for extracting unstructured PDF data using PyMuPDF & Gemini AI, generating structured Excel reports.",
    version="1.0.0"
)

TEMP_DIR = "temp_uploads"
os.makedirs(TEMP_DIR, exist_ok=True)

parser = AIDocumentParser()

@app.get("/")
def read_root():
    return {
        "status": "Online",
        "service": "AI Document Intelligence & Excel Pipeline API",
        "documentation": "/docs"
    }

@app.post("/api/process-pdf")
async def process_pdf_endpoint(file: UploadFile = File(...)):
    """
    Upload a PDF document.
    Extracts text via PyMuPDF, parses structured JSON via Gemini AI, and returns Excel report.
    """
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are supported.")
        
    temp_filepath = os.path.join(TEMP_DIR, file.filename)
    with open(temp_filepath, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
        
    # Step 1: Extract PDF Text
    raw_text = extract_pdf_text(temp_filepath)
    if not raw_text:
        raise HTTPException(status_code=500, detail="Failed to extract text from PDF.")
        
    # Step 2: Parse JSON using AI
    structured_json = parser.parse_document(raw_text)
    
    # Step 3: Build Excel Report
    excel_filename = f"report_{os.path.splitext(file.filename)[0]}.xlsx"
    excel_path = build_excel_report(structured_json, excel_filename)
    
    return {
        "filename": file.filename,
        "extracted_data": structured_json,
        "excel_report": excel_filename,
        "status": "Success"
    }
