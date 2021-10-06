import helper.constants as c
import api.data_cuaca as api

class cuaca(object):
    async def __init__(self, user_message, bot_send):
        if user_message.startswith('cuy/cuaca'):
            print('request => ' + user_message)
            data = api.get_cuaca()
            await bot_send(data)
