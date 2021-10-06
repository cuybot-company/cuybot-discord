from TikTokAPI import TikTokAPI

cookie = {
  "s_v_web_id": "verify_kuf91wie_NyAzMIdq_1Efg_4DWC_94uG_nITO0viLQgVo",
  "tt_webid": "7014103910529172993"
}
api = TikTokAPI(cookie=cookie)

def last_follower():
  user_obj = api.getUserByName("dea.afrizal")
  print('user obj => ' + user_obj)
  return user_obj
