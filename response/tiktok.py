import api.data_tiktok as tiktok
import helper.constants as c


class latest(object):
  def __init__(self, user_message, bot_send):
    self.user_message = user_message
    self.bot_send = bot_send

  async def follower(self):
    if any(x in self.user_message for x in c.request_tiktok):
      data = tiktok.get_latest_follower()
      print('data => ' + data)
      await self.bot_send(data)
