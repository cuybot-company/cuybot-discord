import requests
import json
import random

def get_quotes():
  response = requests.get('https://backend-ihsandevs.herokuapp.com/api/quotes%20keren/')
  json_data = json.loads(response.text)
  random_length = random.randint(0,len(json_data['result']) - 1)
  tokoh_quotes = json_data['result'][random_length]
  responseQuotes = requests.get('https://backend-ihsandevs.herokuapp.com/api/quotes%20keren/?name=' + tokoh_quotes)
  json_data_quotes = json.loads(responseQuotes.text)
  random_length_quotes = random.randint(0,len(json_data_quotes['result']) - 1 )
  quotes = json_data_quotes['result'][random_length_quotes]
  return(quotes)