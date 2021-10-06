import os
import locale
import helper.constants as c

from response.status import bot_status
from response.welcome import bot_welcome
from response.help import bot_help
from response.covid import covid
from response.quote import quote
from response.lirik import lirik
from response.news import news
from response.mobile import mobile

from config.liveserver import liveserver
locale.setlocale(locale.LC_ALL, '')


@c.client.event
async def on_ready():
    print('logged in as {0.user} '.format(c.client))


@c.client.event
async def on_message(message):
    if message.author == c.client.user:
        return

    user_message = message.content
    bot_send = message.channel.send

    _botHelp = bot_help(user_message, bot_send)
    _botStatus = bot_status(user_message, bot_send)
    _botWelcome = bot_welcome(user_message, bot_send)
    _covid = covid(user_message, bot_send)
    _quotes = quote(user_message, bot_send)
    _lirik = lirik(user_message, bot_send)
    _news = news(user_message, bot_send)
    _mobile = mobile(user_message, bot_send)
    
    await _botHelp.info()
    await _botStatus.check()
    await _botWelcome.message()
    await _covid.find_latest()
    await _quotes.find_one()
    await _lirik.find_one()
    await _news.find_one()
    await _mobile.find_latest()

liveserver()
c.client.run(os.getenv('TOKEN'))
