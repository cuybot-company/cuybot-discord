import helper.constants as c
import api.data_tiktok as api

class Tiktok(object):
    def __init__(self, user_message, bot_send):
        self.user_message = user_message
        self.bot_send = bot_send
    async def find(self):
        if any(x in self.user_message for x in c.request_tiktok):
            username = self.user_message.split(" ", 1)
            if len(username) == 1:
                await self.bot_send(':clap: Masukan username tiktok yang anda mau mendapatkan informasi:\n`cuy/tt [username]` :clap:')
            else:
                resp = api.info(username[1])
                await self.bot_send(resp)
