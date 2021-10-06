import requests
import json

def get_covid_data(args, params, child):
  response = requests.get('https://data.covid19.go.id/public/api/update.json')
  json_data = json.loads(response.text)
  data = ''
  if args != '' and params != '' and child != '':
   data = json_data[args][params][child]
  elif args != '' and params != '' and child == '':
   data = json_data[args][params]
  else:
    data = json_data[args]
  return(data)