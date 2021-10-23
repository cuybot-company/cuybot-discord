import helper.discord as d
import helper.constants as c
from discord.ext import commands
class Bot_Help(c.cog):
  def __init__(self, client):
    self.client = client

  @commands.cooldown(1, 4, commands.BucketType.user)
  @c.cmd.command(name="help")
  async def help(self, ctx):
    bot_send = ctx.message.reply
    user_message = ctx.message.content
    help_message = user_message.split(" ", 1)

    arr = {
      "footer": {"text": "Bot masih dalam tahap pengembangan."},
      "field": [
        {
          "name": "**Normal**", 
          "value": "```\nhelp\nping\nhi\n \n \n \n \n \n \n```", 
          "inline": True
        },
        {
          "name": "**Info**", 
          "value": "```\nberita\ncovid\nquote\nhp\ntiktok\nanime\nlirik\nkamus\ndotalive```", 
          "inline": True
        },
        {
          "name": "**Game**", 
          "value": "```\nbadut\ntic\n \n \n \n \n \n \n \n```", 
          "inline": True
        },
        {
          "name": "**Lainnya**", 
          "value": "```\nwallpaper\nngopi\nusia\nusername\ntebak\nmlredeem\nrep\n \n```", 
          "inline": True
        },
      ]
    }

    embed = d.embeed(
      ":clipboard: **Cuybot Command** :clipboard:", 
      "Prefix cuy bot adalah `cuy/`, kamu bisa mendapatkan info lebih tentang command bot dengan cara `cuy/help <command>`",
      0xFFDB00, 
    arr)

    await bot_send(embed=embed)

  @help.error
  async def help_error(self, ctx, error):
    bot_send = ctx.message.reply

    if isinstance(error, commands.CommandOnCooldown):
      message = f'''
      ```command(s) masih memiliki cooldown di server ini.\nMohon tunggu {int(error.retry_after)} detik lagi dan coba lagi.```'''

      embed = d.embeed(
        ":clock5: **COMMAND COOLDOWN** :clock5:",
        message,
        0xFFDB00,
      )
      await bot_send(embed=embed)

def setup(client):
    client.add_cog(Bot_Help(client))