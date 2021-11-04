import helper.constants as c
import helper.discord as d
from discord.ext import commands

class Events(c.cog):
    def __init__(self, client):
        self.client = client
    
    async def build_guild_embeed(self, guild, state):

        status = "Joined a new" if state == True else "Removed from a"
        emoji = u"\u2705" if state == True else u"\u274C"
        warna = "0x08FF00" if state == True else "0xFF1E01"
        angka = 1 if state == False else 0

        title = f"{emoji} {status} guild!"

        owner = await c.client.fetch_user(guild.owner_id)
        
        arr = {
            "footer": {"text": f"CuBot Now in {len(c.client.guilds)} guilds"},
            "field": [
                {"name": "ID:", "value": f"`{str(guild.id)}`", "inline": True},
                {"name": "Name:", "value": str(guild), "inline": True},
                {"name": "Owner:", "value": str(owner), "inline": True},
                {"name": "Members:", "value": str(guild.member_count - angka), "inline": True},
                {"name": "Channels:", "value": str(len(guild.channels) - len(guild.categories)), "inline": True},
                {"name": "Created at:", "value": str(guild.created_at.strftime('%e, %b %Y')), "inline": True},
            ]
        }

        embed = d.embeed(title,"", int(warna, 16), arr)
        return embed

    @c.cog.listener()
    async def on_guild_join(self, guild):
        recive = None

        for channel in guild.text_channels:
            if channel.permissions_for(guild.me).send_messages:
                recive = channel
                break
        
        arr = {
            "author": {"name": "CuyBot", "icon": c.bot_picture},
            "thumbnail": c.bot_picture
        }

        embed = d.embeed("", desc=
        """:tada: **Hai cuy! gw CuyBot.** \n 
        **Prefix saya adalah `cuy/`**
        **Gunakan command `cuy/help` untuk memulai.**
        **Jika kamu mempunyai masalah, [Join The Server](https://discord.com/invite/2qp6CxN8Df)**
        """, arr=arr)

        if eval(c.production):
            embed_log = await self.build_guild_embeed(guild, True)
            channel = c.client.get_channel(int(c.channel_log))
            await channel.send(embed=embed_log)

        if recive is not None:
            await recive.send(embed=embed)

    @c.cog.listener()
    async def on_guild_remove(self, guild):
        if eval(c.production):
            embed_log = await self.build_guild_embeed(guild, False)
            channel = c.client.get_channel(int(c.channel_log))
            await channel.send(embed=embed_log)

    @c.client.event
    async def on_command_error(ctx, error):
        bot_send = ctx.message.reply

        if isinstance(error, commands.CommandOnCooldown):
            message = f'''
            ```command(s) masih memiliki cooldown di server ini.\nMohon tunggu {int(error.retry_after)} detik lagi dan coba lagi.```'''

            embed = d.embeed(
                ":clock5: **COMMAND COOLDOWN** :clock5:",
                message,
                0xFFDB00,
            )
            await bot_send(embed=embed)

def setup(client):
    client.add_cog(Events(client))