import pymupdf

def extract_text_from_pdf(pdf_path: str) -> str:
  document = pymupdf.open(pdf_path)
  text = ""
  for page in document:
    text += page.get_text()
  return text
