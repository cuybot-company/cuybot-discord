import requests
import json

def request(anime):
    r = requests.get(f"https://info-anime.rizsyad.repl.co/{anime}")
    json_data = json.loads(r.text)
        
    if json_data["status"] == "error":
        return json_data["message"]

    anime_data = json_data["data"]

    return anime_data