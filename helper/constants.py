import discord
from datetime import datetime

request_help = ["cuy/help", "cuy/bantuan", "cuy/command", "cuy/cmd"]
request_stat = ["cuy/status", "cuy/stat", "cuy/st", "cuy/stats", "cuy/test", "cuy/ping", "cuy/p"]
request_welcome = ["cuy/hi", "cuy/helo", "cuy/hello", "cuy/halo", "cuy/hai", "cuy/oy", "cuy/helo"]
request_quote = ["cuy/quotes", "cuy/q", "cuy/quote", "cuy/quo", "cuy/kutipan"]
request_lyric = ["cuy/lirik", "cuy/lyric", "cuy/lyrics", "cuy/l"]
request_tiktok = ["cuy/tiktok", "cuy/foll", "cuy/tiktokfollower", "cuy/follower"]

data_covid_from = 'https://data.covid19.go.id'
today = datetime.today().strftime('%YY-%MM-%DD')
client = discord.Client()
