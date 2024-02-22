from PyPDF2 import PdfReader

def extract_text_from_pdf(file_path):
    with open(file_path, 'rb') as file:
        pdf = PdfReader(file)
        text = ''
        for page in pdf.pages:
            text += page.extract_text()
        return text

if __name__ == '__main__':
    # Usage
    pdf_file_path = 'test.pdf'
    extracted_text = extract_text_from_pdf(pdf_file_path)
    print(extracted_text)
