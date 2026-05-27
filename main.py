from pathlib import Path
import tempfile

import pytesseract
from fastapi import FastAPI, File, HTTPException, UploadFile
from pdf2image import convert_from_path

app = FastAPI(title="PDF OCR API", version="1.0.0")


@app.get("/")
def root() -> dict:
    return {"message": "PDF OCR API is running"}


@app.post("/extract-text")
async def extract_text(file: UploadFile = File(...)) -> dict:
    if file.content_type not in ("application/pdf", "application/x-pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are allowed.")

    suffix = Path(file.filename or "upload.pdf").suffix.lower()
    if suffix != ".pdf":
        suffix = ".pdf"

    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as temp_pdf:
            temp_pdf.write(await file.read())
            temp_pdf_path = temp_pdf.name

        pages = convert_from_path(temp_pdf_path, dpi=300)
        text_output = [pytesseract.image_to_string(page, lang="eng") for page in pages]
        full_text = "\n".join(text_output).strip()
        return {
            "filename": file.filename,
            "pages": len(pages),
            "text": full_text,
        }
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"OCR failed: {exc}") from exc
    finally:
        temp_path = Path(temp_pdf_path) if "temp_pdf_path" in locals() else None
        if temp_path and temp_path.exists():
            temp_path.unlink(missing_ok=True)


"""
Run:
    pip install fastapi uvicorn pytesseract pdf2image pillow
    uvicorn main:app --reload
"""
