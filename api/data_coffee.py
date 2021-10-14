import requests
import json

def data_coffee():
    data_cofee = requests.get("https://coffee.alexflipnote.dev/random.json")
    data = json.loads(data_cofee.text)
    return data["file"]
    