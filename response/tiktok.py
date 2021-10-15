import helper.constants as c
import helper.discord as d
import api.data_tiktok as api


class Tiktok(c.cog):
    def __init__(self, client):
        self.client = client
    @c.cmd.command(name='tt', aliases=['tiktok'])
    async def find(self, ctx):
        bot_send = ctx.message.reply
        user_message = ctx.message.content
        username = user_message.split(" ", 1)
        if len(username) == 1:
            embed = d.embeed(
                "Tiktok",
                ':clap: Masukan username tiktok yang anda mau mendapatkan informasi:\n`cuy/tt [username]` :clap:'
            )
            await bot_send(embed=embed)
        else:
            resp = api.info(username[1])

            if type(resp) is str:
                embed = d.embeed(
                    ":information_source: Informasi Akun TikTok :information_source: ",
                    resp)
                return await bot_send(embed=embed)

            # Info Account Tiktok
            username = resp["username"]
            link = resp["url"]
            thumb = resp["profileImage"]
            verified = 'Sudah' if resp["verified"] == True else 'Belum'
            bio = f"(Akun {username} belum memasukan bio)" if resp["bio"] == "" else resp["bio"]

            arr = {
                "thumbnail":
                thumb,
                "author": {
                    "name": username,
                    "url": link,
                    "icon": thumb
                },
                "field": [{
                    "name": "Bio",
                    "value": bio,
                    "inline": True
                }, {
                    "name": "Following",
                    "value": resp["following"],
                    "inline": True
                }, {
                    "name": "Followers",
                    "value": resp["followers"],
                    "inline": True
                }, {
                    "name": "Fans",
                    "value": resp["fans"],
                    "inline": True
                }, {
                    "name": "Hearts",
                    "value": resp["hearts"],
                    "inline": True
                }, {
                    "name": "Videos",
                    "value": resp["videos"],
                    "inline": True
                }, {
                    "name": "Verified",
                    "value": f"Akun {verified} Verified",
                    "inline": True
                }]
            }

            embed = d.embeed(
                ":information_source: Informasi Akun TikTok :information_source: ",
                "", "", arr)
            await bot_send(embed=embed)

def setup(client):
    client.add_cog(Tiktok(client))
