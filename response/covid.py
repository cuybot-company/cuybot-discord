import helper.constants as c
import api.data_covid as api

class covid(object):
  def __init__(self, user_message, bot_send):
    self.user_message = user_message
    self.bot_send = bot_send
  async def find_latest(self):
        if self.user_message.startswith('cuy/covid'):
            odp = api.get_covid_data('data', 'jumlah_odp', '')
            total_spesimen_negatif = api.get_covid_data(
                'data', 'total_spesimen_negatif', '')
            total_positif = api.get_covid_data(
                'update', 'penambahan', 'jumlah_positif')
            total_sembuh = api.get_covid_data(
                'update', 'penambahan', 'jumlah_sembuh')
            total_meninggal = api.get_covid_data(
                'update', 'penambahan', 'jumlah_meninggal')
            update_per = api.get_covid_data('update', 'penambahan', 'created')

            await self.bot_send(':flag_mc: ***DATA COVID*** :flag_mc:\nUPDATE PER: ' + update_per + ' :date:\n' + ':warning: Data Resmi Dari: ' + c.data_covid_from + ' :warning:\n\n' + 'Total ODP saat ini: **' + f'{odp:,}' + '** orang :thermometer_face:' + "\n" + 'Total spesimen negatif: **' + f'{total_spesimen_negatif:,}' + '** orang :thinking:' + '\n' + 'total positif: **' + f'{total_positif:,}' + '** orang :persevere:' + '\n' + 'Total sembuh: **' + f'{total_sembuh:,}' + '** orang :hugging:' + '\n' + 'Total meninggal: **' + str(total_meninggal) + '** orang :cry:' + '\n\n' + '---TERIMAKASIH CUYBOT--- :laughing:')
