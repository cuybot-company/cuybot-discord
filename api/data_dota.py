import requests
import json


def get_dota_live():
  response = requests.get('https://api.opendota.com/api/live')
  json_data = json.loads(response.text)
  return(json_data)
