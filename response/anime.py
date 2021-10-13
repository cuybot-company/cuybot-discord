import helper.constants as c
import helper.discord as d
import api.data_anime as api

class Anime(object):
    def __init__(self, user_message, bot_send):
        self.user_message = user_message
        self.bot_send = bot_send
    async def info(self):
        if self.user_message.startswith('cuy/anime'):
            anime = self.user_message.split(" ", 1)
            if len(anime) == 1:
                embed = d.embeed(
                    "Anime",
                    ':clap: Masukan anime yang anda mau mendapatkan informasi:\n`cuy/anime [nama-anime]` :clap:'
                )
                await self.bot_send(embed=embed)
            else:
                resp = api.request(anime[1])

                if type(resp) is str:
                    embed = d.embeed(
                        ":information_source: Informasi Anime :information_source: ",
                        resp)
                    return await self.bot_send(embed=embed)

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
                await self.bot_send(embed=embed)
