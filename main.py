from fastapi import FastAPI
import uvicorn
import openai
import os
from pydantic import BaseModel

openai.api_key = "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"
app = FastAPI()
model_engine = "text-davinci-003"


class Proquest(BaseModel):
    prompt: str


@app.get("/")
def wow():
    return {"mes":"WOW!"}


@app.post("/ask")
async def asker(arg:Proquest):
    prompter = openai.Completion.create(engine=model_engine,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
     prompt=arg.prompt)

    return {"He said": prompter.choices[0]["text"]}

uvicorn.run(app, port=80,host="0.0.0.0")
