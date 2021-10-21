import api.data_user_request as api
import random
from random import choice
import helper.constants as c
import discord

win = False
your_try = []

class Reward(c.cog):
  def __init__(self, client):
    self.client = client
  @c.cmd.command(name="reward")
  async def reward(self, ctx):
    sender_id = ctx.message.author.id
    bot_send = ctx.message.reply
    num = random.randint(1, 100)
    if discord.utils.get(ctx.message.author.roles, name="Moderator 🔑"):    
        await bot_send(f'<@{sender_id}> lu harus dapatin angka *{num}*, goodluck! ketik `cuy/gacha` untuk menebak angka')
    else:
        await bot_send('maaf lu gak punya akses untuk eksekusi command ini')
  
  @c.cmd.command(name="gacha")
  async def gacha(self, ctx):
    global your_try
    sender_id = ctx.message.author.id
    bot_send = ctx.message.reply
    user_db_num = api.reward_value(sender_id)
    num = random.randint(1, 100)
    i = 0
    while i < 1:
      if any(x in f'{num}' for x in your_try):
        num = random.randint(1, 100)
      else:
        i = 1
      if i == 1:
        break
    if len(your_try) == 0:
      your_try = [f'{num}']
    else:
      your_try.append(f'{num}')
    
    if num == int(user_db_num):
        api.reward_win_time(sender_id)
        await bot_send(f'<@{sender_id}> WIN!!! :clap:')
    else :
        await bot_send(f'{num} Maaf kamu belum beruntung \nSilahkan coba lagi')

def setup(client):
    client.add_cog(Reward(client))
