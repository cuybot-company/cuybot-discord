import helper.constants as c

class play_game(object):
  def __init__(self, user_message, bot_send):
    self.user_message = user_message
    self.bot_send = bot_send
  async def message(self):
    if any(x in self.user_message for x in c.request_play_game):
      await self.bot_send('wait a game ...')