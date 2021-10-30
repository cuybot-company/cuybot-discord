import discord
from discord.ext import commands
from datetime import datetime
import helper.discord as d

request_update = ["up", "update"]
request_disconnect = ["dc", "disconnect"]
request_new_mobile = ["baru", "terbaru", "new"]

request_stat = ["cuy/status", "cuy/stat", "cuy/stats", "cuy/test", "cuy/ping"]
request_welcome = ["cuy/hi", "cuy/helo", "cuy/hello", "cuy/halo", "cuy/hai"]
request_quote = ["cuy/quotes", "cuy/quote", "cuy/kutipan"]
request_lyric = ["cuy/lirik", "cuy/lyric", "cuy/lyrics"]
request_mobile = ["cuy/mobile", "cuy/hp", "cuy/handphone", "cuy/phone"]
request_dota = ["cuy/dotalive", "cuy/dota-live", "cuy/dota-stream"]
request_mobilelegends = ["cuy/ml", "cuy/mlredeem"]

request_tiktok = ["cuy/tt", "cuy/tiktok"]

request_wallpaper = ["cuy/wp", "cuy/wallpaper"]
request_word = ["cuy/dictionary", "cuy/kamus", "cuy/Kamus", "cuy/Dictionary", "cuy/dict"]
request_face = ["cuy/tebak muka", "cuy/tebak wajah"]
request_coffee = ["cuy/coffee", "cuy/coffee hari ini", "cuy/ngopi", "cuy/ngopi dulu"]
request_avatar = ["cuy/avatar"]

data_covid_from = 'https://data.covid19.go.id'
today = datetime.today().strftime('%YY-%MM-%DD')
activity = discord.Activity(type=discord.ActivityType.watching, name="cuy/help")

# commands.when_mentioned_or("cuy/")

client = commands.Bot(command_prefix="cuy/", help_command=None, activity=activity)

@client.event
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

cmd = commands
cog = commands.Cog