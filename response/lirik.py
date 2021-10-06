import api.data_lirik as api
import helper.constants as c

class lirik(object):
    def __init__(self, user_message, bot_send):
        self.user_message = user_message
        self.bot_send = bot_send

    async def find_one(self):
        if any(lyrics in self.user_message for lyrics in c.request_lyric):
            if self.user_message.isspace() == 'false':
                return ':clap: ketik judul lagunya atau berikut juga dengan nama bandnya :clap:'
            else:
                requested_song = self.user_message.split(" ", 1)[1]
                daftar_lagu = api.get_lirik(requested_song)
                await self.bot_send(daftar_lagu)
