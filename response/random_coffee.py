import api.data_coffee as api
import helper.constants as c
import discord


class Coffee(c.cog):
    def __init__(self, client):
        self.client = client
    @c.cmd.command(name='coffee', aliases=['ngopi'])
    async def findOne(self, ctx):
        user_message = ctx.message.content
        bot_send = ctx.message.reply
        if any(x in user_message for x in c.request_coffee):
            data_coffee = api.data_coffee()
            embed = discord.Embed(color = discord.Colour.green(),description= ":coffee: ngopi dulu cuy")
            embed.set_image(url = data_coffee)
            await bot_send(embed=embed)

def setup(client):
    client.add_cog(Coffee(client))