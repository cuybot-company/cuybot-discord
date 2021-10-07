import api.data_age_prediction as api
import helper.constants as c

class predict_age(object):
  def __init__(self, user_message, bot_send):
    self.user_message = user_message
    self.bot_send = bot_send
  async def prediction(self):
    if self.user_message.startswith('cuy/usia'):
        data = self.user_message.split(" ", 1)
        if len(data) == 1:
            await self.bot_send(':x: Masukin dulu nama lu cuy :x:')
        elif len(data) > 2:
            await self.bot_send(':x: Hanya support menebak 1 kata nama (nama panggilan atau real name) :x:')
        else:
            requested_name = self.user_message.split(" ", 1)[1]
            predicting = api.predict(requested_name)
            await self.bot_send(predicting)

