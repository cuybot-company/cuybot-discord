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
# from response.tiktok import *
from response.mobile import mobile
from response.predict_age import predict_age
from response.user_request import user_request
from response.play_game import play_game

from config.liveserver import liveserver
locale.setlocale(locale.LC_ALL, '')


@c.client.event
async def on_ready():
    print('logged in as {0.user} '.format(c.client))


@c.client.event
async def on_message(message):
    if message.author == c.client.user:
        return

    sender = message.author
    user_message = message.content
    bot_send = message.reply

    _botHelp = bot_help(user_message, bot_send)
    _botStatus = bot_status(user_message, bot_send)
    _botWelcome = bot_welcome(user_message, bot_send)
    _covid = covid(user_message, bot_send)
    _quotes = quote(user_message, bot_send)
    _lirik = lirik(user_message, bot_send)
    _news = news(user_message, bot_send)
    # _tiktok = tiktok(user_message, bot_send)
    _mobile = mobile(user_message, bot_send)
    _predictAge = predict_age(user_message, bot_send)
    _userRequest = user_request(sender, user_message, bot_send)
    _botPlayGame = play_game(user_message, bot_send)

    
    await _botHelp.info()
    await _botStatus.check()
    await _botWelcome.message()
    await _covid.find_latest()
    await _quotes.find_one()
    await _lirik.find_one()
    await _news.find_one()
    # await _tiktok.account_info()
    # await _tiktok.followers()
    # await _tiktok.likes()
    # await _tiktok.videos()
    # await _tiktok.urls()
    await _mobile.find_latest()
    await _predictAge.prediction()
    await _userRequest.save()
    await _botPlayGame.message()

liveserver()
c.client.run(os.getenv('TOKEN'))
