import requests
import json

def get_mobile_latest():
  response = requests.get('https://api-mobilespecs.azharimm.site/v2/latest')
  json_data = json.loads(response.text)
  return(json_data['data']['phones'])

def get_mobile_spec(merk):
  response = requests.get('http://api-mobilespecs.azharimm.site/v2/search?query=' + merk)
  json_data = json.loads(response.text)
  if len(json_data['data']['phones']) == 0:
    return 'empty'
  else:
    i = 0
    length = len(json_data['data']['phones'])
    while i < length:
      json_merk = json_data['data']['phones'][i]['brand'] +' '+ json_data['data']['phones'][i]['phone_name'] 
      json_merk_name = json_data['data']['phones'][i]['phone_name']
      if json_merk.lower() == merk.lower() or json_merk_name.lower() == merk.lower() :
        response_spec = requests.get(json_data['data']['phones'][i]['detail'])
        json_data_spec = json.loads(response_spec.text)
        return json_data_spec['data']
        break
      i += 1
      if i == length:
        return 'empty'
        break