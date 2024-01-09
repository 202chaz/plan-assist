import os
import prompts
import tempfile
import pdfplumber

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
  # load document
  pdf = pdfplumber.open(file.file)
  print(pdf)
  # loader =PDFPlumberLoader(pdf)
  # documents = loader.load()
  
  # split the documents into chunks
  # text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
  # texts = text_splitter.split_documents(documents)
  # select which embeddings we want to use
  # embeddings = OpenAIEmbeddings()
  # create the vectorestore to use as the index
  # db = Chroma.from_documents(texts, embeddings)
  # expose this index in a retriever interface
  # retriever = db.as_retriever(search_type="similarity", search_kwargs={"k":2})

  responses = []

  # for prompt in prompts.prompts():
  #   for question in prompt['questions']:
  #     # create a chain to answer questions 
  #     qa = RetrievalQA.from_chain_type(
  #         llm=OpenAI(), chain_type="stuff", retriever=retriever, return_source_documents=True)
  #     query = question
  #     result = qa({"query": query})
  #     responses.append({"key": prompt["key"], "result": result["result"]})
  
  return responses

async def test_upload(file):
  # loader = PDFPlumberLoader(file)
  print(await file.read())
  
  return {}