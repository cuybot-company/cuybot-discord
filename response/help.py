import helper.constants as c

class Bot_Help(object):
  def __init__(self, user_message, bot_send):
    self.user_message = user_message
    self.bot_send = bot_send
  async def info(self):
    if any(help in self.user_message for help in c.request_help):
      await self.bot_send(':clap: --CUYBOT HELP-- :clap:\ncommand dasar pemanggilan bot: `cuy/(command)` tanpa tada kurung\n\n***command yang tersedia:***\n\n*ping bot status*:\n`cuy/status, cuy/stat, cuy/stats, cuy/test, cuy/ping`\n*pesan selamat datang*:\n`cuy/help, cuy/bantuan, cuy/command`\n*menyapa bot*: `cuy/helo, cuy/hi, cuy/hai, cuy/hello`\n*data covid hari in*: `cuy/covid`\n*quotes untuk memotivasi diri*:\n`cuy/quotes, cuy/quote, cuy/kutipan,`\n*Informasi Berita Paling TOP*: `cuy/berita`\n*informasi spesifikasi smartphone*: `cuy/hp, cuy/handphone, cuy/mobile, cuy/phone` spasi terbaru atau spasi merk hp-nya\n*cari lirik lagu*:\n`cuy/lirik, cuy/lyric, cuy/lyrics` spasi judul lagu dan atau spasi nama band nya\n\n\nBOT masih dalam tahap pengembangan lanjutan, untuk info lebih detail liat disini:\n`||xxxxxxxxx||`\n\n:wave::wave::wave:')