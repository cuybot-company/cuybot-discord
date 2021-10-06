import api.data_quote as api
import helper.constants as c

class quote(object):
  def __init__(self, user_message, bot_send):
    self.user_message = user_message
    self.bot_send = bot_send
  async def find_one(self):
        if any(x in self.user_message for x in c.request_quote):
            await self.bot_send('Tunggu sebentar saya carikan dulu quotes menarik untuk kamu ')
            data = api.get_quotes()
            await self.bot_send(data)
