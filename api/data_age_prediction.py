import requests
import json


def predict(name):
    yourname = requests.get(
        'https://api.agify.io/?name=' + name)
    datas = json.loads(yourname.text)
    age = str(datas['age']) 
    if  age == "None":
        return('Oke markicob nebak usia si ' + str(datas['name']) + '!\n' + 'gw gak bisa nebak njir itu mah, maaf :(')
    else:
        return('Oke markicob nebak usia si ' + str(datas['name']) + '!\n' + 'cuybot nebak kalau umur lu keknya ' + '**' + str(datas['age']) +'**' + '\n\nhehe peace :P maaf kalau salah, thank u kalau bener :)')
