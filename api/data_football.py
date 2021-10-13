import requests
import json

def get_data_football():
  url = "https://www.scorebat.com/video-api/v3/"
  response = requests.request("GET", url)
  json_data = json.loads(response.text)
  data = json_data['response']
  i = 0
  list = 0
  
  result = 'Hasil Pertandingan :'
  while list < 10:
    if 'title' in data[i] :
      list += 1
      search = 'MEXICO' in data[i]['competition']
      result = result + '\n ' + str(list) + '. ' + data[i]['title'] + '\n Kompetisi : ' + str(search)
    i += 1
    
  return(result)