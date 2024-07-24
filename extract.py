import pdfplumber
import re
import json

def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text

def preprocess_text(text):
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^A-Za-z0-9\s.,?!]', '', text)
    return text

pdf_path = "./solid.pdf"
extracted_text = extract_text_from_pdf(pdf_path)
preprocessed_text = preprocess_text(extracted_text)

data = {
    "prompt": "Analyze the following C# code from the PDF:",
    "completion": preprocessed_text
}

with open('dataset.json', 'w') as f:
    json.dump(data, f)

print("Dataset saved as dataset.json")
