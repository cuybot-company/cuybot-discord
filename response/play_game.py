import helper.constants as c
import logging

class play_game(object):
  def __init__(self, user_message, bot_send):
    self.user_message = user_message
    self.bot_send = bot_send

  async def message(self):
    # if any(x in self.user_message for x in c.request_play_game):
    #   await self.bot_send('wait a game ...')

    if self.user_message.startswith('cuy/play'):
            parameter = self.user_message.split()
            logging.info('This is an info message', parameter)
            # if len(parameter) == 1:
            #     await self.bot_send('masukkan kategori berita, contoh: \n`/berita nasional`\n`/berita internasional`\n`/berita ekonomi`\n`/berita olahraga`\n`/berita teknologi`\n`/berita hiburan`')
            # else:
            #     daftar_news = api.data_news(self.user_message)
            #     await self.bot_send(daftar_news)
