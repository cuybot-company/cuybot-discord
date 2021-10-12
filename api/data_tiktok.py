import requests
import json

def info(username):

        r = requests.get(f'https://info-tiktok.rizsyad.repl.co/{username}')
        json_data = json.loads(r.text)
        
        if json_data["status"] == "error":
            return json_data["message"]

        profile_data = json_data["data"]

        return profile_data