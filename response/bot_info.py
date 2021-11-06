import helper.constants as c
from discord.ext import commands
import helper.discord as d
import helper.command_help as cmd

cmd_invite = next(filter(lambda x: x['name'] == "invite", cmd.list_help_cmd))
cmd_status = next(filter(lambda x: x['name'] == "status", cmd.list_help_cmd))
cmd_hi = next(filter(lambda x: x['name'] == "hi", cmd.list_help_cmd))

class Bot_Info(c.cog):
    def __init__(self, client):
        self.client = client

    @c.cmd.command(aliases=cmd_invite["alias"])
    @commands.cooldown(1, cmd_invite["cooldown"], commands.BucketType.user)
    async def invite_bot(self,ctx):
        bot_send = ctx.message.reply

        arr = {
            "author": {"name": "CuyBot", "icon": c.bot_picture}
        }

        embed = d.embeed(
            "Invite me to your server!",
            "[**Invite CuyBot**](https://discord.com/oauth2/authorize?client_id=894421026841165826&permissions=67584&scope=bot) | [**Support Server**](https://discord.com/invite/2qp6CxN8Df)",
            "",
            arr
        )

        await bot_send(embed=embed)

    @c.cmd.command(aliases=cmd_status["alias"])
    @commands.cooldown(1, cmd_status["cooldown"], commands.BucketType.user)
    async def check(self, ctx):
        bot_send = ctx.message.reply
        await bot_send(':partying_face: CuyBot Masih Aktif! :partying_face:')

    @c.cmd.command(aliases=cmd_hi["alias"])
    @commands.cooldown(1, cmd_hi["cooldown"], commands.BucketType.user)
    async def message(self, ctx):
        bot_send = ctx.message.reply
        await bot_send(':partying_face: Oy cuy! :partying_face: \n\nperkenalkan cuy gw bot buatannya dea dan tim :yum:\ngw siap bantu ngasih info info sesuatu yang lu butuhin')

def setup(client):
    client.add_cog(Bot_Info(client))