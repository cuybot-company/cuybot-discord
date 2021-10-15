import helper.constants as c
#from generate_username import generate_username

class Username(c.cog):
    def __init__(self, client):
        self.client = client
    @c.cmd.command(name="username")
    async def check(self, ctx):
        bot_send = ctx.message.reply
        user_message = ctx.message.content
        #await self.bot_send(f"nih cuy username nya ***{generate_username(1)[0]}***")
        await bot_send(f"nih cuy username nya ******")

def setup(client):
    client.add_cog(Username(client))