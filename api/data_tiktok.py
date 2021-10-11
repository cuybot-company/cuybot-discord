import requests
import json
from bs4 import BeautifulSoup

def info(username):
    if username.startswith('@'):
        username = username
    else:
        username = f'@{username}'


    try:
        r = requests.get(f'https://tiktok.com/{username}', headers={'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'})
        soup = BeautifulSoup(r.text, "html.parser")


        content = soup.find_all("script", attrs={"type":"application/json", "crossorigin":"anonymous"})
        content = json.loads(content[0].contents[0])

        profile_data = {
            "UserID":content["props"]["pageProps"]["userInfo"]["user"]["id"],
            "username":content["props"]["pageProps"]["userInfo"]["user"]["uniqueId"],
            "nickName":content["props"]["pageProps"]["userInfo"]["user"]["nickname"],
            "bio":content["props"]["pageProps"]["userInfo"]["user"]["signature"],
            "profileImage":content["props"]["pageProps"]["userInfo"]["user"]["avatarLarger"],
            "following":content["props"]["pageProps"]["userInfo"]["stats"]["followingCount"],
            "followers":content["props"]["pageProps"]["userInfo"]["stats"]["followerCount"],
            "fans":content["props"]["pageProps"]["userInfo"]["stats"]["followerCount"],
            "hearts":content["props"]["pageProps"]["userInfo"]["stats"]["heart"],
            "videos":content["props"]["pageProps"]["userInfo"]["stats"]["videoCount"],
            "verified":content["props"]["pageProps"]["userInfo"]["user"]["verified"]
        }

        bio = profile_data["bio"]
        following = profile_data["following"]
        followers = profile_data["followers"]
        fans = profile_data["fans"]
        hearts = profile_data["hearts"]
        videos = profile_data["videos"]
        verified = "Akun Sudah Verified" if profile_data["verified"] == True else "Akun Belum Verified"

        message = """
        :information_source: Informasi Akun TikTok :information_source: 
        
Link Tiktok: https://www.tiktok.com/{}
bio: {}
Following: {}
Followers: {}
Fans: {}
Likes: {}
Videos: {}
Verified: {}
    """.format(username, bio, following, followers, fans, hearts, videos, verified)

        return message

    except:
        return("Username {} tidak ditemukan".format(username))