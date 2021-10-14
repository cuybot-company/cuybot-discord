import helper.constants as c
import json
from urllib import request

api_key = 'c427ea57fb1b29d190682f9b1b25d5c8'
def get_cuaca(kota):
    cuaca = request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + kota + '&appid=' + api_key)
    datas = json.loads(cuaca.read())
    if datas['cod'] == 200:
        lokasi = datas['name']
        weather = datas['weather'][0]['main']
        suhu = (datas['main']['temp'] - 273)
        return('Sumber data dari: ' + c.data_cuaca_from + 'Lokasi: ' + lokasi + '\nCuaca: ' + weather + '\nSuhu: ' + str(round(suhu,2)) + ' derajat celcius')
    else:
        return("Maaf kotamu tidak terdaftar disini")

