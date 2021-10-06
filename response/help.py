import helper.constants as c

class bot_help(object):
  def __init__(self, user_message, bot_send):
    self.user_message = user_message
    self.bot_send = bot_send
  async def info(self):
    if any(x in self.user_message for x in c.request_help):
      await self.bot_send(':clap: --CUYBOT HELP-- :clap:\ncommand dasar pemanggilan bot: `cuy/(command)` tanpa tada kurung\n***command yang tersedia:***\n\n*ping bot status*:\n`cuy/status, cuy/stat, cuy/st, cuy/stats, cuy/test, cuy/ping, cuy/p`\n*pesan selamat datang*:\n`cuy/help, cuy/h, cuy/bantuan, cuy/command, cuy/cmd`\n*data covid hari in*: `cuy/covid`\n*quotes untuk memotivasi diri*:\n`cuy/quotes, cuy/q, cuy/quote, cuy/quo, cuy/kutipan,`\n*cari lirik lagu*:\n`cuy/lirik[spasi]judul lagu, cuy/lirik[spasi judul lagi][nama band], cuy/lyric[spasi nama band / judul lagu], cuy/lyrics[spasi nama band / judul lagu], cuy/l[spasi nama band / judul lagu]`\n*notes*: disarankan menggunakan kombinasi selengkapnya contoh: `cuy/lirik avenged sevenfold dear god`\n\nBOT masih dalam tahap pengembangan lanjutan, untuk info lebih detail liat disini:\n`https://cuybot-discord.afrizaldea.repl.co`\n\n:wave::wave::wave:')