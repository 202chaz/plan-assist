from typing import Union, Annotated

from fastapi import FastAPI, UploadFile, Form, File, Request
from fastapi.middleware.cors import CORSMiddleware

import pdfplumber
import re
import numpy
import pandas as pd
import math
import pbt
import pdf_parser
import uvicorn

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
  return {"Hello": "World"}

@app.post("/plan_names")
async def plan_names(request: Request, file: UploadFile = File(...)):
  content = await file.read()
  plans = pbt.get_plans(content)
  return plans

@app.post("/pbt_data")
async def pbt_data(plan_name: str = Form(...), sheet_name: str = Form(...), file: UploadFile = File(...)):
  content = await file.read()
  plan = pbt.get_plan(content, plan_name, sheet_name)
  return plan

@app.post("/parse_pdf")
async def parse_pdf(file: UploadFile = File(...)):
  pdf = pdf_parser.test_upload(file)
  return pdf

def main() -> None:
  """Invoke the entrypoint function of the script."""
  uvicorn.run("main:app", host="0.0.0.0", reload=True)

if __name__ == "__main__":
  main()
