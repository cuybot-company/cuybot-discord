import api.data_quote as api

class quote(object):
  def __init__(self, user_message, bot_send):
    self.user_message = user_message
    self.bot_send = bot_send
  async def find_one(self):
        if self.user_message.startswith('cuy/quotes'):
            await self.bot_send('Tunggu sebentar saya carikan dulu quotes menarik untuk kamu ')
            data = api.get_quotes()
            await self.bot_send(data)
