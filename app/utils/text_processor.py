from langchain.text_splitter import CharacterTextSplitter
from langchain.schema import Document

def process_text(text):
  text_splitter = CharacterTextSplitter(chunk_size=512, chunk_overlap=50)
  text_chunks = text_splitter.split_text(text)

  documents = [Document(page_content=chunk) for chunk in text_chunks]
  return documents
