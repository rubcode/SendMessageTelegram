import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()
token = os.environ['TOKEN']
chatID = os.environ['CHAT_ID']
url = f"https://api.telegram.org/bot{token}/sendMessage"

payload = json.dumps({
  "text": "A partir de hoy yo estare enviando notificaciones sobre los procesos de Calidad",
  "chat_id": chatID
})
headers = {
  'Content-Type': 'application/json'
}
response = requests.request("GET", url, headers=headers, data=payload)
print(response.text)