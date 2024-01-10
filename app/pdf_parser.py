import os
import prompts
import tempfile
import pdfplumber
import shutil
import re

from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
from langchain.document_loaders import TextLoader
from langchain.document_loaders import PDFPlumberLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains.question_answering import load_qa_chain

def parse_file(file):
  is_sbc = False
  
  # load document
  path = "./pdf_uploads-" + file.filename
  with open(path, 'wb+') as buffer:
    shutil.copyfileobj(file.file, buffer)

    # Try to get the plan name
    pdf = pdfplumber.open(path)
    pages = pdf.pages
    for page in pages:
      text = page.extract_text()
      is_sbc = "Summary of Benefits and Coverage" in text
      if is_sbc:
        break 
  
    loader = PDFPlumberLoader(path)
    documents = loader.load()
    
    # split the documents into chunks
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    texts = text_splitter.split_documents(documents)
    # select which embeddings we want to use
    embeddings = OpenAIEmbeddings()
    # create the vectorestore to use as the index
    db = Chroma.from_documents(texts, embeddings)
    # expose this index in a retriever interface
    retriever = db.as_retriever(search_type="similarity", search_kwargs={"k":2})

    responses = []

    for prompt in prompts.prompts():
      for question in prompt['questions']:
        # create a chain to answer questions 
        qa = RetrievalQA.from_chain_type(
            llm=OpenAI(), chain_type="stuff", retriever=retriever, return_source_documents=True)
        query = question
        result = qa({"query": query})
        responses.append({"key": prompt["key"], "result": result["result"]})

    return {"data": responses, "sbc": is_sbc}