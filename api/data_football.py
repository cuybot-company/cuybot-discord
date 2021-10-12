import requests
import json

def get_data_football(param):
  data_param = param.split()[1]
  url = "http://api.football-data.org/v2/players/"
  payload={}
  headers = {
    'X-Auth-Token': '010b53276b8f4551a4cb1c74c6df80a4'
  }

  response = requests.request("GET", url+data_param, headers=headers, data=payload)
  json_data = json.loads(response.text)
  name = json_data['name']
  birth = json_data['dateOfBirth']
  nationality = json_data['nationality']
  position = json_data['position']
  return('DATA PEMAIN : \n Nama : '+name+'\n Tanggal Lahir : '+birth+'\n Kebangsaan : '+nationality+'\n Posisi : '+position)