import requests
import json


def predict(name):
    yourname = requests.get(
        'https://api.agify.io/?name=' + name)
    datas = json.loads(yourname.text)
    return('Hi ' + str(datas['name']) + '!\n' + 'cuybot nebak kalau umur lu keknya ' + '**' + str(datas['age']) +'**' + '\n\nhehe peace :P maaf kalau salah, thank u kalau bener :)')
