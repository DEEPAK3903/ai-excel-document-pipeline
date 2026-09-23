# 📄 Automated Excel Processing & AI Document Intelligence Pipeline

An enterprise-grade Python pipeline designed to ingest unstructured PDF documents (invoices, receipts, healthcare claims), extract text regions using PyMuPDF, structure fields into JSON schemas using Gemini LLM/Rule-based parsers, and automatically generate formatted multi-sheet Excel reports (`OpenPyXL` & `Pandas`). Includes a `FastAPI` REST web service.

## 🚀 Key Features
- **PDF Text Extraction:** Uses `PyMuPDF` (`pymupdf`) for fast, clean text extraction across multi-page documents.
- **AI Document Structuring Engine:** Uses `google-generativeai` (Gemini API) to parse unstructured text into validated JSON payloads.
- **Rule-Based Fallback Engine:** Features a fallback RegEx parser for offline testing without API keys.
- **Multi-Sheet Excel Generator:** Generates multi-tab Excel reports (`Invoice Summary` and `Line Items`) formatted using `OpenPyXL` and `Pandas`.
- **FastAPI REST Service:** Built-in web service (`api_service.py`) providing `/api/process-pdf` REST endpoint with interactive Swagger UI docs.

## 🛠️ Tech Stack
- **Python 3.11**
- **PyMuPDF (`pymupdf`)**
- **Google Gemini API (`google-generativeai`)**
- **Pandas & OpenPyXL**
- **FastAPI & Uvicorn**

## 💻 How to Run

### 1. Run the CLI & Test Pipeline
```bash
# Install Dependencies
pip install -r requirements.txt

# Run Main Pipeline (Generates sample PDF & outputs final Excel report)
python main.py
```

### 2. Start the FastAPI REST Web Service
```bash
uvicorn api_service:app --reload
```
Open your browser at `http://127.0.0.1:8000/docs` to test the interactive PDF Upload REST endpoint!

## 📂 Output Files Generated
1. `sample_invoice.pdf` (Generated Sample Input)
2. `final_ai_document_report.xlsx` (Final Formatted Excel Report)
