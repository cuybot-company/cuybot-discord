import requests
import json

def get_face():
  response = requests.get('https://100k-faces.glitch.me/random-image-url')
  json_data = json.loads(response.text)
  return([json_data])