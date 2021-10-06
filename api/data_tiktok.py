from TikTokApi import TikTokApi
tt_api = TikTokApi()

def get_latest_follower():
  user_videos = tt_api.byUsername('dea.afrizal', count=1)
  tiktok_id = tt_api.getUser('tiktok')['userInfo']['user']['id']
  return(user_videos)