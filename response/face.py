import helper.constants as c
import api.data_face as api
import discord

class Face(c.cog):
  def __init__(self, client):
    self.client = client
  @c.cmd.command(name="tebak")
  async def guess_the_face(self, ctx):
    user_message = ctx.message.content
    bot_send = ctx.message.reply
    message = user_message.split(" ", 2)
    if len(message) == 2:
      await bot_send('masukan nama orang yang mau ditebak namanya cuy')
    else:
      data = api.get_face()
      embed = discord.Embed(color = discord.Colour.red(),description= message[2] + ' wajahnya mirip ini kan?')
      embed.set_image(url = data[0]['url'])
      await bot_send(embed=embed)

def setup(client):
    client.add_cog(Face(client))