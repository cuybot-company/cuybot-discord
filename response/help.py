import helper.constants as c

class Bot_Help(object):
  def __init__(self, user_message, bot_send):
    self.user_message = user_message
    self.bot_send = bot_send
  async def info(self):
    if any(help in self.user_message for help in c.request_help):
      await self.bot_send(':clap: --CUYBOT HELP-- :clap:\ncommand dasar pemanggilan bot: `cuy/(command)` tanpa tada kurung\n\n***command yang tersedia:***\n\n*ping bot status*:\n`/status, /stat, /stats, /test, /ping`\n*pesan selamat datang*:\n`/help, /bantuan, /command`\n*menyapa bot*: `/helo, /hi, /hai, /hello`\n*data covid hari in*: `/covid`\n*berita teknologi hari ini*: `/berita`\n*quotes untuk memotivasi diri*:\n`/quotes, /quote, /kutipan,`\n*Info Akun Tiktok*:\n`/tiktok, /follower, /like, /link, /video`\n*tebak usia (hiburan)*: `/usia [spasi] nama`\n*Informasi Berita Terkini*: `/berita`\n*informasi spesifikasi smartphone*: `/hp [spasi] merk hp, /handphone, /mobile, /phone`\n*Informasi daftar smartphone terbaru*: `/hp baru, /handphone baru, /mobile baru, /phone baru`\n*cari lirik lagu*:\n`/lirik, /lyric, /lyrics`\n*notes*: disarankan menggunakan kombinasi selengkapnya contoh: `/lirik avenged sevenfold dear god`\n\nBOT masih dalam tahap pengembangan lanjutan, untuk info lebih detail liat disini:\n`||xxxxxxxxx||`\n\n:wave::wave::wave:')