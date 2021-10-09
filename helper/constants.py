import discord, os
from datetime import datetime

request_help = ["cuy/help", "cuy/bantuan", "cuy/command"]
request_stat = ["cuy/status", "cuy/stat", "cuy/stats", "cuy/test", "cuy/ping"]
request_welcome = ["cuy/hi", "cuy/helo", "cuy/hello", "cuy/halo", "cuy/hai"]
request_quote = ["cuy/quotes", "cuy/quote", "cuy/kutipan"]
request_lyric = ["cuy/lirik", "cuy/lyric", "cuy/lyrics"]
request_mobile = ["cuy/mobile", "cuy/hp", "cuy/handphone", "cuy/phone"]
request_new_mobile = ["baru", "terbaru", "new"]
request_dota = ["cuy/dotalive", "cuy/dota-live", "cuy/dota-stream"]

data_covid_from = 'https://data.covid19.go.id'
today = datetime.today().strftime('%YY-%MM-%DD')
client = discord.Client()
