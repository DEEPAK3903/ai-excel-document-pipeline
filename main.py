import sys
import logging
import fitz  # PyMuPDF
from pdf_extractor import extract_pdf_text
from ai_parser import AIDocumentParser
from excel_builder import build_excel_report

# Windows console encoding compatibility
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def create_sample_pdf(filename="sample_invoice.pdf"):
    """Creates a sample PDF document for testing the extraction pipeline."""
    doc = fitz.open()
    page = doc.new_page()
    
    text = """
    ==================================================
    INVOICE: INV-2026-089
    Date: 2026-09-24
    Customer: VSQUARE Construction & Tech Services
    ==================================================

    DESCRIPTION                                  QTY   PRICE   TOTAL
    ------------------------------------------------------------------
    Web Automation Module License                 1    $450    $450.00
    AI Document Processing Service                2    $300    $600.00
    Excel Pipeline Setup & Integration            1    $250    $250.00
    ------------------------------------------------------------------
    Subtotal: $1300.00
    Tax (10%): $130.00
    Total Amount Due: $1430.00
    ==================================================
    Thank you for your business!
    """
    page.insert_text((50, 50), text, fontsize=11)
    doc.save(filename)
    doc.close()
    logging.info(f"Sample PDF created: {filename}")
    return filename

def main():
    print("=" * 60)
    print("AUTOMATED EXCEL PROCESSING & AI DOCUMENT INTELLIGENCE PIPELINE")
    print("=" * 60)

    # Step 1: Create or Target PDF File
    pdf_path = create_sample_pdf("sample_invoice.pdf")
    
    # Step 2: Extract Text using PyMuPDF (fitz)
    logging.info("Step 1: Extracting text from PDF using PyMuPDF...")
    raw_text = extract_pdf_text(pdf_path)
    print("\n--- Extracted Raw Text ---")
    print(raw_text)
    print("--------------------------\n")
    
    # Step 3: AI Document Intelligence Parsing
    logging.info("Step 2: Parsing unstructured text with AI Engine...")
    parser = AIDocumentParser()
    structured_json = parser.parse_document(raw_text)
    
    print("\n--- Structured AI JSON Payload ---")
    import json
    print(json.dumps(structured_json, indent=2))
    print("-----------------------------------\n")

    # Step 4: Build Excel Report
    logging.info("Step 3: Generating formatted Excel Report using OpenPyXL...")
    excel_file = build_excel_report(structured_json, "final_ai_document_report.xlsx")
    
    print("=" * 60)
    print(f"PIPELINE COMPLETE! Excel Report Generated: {excel_file}")
    print("=" * 60)

if __name__ == "__main__":
    main()
