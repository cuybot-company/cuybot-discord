import os
import locale
import helper.constants as c

from response.status import Bot_Status
from response.welcome import Bot_Welcome
from response.help import Bot_Help
from response.covid import Covid
from response.quote import Quote
from response.lirik import Lirik
from response.news import News
from response.mobile import Mobile
from response.predict_age import Predict_Age
from response.user_request import User_Request
from response.reputation import Reputation

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
    bot_say = message.channel.send

    _botHelp = Bot_Help(user_message, bot_send)
    _botStatus = Bot_Status(user_message, bot_send)
    _botWelcome = Bot_Welcome(user_message, bot_send)
    _covid = Covid(user_message, bot_send)
    _quotes = Quote(user_message, bot_send)
    _lirik = Lirik(user_message, bot_send)
    _news = News(user_message, bot_send)
    _mobile = Mobile(user_message, bot_send)
    _predictAge = Predict_Age(user_message, bot_send)
    _userRequest = User_Request(sender, user_message, bot_send)
    _reputation = Reputation(sender, user_message, bot_say)
    
    await _botHelp.info()
    await _botStatus.check()
    await _botWelcome.message()
    await _covid.find_latest()
    await _quotes.find_one()
    await _lirik.find_one()
    await _news.find_one()
    await _mobile.find_latest()
    await _predictAge.prediction()
    await _userRequest.save()
    await _reputation.check()

liveserver()
c.client.run(os.getenv('TOKEN'))