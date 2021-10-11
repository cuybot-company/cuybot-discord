import helper.constants as c
import discord

class Bot_Help(object):
  def __init__(self, user_message, bot_send):
    self.user_message = user_message
    self.bot_send = bot_send
  async def info(self):
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
    embed.set_footer(text="Bot masih dalam tahap pengembangan.")
    await self.bot_send(embed=embed)