import api.data_coffee as api
import helper.constants as c
import discord
import helper.command_help as cmd
from discord.ext import commands

command = next(filter(lambda x: x['name'] == "ngopi", cmd.list_help_cmd))

class Coffee(c.cog):
    def __init__(self, client):
        self.client = client

    @c.cmd.command(aliases=command["alias"])
    @commands.cooldown(1, command["cooldown"], commands.BucketType.user)
    async def find_kopi(self, ctx):
        user_message = ctx.message.content
        bot_send = ctx.message.reply

        data_coffee = api.data_coffee()
        embed = discord.Embed(color = discord.Colour.green(),description= ":coffee: ngopi dulu cuy")
        embed.set_image(url = data_coffee)
        await bot_send(embed=embed)

def setup(client):
    client.add_cog(Coffee(client))