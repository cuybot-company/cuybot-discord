import helper.constants as c
import api.data_cuaca as api

class Cuaca(c.cog):
    def __init__(self, client):
        self.client = client
    @c.cmd.command(name="cuaca")
    async def send(self, ctx):
        user_message = ctx.message.content
        bot_send = ctx.message.reply
        print('request => ' + user_message)
        data = api.get_cuaca()
        await bot_send(data)

def setup(client):
    client.add_cog(Cuaca(client))
