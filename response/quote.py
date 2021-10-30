import api.data_quote as api
import helper.constants as c
import helper.command_help as cmd
from discord.ext import commands

command = next(filter(lambda x: x['name'] == "quotes", cmd.list_help_cmd))
class Quote(c.cog):
  def __init__(self, client):
    self.client = client

  @c.cmd.command(aliases=command["alias"])
  @commands.cooldown(1, command["cooldown"], commands.BucketType.user)
  async def find_quotes(self, ctx):
    bot_send = ctx.message.reply
    await bot_send('Tunggu sebentar saya carikan dulu quotes menarik untuk kamu ')
    data = api.get_quotes()
    await bot_send(data)

def setup(client):
    client.add_cog(Quote(client))