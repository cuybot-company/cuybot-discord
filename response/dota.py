import api.data_dota as api
import helper.constants as c
from datetime import datetime

class Dota(object):
  def __init__(self, user_message, bot_send):
    self.user_message = user_message
    self.bot_send = bot_send
  async def live(self):
    if any(x in self.user_message for x in c.request_dota):
      data = api.get_dota_live()

      i = 0
      list = 0
      live = 'Upcoming Live :'
      while list < 10:
        if 'team_name_radiant' in data[i]:
          list += 1
          live = live + '\n ' + str(list) + '. ' + data[i]['team_name_radiant'] + ' - ' + data[i]['team_name_dire'] + '(' + str(datetime.fromtimestamp(data[i]['activate_time'])) + ' UTC)'
        i += 1
      await self.bot_send(live)
