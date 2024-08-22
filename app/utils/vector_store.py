import os
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from chromadb.config import Settings

CHROMADB_HOST = os.getenv('CHROMADB_HOST', 'chromadb')
CHROMADB_PORT = os.getenv('CHROMADB_PORT', '8001')

def vector_store(documents):
  global db
  
  embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

  
  client_settings = Settings(
    chroma_server_host=CHROMADB_HOST,
    chroma_server_http_port=CHROMADB_PORT
  )

  vector_store = Chroma.from_documents(
    documents=documents,
    embedding=embeddings,
    persist_directory="./chroma_db",
    client_settings=client_settings
  )

  vector_store.persist()

  db = vector_store
