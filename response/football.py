import api.data_football as api
import helper.constants as c

class Football(object):
  def __init__(self, user_message, bot_send):
    self.user_message = user_message
    self.bot_send = bot_send
  async def check(self):
     if self.user_message.startswith('cuy/football'):
        league = api.get_data_football(self.user_message)
        await self.bot_send(league)
