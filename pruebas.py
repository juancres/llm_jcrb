import requests
import json

url = 'http://localhost:11434/api/generate'
myobj = {
    "model": "tinyllama",
    "prompt":  "cual es la velocidad de conexion mas rapida de internet en el mundo",
    "stream": False
}


x = requests.post(url, json = myobj)

x = json.loads(x.text)

print(x["response"])

