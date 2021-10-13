import helper.constants as c
import api.data_face as api
import discord

class Face:
  def __init__(self, user_message, bot_send):
    self.user_message = user_message
    self.bot_send = bot_send
  async def guess_the_face(self):
    if any(word in self.user_message for word in c.request_face):
      message = self.user_message.split(" ", 2)
      if len(message) == 2:
        await self.bot_send('masukan nama orang yang mau ditebak namanya cuy')
      else:
        data = api.get_face()
        embed = discord.Embed(color = discord.Colour.red(),description= message[2] + ' wajahnya mirip ini kan?')
        embed.set_image(url = data[0]['url'])
        await self.bot_send(embed=embed)