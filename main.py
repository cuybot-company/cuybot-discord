import os
import locale
import helper.constants as c

from response.status import Bot_Status
from response.welcome import Bot_Welcome
from response.help import Bot_Help
from response.covid import Covid
from response.dota import Dota
from response.quote import Quote
from response.lirik import Lirik
from response.news import News
from response.mobile import Mobile
from response.predict_age import Predict_Age
from response.user_request import User_Request
from response.reputation import Reputation
from response.mobilelegends import Mobile_Legends
from response.badutcuy import BadutStart
from response.username import Username
from response.tiktok import Tiktok
from response.server import Server
from response.wallpaper import wallpaper
from response.word import Dictionary
from response.anime import Anime
from response.face import Face
from response.random_coffee import Coffee
from response.bot_tictactoe import TicTacToeBot
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

    _botHelp = Bot_Help(sender, c.client, user_message, bot_send)
    _botStatus = Bot_Status(user_message, bot_send)
    _botWelcome = Bot_Welcome(user_message, bot_send)
    _covid = Covid(user_message, bot_send)
    _dota = Dota(user_message, bot_send)
    _quotes = Quote(user_message, bot_send)
    _lirik = Lirik(user_message, bot_send)
    _news = News(user_message, bot_send)
    _mobile = Mobile(user_message, bot_send)
    _predictAge = Predict_Age(user_message, bot_send)
    _mobilelegends = Mobile_Legends(user_message, bot_send)
    _userRequest = User_Request(sender, user_message, bot_send)
    _reputation = Reputation(sender, user_message, bot_say)
    _badutStart = BadutStart(sender, c.client, user_message, bot_say, bot_send)
    _username = Username(user_message, bot_send)
    _tiktok = Tiktok(user_message, bot_send)
    _server = Server(sender, c.client, user_message, bot_send)
    _wallpaper = wallpaper(user_message, bot_send)
    _dictionary = Dictionary(user_message, bot_send)
    _anime = Anime(user_message, bot_send)
    _face = Face(user_message, bot_send)
    _coffee = Coffee(user_message, bot_send)
    _ttt = TicTacToeBot(sender, c.client, user_message, bot_say, bot_send)
    
    await _botHelp.info()
    await _botStatus.check()
    await _botWelcome.message()
    await _covid.find_latest()
    await _dota.live()
    await _quotes.find_one()
    await _lirik.find_one()
    await _news.find_one()
    await _mobile.find_latest()
    await _predictAge.prediction()
    await _mobilelegends.redeem()
    await _userRequest.save()
    await _reputation.check()
    await _badutStart.begin()
    await _username.check()
    await _tiktok.find()
    await _server.control()
    await _wallpaper.fetch()
    await _dictionary.Dictionary_word()
    await _anime.info()
    await _face.guess_the_face()
    await _coffee.findOne()
    await _ttt.begin()

liveserver()
c.client.run(os.getenv('TOKEN'))