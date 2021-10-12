import requests
import json

def info(username):

        r = requests.get(f'https://info-tiktok.rizsyad.repl.co/{username}')
        json_data = json.loads(r.text)
        
        if json_data["status"] == "false":
            return(f"Username {username} tidak ditemukan")

        profile_data = json_data["data"]

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