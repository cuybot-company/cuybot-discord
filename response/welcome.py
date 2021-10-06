import helper.constants as c

class bot_welcome(object):
  def __init__(self, user_message, bot_send):
    self.user_message = user_message
    self.bot_send = bot_send
  async def message(self):
    if any(x in self.user_message for x in c.request_welcome):
      await self.bot_send(':partying_face: Oy cuy! :partying_face: \n\nperkenalkan cuy gw bot buatannya dea dan tim :yum:\ngw siap bantu ngasih info info sesuatu yang lu butuhin')