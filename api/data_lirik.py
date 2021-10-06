import requests
import json


def get_lirik(lagu):
    list_lagu = requests.get(
        'https://api-song-lyrics.herokuapp.com/search?q=' + lagu)
    datas = json.loads(list_lagu.text)
    lirik = datas['data']
    if len(lirik) > 1:
        return('mohon judul lebih spesifik lagi, terlalu banyak list (fitur masih ongoing cuy).\ncoba cari misalnya cuy/lirik kala cinta menggoda')
    elif len(lirik) == 1:
        for data in lirik:
            liriks = data['songLyrics']
            result = lirik_detail(liriks)
            return(result)
    else:
        return('maaf gw kurang paham cuy, cari lirik lainnya ya. jangan lupa pake command\ncuy/lirik [nama lagu selengkap lengkapnya, kalau bisa nama band nya juga masukin]')


def lirik_detail(link):
    lirik = requests.get(link)
    json_data = json.loads(lirik.text)
    lirik_asli = json_data['data']['songLyrics']
    return(lirik_asli)
