from docx import Document
import PyPDF2
from bs4 import BeautifulSoup
def read_txt(path):
    return open(path, "r", encoding="utf-8").read()
def read_docx(path):
    doc = Document(path)
    return "\n".join([p.text for p in doc.paragraphs])
def read_pdf(path):
    reader = PyPDF2.PdfReader(open(path, "rb"))
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text
def read_html(path):
    html = open(path, "r", encoding="utf-8").read()
    soup = BeautifulSoup(html, "html.parser")
    return soup.get_text()
