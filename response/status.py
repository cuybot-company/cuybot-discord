import helper.constants as c
import helper.command_help as cmd
from discord.ext import commands

command = next(filter(lambda x: x['name'] == "status", cmd.list_help_cmd))

class Bot_Status(c.cog):
  def __init__(self, client):
    self.client = client

  @c.cmd.command(aliases=command["alias"])
  @commands.cooldown(1, command["cooldown"], commands.BucketType.user)
  async def check(self, ctx):
    bot_send = ctx.message.reply
    await bot_send(':partying_face: CuyBot Masih Aktif! :partying_face:')

def setup(client):
    client.add_cog(Bot_Status(client))