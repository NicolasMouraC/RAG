
## How to deploy
This code uses make Linux command in order to make it easy to deploy docker in production. Run the following commands:

- **make start**: Start containers and volumes.
- **make stop**: Stop containers.
- **make clean**: Remove containers and volumes.
- **make deploy**: Pull latest code from git main branch and build containers.

## Important notes
- A test request can be send to AWS EC2 https://100.25.182.78:8000. But due to test server limitations, expect server downtime.
- Default environments variables will be used in case of no value set, docker environment is set to default.
- A ollama model is required, the default one is mistral, use `ollama pull mistral` inside ollama container if you don't have a model installed on your PC. 
- It is recommended to allow graphic card use from ollama container.

## Folders Structure

- App: Main folder
-- Routes: App routes
-- Utils: App helper function
- Pdf: Default pdf location
- Models: (After initial setting) ollama LLM models folders

## Server Startup
After the server boots, it will automatically extract the standard pdf, process the text from it and store it in chromadb vectors.

## Server Routes
- GET /
> Returns message, current UTC date and a success flag.
- POST /get-response
 
|                |VALUE                          |REQUIRED                         |
|----------------|-------------------------------|-----------------------------|
|query           |String                         |TRUE                         |
> Given the correct body requisition, it will send a response back for the question provided using RAG functionalities.

