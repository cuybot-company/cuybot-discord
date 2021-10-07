import requests
import json

def get_mobile_latest():
  response = requests.get('https://api-mobilespecs.azharimm.site/v2/latest')
  json_data = json.loads(response.text)
  return(json_data['data']['phones'])

def get_mobile_spec(merk):
  response = requests.get('http://api-mobilespecs.azharimm.site/v2/search?query='+ merk )
  json_data = json.loads(response.text)

  if len(json_data['data']['phones']) == 0:
    return 'empty'
  else:
    response_spec = requests.get(json_data['data']['phones'][0]['detail'] )
    json_data_spec = json.loads(response_spec.text)

    return(json_data_spec['data'])