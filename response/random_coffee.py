import api.data_coffee as api
import helper.constants as c


class Coffee(object):
    def __init__(self, user_message, bot_send):
        self.user_message = user_message
        self.bot_send = bot_send

    async def findOne(self):
        if any(x in self.user_message for x in c.request_coffee):
            data_coffee = api.data_coffee()
            await self.bot_send(":coffee: ngopi dulu cuy " + "\n\n"+data_coffee)