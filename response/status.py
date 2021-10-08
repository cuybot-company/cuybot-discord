import helper.constants as c

class Bot_Status:
  def __init__(self, user_message, bot_send):
    self.user_message = user_message
    self.bot_send = bot_send
  async def check(self):
    if any(word in self.user_message for word in c.request_stat):
      await self.bot_send(':partying_face: CuyBot Masih Aktif! :partying_face:')