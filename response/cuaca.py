import helper.constants as c
import api.data_cuaca as api

class cuaca(object):
    def __init__(self, user_message, bot_send):
        self.user_message = user_message
        self.bot_send = bot_send
    async def find_one(self):
        if self.user_message.startswith('cuy/cuaca'):
            request_cuaca = self.user_message.split(" ", 1)[1]
            data = api.get_cuaca(request_cuaca)
            await self.bot_send(data)
