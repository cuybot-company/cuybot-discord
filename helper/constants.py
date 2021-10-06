import discord
from datetime import datetime

request_stat = ["cuy/status", "cuy/stat", "cuy/st", "cuy/stats", "cuy/test", "cuy/ping", "cuy/p"]
request_welcome = ["cuy/hi", "cuy/helo", "cuy/hello", "cuy/halo", "cuy/hai", "cuy/oy", "cuy/helo"]
data_covid_from = 'https://data.covid19.go.id'
today = datetime.today().strftime('%YY-%MM-%DD')
client = discord.Client()
