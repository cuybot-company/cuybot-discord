import helper.discord as d

class Bot_Help(object):
  def __init__(self, sender, client, user_message, bot_send):
    self.user_message = user_message
    self.bot_send = bot_send
    self.client = client
    self.author = sender
  async def info(self):
    if self.user_message.startswith('cuy/help'):
      buttons = [u"\u23EA", u"\u25C0", u"\u25B6", u"\u23E9"]
      current = 0
      arr = {
        "footer": {"text": "Bot masih dalam tahap pengembangan."},
        "field": [
          {"name": "Ping bot status:", "value": "status, stat, stats, test, ping", "inline": True},
          {"name": "Menyapa bot", "value":"helo, hi, hai, hello", "inline":True},
          {"name": "Pesan selamat datang:", "value":"help, bantuan, command", "inline":True},
          {"name": "Berita", "value":"berita", "inline":True},
          {"name": "Data covid hari ini", "value":"covid", "inline":True},
          {"name": "Quotes untuk memotivasi diri", "value":"quotes, quote, kutipan", "inline":True},
          {"name": "Cari info spek handphone", "value":"hp *merk_hp*, handphone, mobile, phone", "inline":True},
          {"name": "Cari info daftar hp terbaru", "value":"hp baru, handphone baru, mobile baru, phone baru", "inline":True},
          {"name": "Cari info akun tiktok", "value": "tt nama-akun, tiktok nama-akun"},
          {"name": "Cari info anime", "value":"anime nama-anime", "inline":True},
          {"name": "Cari lirik lagu:", "value":"lirik, lyric, lyrics", "inline":True},
          {"name": "Cari info kamus bahasa", "value":"kamus, dict, dictionary", "inline":True},
          {"name": "Cari gambar atau wallpaper", "value": "wallpaper *genre*, wp *genre*, wallpaper, wp, wallpaper list, wp list", "inline": True},
          {"name": "Inspirasi kopi untuk menemani hari", "value":"ngopi dulu, coffee, kopi hari ini, ngopi", "inline":True},
          {"name": "Tebak usia iseng-isengan", "value":"usia *nama*", "inline":True},
          {"name": "Tebak wajah iseng-isengan", "value":"tebak wajah, tebak muka", "inline":True},
          {"name": "Random username", "value":"username", "inline":True},
          {"name": "Cari info Live Stream Dota", "value":"dotalive, dota-live, dotastream", "inline":True},
          {"name": "Mobile Legends Redeem", "value":"ml, mlredeem", "inline":True},
          {"name": "Game #1 (BADUT-CUY)", "value":"`. start`, `. stop`", "inline":True},
          {"name": "Game #2 (Tic Tac Toe) Bot", "value":"`tic start`", "inline":True},
          {"name": "Seputar reputasi member **cuyhub community**", "value":"rep help, rep @mention [angka], rep @mention", "inline":True},
        ]
      }

      split_field = [arr["field"][i:i + 10] for i in range(0, len(arr["field"]), 10)]
      arr["field"] = split_field[current]

      embed = d.embeed("Cuybot Help", "Command dasar pemanggilan bot cuy/(command) tanpa tanda kurung", 0x50d396, arr)

      msg = await self.bot_send(embed=embed)

      for button in buttons:
        await msg.add_reaction(button)

      while True:
        try:
          reaction, user = await self.client.wait_for('reaction_add', check=lambda reaction, user: user == self.author and reaction.emoji in buttons, timeout=60.0)
        except:
          await msg.clear_reactions()
        else:
          prev_page = current

          if reaction.emoji == buttons[0]:
            current = 0

          elif reaction.emoji == buttons[1]:
            if current > 0:
              current -= 1

          elif reaction.emoji == buttons[2]:
            if current < len(split_field)-1:
              current += 1

          elif reaction.emoji == buttons[3]:
            current = len(split_field)-1

          for button in buttons:
            await msg.remove_reaction(button, self.author)
          
          if current != prev_page:
            arr["field"] = split_field[current]
            embed = d.embeed("Cuybot Help", "Command dasar pemanggilan bot cuy/(command) tanpa tanda kurung", 0x50d396, arr)
            await msg.edit(embed=embed)