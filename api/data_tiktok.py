from TikTokApi import TikTokApi
tt_api = TikTokApi()

class tiktok(object):
  def __init__(self, user_message, bot_send):
    self.user_message = user_message
    self.bot_send = bot_send
    
    async def get_latest_follower(self):
      user_videos = tt_api.byUsername('dea.afrizal', count=1)
      tiktok_id = tt_api.getUser('tiktok')['userInfo']['user']['id']
      return(user_videos)