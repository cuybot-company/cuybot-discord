import api.data_news as api


class news(object):
    def __init__(self, user_message, bot_send):
        self.user_message = user_message
        self.bot_send = bot_send

    async def find_one(self):
        if self.user_message.startswith('cuy/berita'):
            daftar_news = api.data_news()
            await self.bot_send(daftar_news)
