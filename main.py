from fastapi import FastAPI, HTTPException
import uvicorn
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

@app.get("/")
def root():
    response = {"Hello World"}
    return response
if __name__ == "__main__":
    uvicorn.run(app)
    