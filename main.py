#pip install pytesseract pdf2image pillow

import pytesseract
from pdf2image import convert_from_path

# Convert PDF to images
pages = convert_from_path("sample1.pdf", dpi=300)

text_output = []
for page in pages:
    text = pytesseract.image_to_string(page, lang="eng")
    text_output.append(text)

print("\n".join(text_output))
