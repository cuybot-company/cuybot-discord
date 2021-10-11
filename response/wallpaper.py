import random
import api.data_wallpaper as api
class wallpaper(object):
    def __init__(self, user_message, bot_send):
        self.user_message = user_message
        self.bot_send = bot_send
    async def fetch(self):
        if(self.user_message.startswith("cuy/wallpaper") or self.user_message.startswith("cuy/wp")):
            parsedMessage = self.user_message.split(" ")
            parsedMessage.pop(0)
            if len(parsedMessage) == 0:
                genre = None
            else:
                genre = parsedMessage[0].capitalize()
            newMessage = await self.bot_send("`Fetching image`")
            await newMessage.edit(content = "`Fetching image.`")
            await newMessage.edit(content = "`Fetching image..`")
            await newMessage.edit(content = "`Fetching image...`")
            await newMessage.edit(content = "`Fetching image....`")
            imageURL = await api.get_wallpaper(genre)
            await newMessage.edit(content = imageURL)