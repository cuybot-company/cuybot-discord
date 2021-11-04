import discord
from discord.ext import commands
from datetime import datetime

production = "False"
channel_log = "905782097912922132"

request_update = ["up", "update"]
request_disconnect = ["dc", "disconnect"]
request_new_mobile = ["baru", "terbaru", "new"]

bot_picture="https://cdn.discordapp.com/avatars/894421026841165826/aede7e6874a861e91f15277c9ac3388c.webp?size=4096"
data_covid_from = 'https://data.covid19.go.id'
today = datetime.today().strftime('%YY-%MM-%DD')
activity = discord.Activity(type=discord.ActivityType.watching, name="cuy/help")

# commands.when_mentioned_or("cuy/")

client = commands.Bot(command_prefix="cuy/", help_command=None, activity=activity)

cmd = commands
cog = commands.Cog