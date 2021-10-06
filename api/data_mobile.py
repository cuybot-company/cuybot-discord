import requests
import json

def get_mobile_latest():
  response = requests.get('https://api-mobilespecs.azharimm.site/v2/latest')
  json_data = json.loads(response.text)
  return(json_data['data']['phones'])