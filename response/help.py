import helper.constants as c

class bot_help(object):
  def __init__(self, user_message, bot_send):
    self.user_message = user_message
    self.bot_send = bot_send
  async def info(self):
    if any(x in self.user_message for x in c.request_help):
      await self.bot_send(':clap: --CUYBOT HELP-- :clap:\n\ncommand dasar pemanggilan bot: `cuybot/(command)` tanpa tada kurung\n\ncommand yang tersedia:\n\n**ping bot status**:\n`cuy/status, cuy/stat, cuy/st, cuy/stats, cuy/test, cuy/ping, cuy/p`\n**pesan selamat datang**:\n`cuy/help, cuy/h, cuy/bantuan, cuy/command, cuy/cmd`\n**data covid hari ini**: `cuybot/covid`\n**cari lirik lagu**:\n`cuybot/lirik[spasi]judul lagu\ncuybot/lirik[spasi judul lagi][nama band]\ncuybot/lyric[spasi nama band / judul lagu]\ncuybot/lyrics[spasi nama band / judul lagu]\ncuybot/l[spasi nama band / judul lagu]`\n\n***notes***: disarankan menggunakan kombinasi selengkapnya contoh: cuybot/lirik avenged sevenfold dear god\n**quotes untuk memotivasi diri**:\n`cuybot/quotes cuybot/q cuybot/quote cuybot/quo cuybot/kutipan`\n\nBOT masih dalam tahap pengembangan lanjutan, untuk info lebih detail liat disini:\n`https://cuybot-discord.afrizaldea.repl.co`\n\n:wave::wave::wave:')