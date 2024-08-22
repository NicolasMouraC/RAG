import os
import sys
import logging
import datetime
from fastapi import FastAPI
from dotenv import load_dotenv
from app.utils.error_handler import imposter_syndrome
from app.utils.pdf_processor import extract_text_from_pdf
from app.utils.text_processor import process_text
from app.utils.vector_store import vector_store
from app.routes.chain_routes import chain_routes

load_dotenv()
PORT = os.getenv('PORT', 8000)
PDF_FILE_LOCATION = os.getenv('PDF_FILE_LOCATION', './pdf/Politica_de_Privacidade.pdf')

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def startup():
  pdf_text = extract_text_from_pdf(PDF_FILE_LOCATION)
  processed_text = process_text(pdf_text)
  vector_store(processed_text)

def shutdown():
  logger.info("Closing server")

def lifespan(_app: FastAPI):
  startup()
  yield
  shutdown()

app = FastAPI(lifespan=lifespan)

sys.excepthook = imposter_syndrome

app.include_router(chain_routes, tags=["chain"])

@app.get("/")
def root():
  date = datetime.date.today()
  return {
    "message": "Application is running",
    "date": date,
    "success": True
  }

if __name__ == "__main__":
  import uvicorn
  uvicorn.run(app, host="0.0.0.0", port=PORT)