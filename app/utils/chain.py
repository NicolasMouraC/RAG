import os
from langchain_community.chat_models import ChatOllama
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

LLM_MODEL = os.getenv('LLM_MODEL', 'mistral')

OLLAMA_BASE_URL = os.getenv('OLLAMA_BASE_URL', 'http://ollama:11434')

def get_prompt():
    template = """You are an AI language model assistant. Your task is to generate the best
    possible answer of the given user question to retrieve relevant documents from
    a vector database.
    Answer the question, in portuguese, based ONLY on the following context:
    {context}
    Question: {question}
    """
    prompt = ChatPromptTemplate.from_template(template)
    return prompt

def chain(input_query, db):
    if input_query:
        llm = ChatOllama(model=LLM_MODEL, base_url=OLLAMA_BASE_URL)
        
        prompt = get_prompt()
        
        chain_process = (
            {"context": db.as_retriever(), "question": RunnablePassthrough()}
            | prompt
            | llm
            | StrOutputParser()
        )

        response = chain_process.invoke(input_query)
        
        return response

    return None
