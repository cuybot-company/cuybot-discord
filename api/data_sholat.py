import requests
import json
from datetime import date

def get_jadwal_sholat(param):
  dt = date.today()
  dt_year = str(dt.year)
  dt_month = str(dt.month)
  dt_day = str(dt.day)
  data_param = param.split()[1]
  response = requests.get('https://api.myquran.com/v1/sholat/kota/cari/' + data_param)
  json_data = json.loads(response.text)
  id_kota = json_data['data'][0]['id']
  nama_kota = json_data['data'][0]['lokasi']
  final_response = requests.get('https://api.myquran.com/v1/sholat/jadwal/' + id_kota + '/'+ dt_year +'/'+ dt_month +'/'+ dt_day)
  json_data_sholat = json.loads(final_response.text)
  final_data = json_data_sholat['data']['jadwal']
  tanggal = json_data_sholat['data']['jadwal']['tanggal']
  imsak = json_data_sholat['data']['jadwal']['imsak']
  shubuh = json_data_sholat['data']['jadwal']['subuh']
  terbit = json_data_sholat['data']['jadwal']['terbit']
  dhuha = json_data_sholat['data']['jadwal']['dhuha']
  dzuhur = json_data_sholat['data']['jadwal']['dzuhur']
  ashar = json_data_sholat['data']['jadwal']['ashar']
  maghrib = json_data_sholat['data']['jadwal']['maghrib']
  isya = json_data_sholat['data']['jadwal']['isya']
  final_result = 'JADWAL SHOLAT '+nama_kota+ ':\n' +tanggal+'\nShubuh : '+shubuh+'\nImsak : '+imsak+'\nTerbit : '+terbit+'\nDhuha : '+dhuha+'\nDzuhur : '+dzuhur+'\nAshar : '+ashar+'\nMaghrib : '+maghrib+'\nIsya : '+isya+'\nLuangkanlah waktu untuk Sholat, bukan Sholat di waktu luang'
  return(final_result)  