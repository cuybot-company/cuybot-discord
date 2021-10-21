import api.data_user_request as api
import random
from random import choice
import helper.constants as c

win = False

class Reward(c.cog):
  def __init__(self, client):
    self.client = client
  @c.cmd.command(name="reward")
  async def reward(self, ctx):
    sender_id = ctx.message.author.id
    bot_send = ctx.message.reply
    num = random.randint(1, 100)
    exist = api.reward_find(sender_id)
    if exist == None:
        api.reward_insert(sender_id, num)
        await bot_send(f'<@{sender_id}> lu harus dapatin angka **{num}**, goodluck! ketik `cuy/gacha` untuk menebak angka')
  
  @c.cmd.command(name="gacha")
  async def gacha(self, ctx):
    your_try = []
    sender_id = ctx.message.author.id
    bot_send = ctx.message.reply
    user_db_num = api.reward_value(sender_id)
    num = random.randint(1, 100)
    if num not in your_try:
        your_try.append(num)
    selection = choice([num for num in range(1,100) if num not in your_try])
    
    if win or user_db_num == None:
        return
    print(str(selection))
    
    if num == int(user_db_num):
        api.reward_win_time(sender_id)
        await bot_send(f'<@{sender_id}> WIN!!! :clap:')
    else :
        await bot_send(f'{num}')

def setup(client):
    client.add_cog(Reward(client))
