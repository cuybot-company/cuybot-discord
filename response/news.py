import api.data_news as api


class News(object):
    def __init__(self, user_message, bot_send):
        self.user_message = user_message
        self.bot_send = bot_send

    async def find_one(self):
        if self.user_message.startswith('cuy/berita'):
            parameter = self.user_message.split()
            if len(parameter) == 1:
                await self.bot_send('masukkan kategori berita, contoh: \n`/berita nasional`\n`/berita internasional`\n`/berita ekonomi`\n`/berita olahraga`\n`/berita teknologi`\n`/berita hiburan`')
            else:
                daftar_news = api.data_news(self.user_message)
                await self.bot_send(daftar_news)
