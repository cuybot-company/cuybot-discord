import helper.constants as c
import helper.command_help as cmd
from discord.ext import commands

command = next(filter(lambda x: x['name'] == "hi", cmd.list_help_cmd))

class Bot_Welcome(c.cog):
  def __init__(self, client):
    self.client = client

  @c.cmd.command(aliases=command["alias"])
  @commands.cooldown(1, command["cooldown"], commands.BucketType.user)
  async def message(self, ctx):
    bot_send = ctx.message.reply
    await bot_send(':partying_face: Oy cuy! :partying_face: \n\nperkenalkan cuy gw bot buatannya dea dan tim :yum:\ngw siap bantu ngasih info info sesuatu yang lu butuhin')

def setup(client):
    client.add_cog(Bot_Welcome(client))