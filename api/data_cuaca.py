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

"""
Json data :
{
    "coord":
        {
            "lon":110.5184,
            "lat":-7.4202
            },
    "weather":
        [{
            "id":803,
            "main":"Clouds",
            "description":"broken clouds",
            "icon":"04n"
                }],
    "base":"stations",
    "main":
        {
            "temp":294.73,
            "feels_like":295.27,
            "temp_min":285.45,
            "temp_max":294.73,
            "pressure":1012,
            "humidity":89,
            "sea_level":1012,
            "grnd_level":928
                },
    "visibility":10000,
    "wind":
        {
            "speed":2.15,
            "deg":213,
            "gust":3.67
                },
    "clouds":{"all":69},
    "dt":1634397658,
    "sys":
        {
            "type":2,
            "id":2041584,
            "country":"ID",
            "sunrise":1634336119,
            "sunset":1634380284
                },
    "timezone":25200,
    "id":1629131,
    "name":"Tengaran",
    "cod":200
        }
"""
