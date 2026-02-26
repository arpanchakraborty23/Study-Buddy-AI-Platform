import os
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Study Buddy Fastapi Server",debug=True,version="0.1.0")

@app.get("/")
def health():
    return {"message": "ok"}



if __name__=="__main__":
    uvicorn.run(app)