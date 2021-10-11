import helper.constants as c
import discord

class Bot_Help(object):
  def __init__(self, user_message, bot_send):
    self.user_message = user_message
    self.bot_send = bot_send
  async def info(self):
    if any(help in self.user_message for help in c.request_help):
      await self.bot_send(':clap: --CUYBOT HELP-- :clap:\ncommand dasar pemanggilan bot: `cuy/(command)` tanpa tada kurung\n\n***command yang tersedia:***\n\n *ping bot status*:\n`/status, /stat, /stats, /test, /ping`\n*pesan selamat datang*:\n`/help, /bantuan, /command`\n*menyapa bot*: `/helo, /hi, /hai, /hello`\n*data covid hari in*: `/covid`\n*berita teknologi hari ini*: `/berita`\n*quotes untuk memotivasi diri*:\n`/quotes, /quote, /kutipan,`\n*Info Live Stream Dota*:\n`/dotalive, /dota-live, /dotastream`\n*tebak usia (hiburan)*: `/usia [spasi] nama`\n*Informasi Berita Terkini*: `/berita`\n*informasi spesifikasi smartphone*: `/hp [spasi] merk hp, /handphone, /mobile, /phone`\n*Informasi daftar smartphone terbaru*: `/hp baru, /handphone baru, /mobile baru, /phone baru`\n*cari lirik lagu*:\n`/lirik, /lyric, /lyrics`\n*notes*: disarankan menggunakan kombinasi selengkapnya contoh: `/lirik avenged sevenfold dear god`\n*Mobile Lengends Redeem*:\n`/ml, /mlredeem`\n*notes*: untuk mengklaim kode redeem digame mobile legends\n*Informasi Akun Tiktok*:\n`/tt, /tiktok`\n\nBOT masih dalam tahap pengembangan lanjutan, untuk info lebih detail liat disini:\n`||xxxxxxxxx||`\n\n:wave::wave::wave:')
      # untuk sementara hard code semua command
      embed=discord.Embed(title="Cuybot Help", description="Command dasar pemanggilan bot cuy/(command) tanpa tanda kurung", color=0x50d396)
      embed.add_field(name=" Ping bot status:", value="status, stat, stats, test, ping", inline=True)
      embed.add_field(name="Pesan selamat datang:", value="help, bantuan, command", inline=True)
      embed.add_field(name="Menyapa bot", value="helo, hi, hai, hello", inline=True)
      embed.add_field(name="Data covid hari ini", value="covid", inline=True)
      embed.add_field(name="Berita", value="berita", inline=True)
      embed.add_field(name="Quotes untuk memotivasi diri", value="quotes, quote, kutipan", inline=True)
      embed.add_field(name="Info Live Stream Dota", value="dotalive, dota-live, dotastream", inline=True)
      embed.add_field(name="Tebak usia", value="usia *nama*", inline=True)
      embed.add_field(name="Informasi spesifikasi smartphone", value="hp *merk_hp*, handphone, mobile, phone", inline=True)
      embed.add_field(name="Informasi daftar smartphone terbaru", value="hp baru, handphone baru, mobile baru, phone baru", inline=True)
      embed.add_field(name="Cari lirik lagu:", value="lirik, lyric, lyrics", inline=True)
      embed.add_field(name="Mobile Legends Redeem", value="ml, mlredeem", inline=True)
      embed.add_field(name="Reputation", value="rep", inline=True)
      embed.add_field(name="Wallpapers", value="wallpaper *genre*, wp *genre*, wallpaper, wp, wallpaper list, wp list")
      embed.set_footer(text="Bot masih dalam tahap pengembangan.")
      await self.bot_send(embed=embed)
