from os import name
import helper.constants as c
import helper.discord as d
import api.data_anime as api

class Anime(c.cog):
    def __init__(self, client):
        self.client = client
    @c.cmd.command(name="anime")
    async def info(self, ctx):
        user_message = ctx.message.content
        bot_send = ctx.message.reply
        anime = user_message.split(" ", 1)
        if len(anime) == 1:
            embed = d.embeed(
                "Anime",
                ':clap: Masukan anime yang anda mau mendapatkan informasi:\n`cuy/anime [nama-anime]` :clap:'
            )
            await bot_send(embed=embed)
        else:
            resp = api.request(anime[1])

            if type(resp) is str:
                embed = d.embeed(
                    ":information_source: Informasi Anime :information_source: ",
                    resp)
                return await bot_send(embed=embed)

            score = resp["score"]
            scoreStats = resp["scoreStats"]

            arr = {
                "footer": {"text":"Data dari https://myanimelist.net/"},
                "thumbnail": resp["picture"],
                "author": {
                    "name":  resp["title"],
                    "url": resp["link"],
                },
                "field": [
                    {"name": "score", "value": f"{score} ({scoreStats})", "inline": True},
                    {"name": "rank", "value": resp["rank"], "inline": True},
                    {"name": "popularity", "value": resp["popularity"], "inline": True},
                    {"name": "type", "value": resp["type"], "inline": True},
                    {"name": "aired", "value": resp["aired"], "inline": True},
                    {"name": "studios", "value": resp["studios"], "inline": True},
                    {"name": "source", "value": resp["source"], "inline": True},
                    {"name": "genres", "value": resp["genres"], "inline": True},
                    {"name": "status", "value": resp["status"], "inline": True},
                ]
            }

            embed = d.embeed(
                ":information_source: Informasi Anime :information_source: ",
                "", "", arr)
            await bot_send(embed=embed)

def setup(client):
    client.add_cog(Anime(client))