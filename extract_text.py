import pdfplumber

def extract_text_from_pdf(pdf_path):
    text = ""
    # PDF 파일 열기
    with pdfplumber.open(pdf_path) as pdf:
        # 각 페이지에서 텍스트 추출
        for page in pdf.pages:
            text += page.extract_text()
    return text

pdf_path = "./solid.pdf"
extracted_text = extract_text_from_pdf(pdf_path)
print(extracted_text)
