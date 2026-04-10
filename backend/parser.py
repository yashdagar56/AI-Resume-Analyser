import fitz

def extract_text_from_pdf(file_bytes: bytes) -> str:
    """
    Extracts all text from every page of a PDF given its bytes.
    """
    doc = fitz.open(stream=file_bytes, filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text("text") + "\n"
    
    return text.strip()
