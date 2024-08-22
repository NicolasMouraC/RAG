FROM python:3.12.1

WORKDIR /

RUN apt-get update && apt-get install git -y && apt-get install curl -y
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

ENV LLM_MODEL=${LLM_MODEL}
ENV OLLAMA_BASE_URL=${OLLAMA_BASE_URL}
ENV CHROMADB_HOST=${CHROMADB_HOST}
ENV CHROMADB_PORT=${CHROMADB_PORT}
ENV PORT=${PORT}
ENV PDF_FILE_LOCATION=${PDF_FILE_LOCATION}

CMD ["python", "main.py"]
