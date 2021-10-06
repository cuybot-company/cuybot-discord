import api.data_tiktok as api
import helper.constants as c

class tiktok(object):
  def __init__(self, user_message, bot_send):
    self.user_message = user_message
    self.bot_send = bot_send
    
  async def account_info(self):
    if self.user_message.startswith('cuy/tiktok'):
      data = api.info()
      await self.bot_send(data)

  async def followers(self):
    if self.user_message.startswith('cuy/follower'):
      data = api.last_follower()
      await self.bot_send(data)

  async def likes(self):
    if self.user_message.startswith('cuy/like'):
      data = api.last_liked()
      await self.bot_send(data)
      
  async def videos(self):
    if self.user_message.startswith('cuy/video'):
      data = api.total_video()
      await self.bot_send(data)

  async def urls(self):
    if self.user_message.startswith('cuy/link'):
      data = api.url()
      await self.bot_send(data)