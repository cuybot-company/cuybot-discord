import discord
from discord.ext import commands
from datetime import datetime

request_stat = ["cuy/status", "cuy/stat", "cuy/stats", "cuy/test", "cuy/ping"]
request_welcome = ["cuy/hi", "cuy/helo", "cuy/hello", "cuy/halo", "cuy/hai"]
request_quote = ["cuy/quotes", "cuy/quote", "cuy/kutipan"]
request_lyric = ["cuy/lirik", "cuy/lyric", "cuy/lyrics"]
request_mobile = ["cuy/mobile", "cuy/hp", "cuy/handphone", "cuy/phone"]
request_new_mobile = ["baru", "terbaru", "new"]
request_dota = ["cuy/dotalive", "cuy/dota-live", "cuy/dota-stream"]
request_mobilelegends = ["cuy/ml", "cuy/mlredeem"]
request_tiktok = ["cuy/tt", "cuy/tiktok"]
request_update = ["up", "update"]
request_disconnect = ["dc", "disconnect"]
request_wallpaper = ["cuy/wp", "cuy/wallpaper"]
request_word = ["cuy/dictionary", "cuy/kamus", "cuy/Kamus", "cuy/Dictionary", "cuy/dict"]
request_face = ["cuy/tebak muka", "cuy/tebak wajah"]
request_coffee = ["cuy/coffee", "cuy/coffee hari ini", "cuy/ngopi", "cuy/ngopi dulu"]
request_avatar = ["cuy/avatar"]

data_covid_from = 'https://data.covid19.go.id'
today = datetime.today().strftime('%YY-%MM-%DD')
client = commands.Bot(command_prefix="cuy/", help_command=None)
cmd = commands
cog = commands.Cog