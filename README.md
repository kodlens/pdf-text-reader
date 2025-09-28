# PDF TEXT READER OCR (Windows Environtment Setup Only)

Small project that will read pdf text/including image using tesseract

## Tesseract OCR (open-source, widely used)

    Pros: Free, good support for many languages, easy to integrate.

    Cons: Accuracy not as high as commercial engines on messy scans.

    Use with:

    Python (pytesseract + pdf2image)

    Node.js (tesseract.js)

## Install Tesseract On Windows

Download installer here (official Windows build, UB Mannheim is recommended):

    https://github.com/UB-Mannheim/tesseract/wiki

Add to Windows env
    
    C:\Program Files\Tesseract-OCR

Verify if tesseract is installed

    tesseract -v

Download and extract testdata

    https://github.com/tesseract-ocr/tessdata

Copy these files
    
    eng.traineddata
    osd.traineddata

And paste it here

    C:\Program Files\Tesseract-OCR\tessdata



