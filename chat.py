from dotenv import load_dotenv
import os
import json
import requests


def sendChat(message):
    message = message.replace('"','')
    load_dotenv()
    token = os.environ['TOKEN']
    chatID = os.environ['CHAT_ID']
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = json.dumps({
        "text": message,
        "chat_id": chatID
    })
    headers = {
    'Content-Type': 'application/json'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    return response.text
