import helper.discord as d

class Bot_Help(object):
  def __init__(self, user_message, bot_send):
    self.user_message = user_message
    self.bot_send = bot_send
  async def info(self):
    if self.user_message.startswith('cuy/help'):
      arr = {
        "footer": {"text": "Bot masih dalam tahap pengembangan."},
        "field": [
          {"name": "Ping bot status:", "value": "status, stat, stats, test, ping", "inline": True},
          {"name": "Server Control", "value": "`server up (update)`, `server update` `server dc (disconnect)` `server disconnect`", "inline":True},
          {"name": "Pesan selamat datang:", "value":"help, bantuan, command", "inline":True},
          {"name": "Menyapa bot", "value":"helo, hi, hai, hello", "inline":True},
          {"name": "Data covid hari ini", "value":"covid", "inline":True},
          {"name": "Berita", "value":"berita", "inline":True},
          {"name": "Quotes untuk memotivasi diri", "value":"quotes, quote, kutipan", "inline":True},
          {"name": "Info Live Stream Dota", "value":"dotalive, dota-live, dotastream", "inline":True},
          {"name": "Informasi Akun TikTok", "value": "tt nama-akun, tiktok nama-akun"},
          {"name": "Tebak usia", "value":"usia *nama*", "inline":True},
          {"name": "Informasi spesifikasi smartphone", "value":"hp *merk_hp*, handphone, mobile, phone", "inline":True},
          {"name": "Informasi daftar smartphone terbaru", "value":"hp baru, handphone baru, mobile baru, phone baru", "inline":True},
          {"name": "Cari lirik lagu:", "value":"lirik, lyric, lyrics", "inline":True},
          {"name": "Mobile Legends Redeem", "value":"ml, mlredeem", "inline":True},
          {"name": "Reputation", "value":"rep help", "inline":True},
          {"name": "Random username", "value":"username", "inline":True},
          {"name": "Wallpapers", "value": "wallpaper *genre*, wp *genre*, wallpaper, wp, wallpaper list, wp list", "inline": True}
        ]
      }
      embed = d.embeed("Cuybot Help", "Command dasar pemanggilan bot cuy/(command) tanpa tanda kurung", 0x50d396, arr)
      await self.bot_send(embed=embed)