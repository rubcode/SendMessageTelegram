from chat import *
from fastapi import FastAPI
app = FastAPI()

@app.get("/sendChat")
def sendMessage(message: str):
  response = sendChat(message)
  return {"response": response}

#message = "Hola mundo"
#sendChat(message)