import requests
import json


def get_word(words): 
    word_get = requests.get('https://api.dictionaryapi.dev/api/v2/entries/en/' + words)
    datas = json.loads(word_get.text)
    return datas