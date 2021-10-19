import random
import api.data_wallpaper as api
import helper.constants as c

class Wallpaper(c.cog):
    def __init__(self, client):
        self.client = client
    @c.cmd.command(name='wp', aliases=['wallpaper'])
    async def fetch(self, ctx):
      bot_send = ctx.message.reply
      user_message = ctx.message.content
      parsedMessage = user_message.split(" ")
      parsedMessage.pop(0)
      if len(parsedMessage) == 0:
        genre = None
      else:
        genre = parsedMessage[0].capitalize()
        newMessage = await bot_send("`Fetching image`")
        await newMessage.edit(content = "`Fetching image.`")
        await newMessage.edit(content = "`Fetching image..`")
        await newMessage.edit(content = "`Fetching image...`")
        await newMessage.edit(content = "`Fetching image....`")
        imageURL = await api.get_wallpaper(genre)
        await newMessage.edit(content = imageURL)

def setup(client):
    client.add_cog(Wallpaper(client))