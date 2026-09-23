import fitz  # PyMuPDF
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def extract_pdf_text(pdf_path):
    """
    Extracts unstructured text from a PDF file using PyMuPDF (fitz).
    Returns the concatenated text string across all pages.
    """
    try:
        logging.info(f"Opening PDF file for text extraction: {pdf_path}")
        doc = fitz.open(pdf_path)
        full_text = ""
        
        for page_num in range(len(doc)):
            page = doc[page_num]
            text = page.get_text()
            full_text += f"\n--- Page {page_num + 1} ---\n" + text
            
        logging.info(f"Extracted {len(full_text)} characters across {len(doc)} pages.")
        return full_text.strip()
    except Exception as e:
        logging.error(f"Failed to extract PDF text from {pdf_path}: {e}")
        return None
