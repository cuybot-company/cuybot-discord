import api.data_user_request as api
import random
from random import choice
import helper.constants as c
import discord

win = False
your_try = []
count = 0
num = 0

class Reward(c.cog):
  def __init__(self, client):
    self.client = client
  @c.cmd.command(name="reward")
  async def reward(self, ctx):
    global count
    global num
    global win
    sender_id = ctx.message.author.id
    bot_send = ctx.message.reply
    if discord.utils.get(ctx.message.author.roles, name="Moderator 🔑"):
        if num == 0 and count == 0:
            num = random.randint(1, 100)
            count = 1
            win = False
            await bot_send(f'<@{sender_id}> lu harus dapatin angka **{num}**, goodluck! ketik `cuy/gacha` untuk menebak angka')
        else:
            await bot_send(f'slot reward sudah dikeluarkan, angka sebelum nya {num} belum selesai di gacha.')    
    else:
        await bot_send('maaf lu gak punya akses untuk eksekusi command ini')
  
  @c.cmd.command(name="gacha")
  async def gacha(self, ctx):
    global num
    global count
    global your_try
    global win
    sender_id = ctx.message.author.id
    bot_send = ctx.message.reply
    num2 = random.randint(1, 100)
    i = 0
    if win == True:
        await bot_send('Game udah selesai ya cuy!')
    else:
        while i < 1:
            if any(x in f'{num2}' for x in your_try):
                num2 = 5
            else:
                i = 1
            if i == 1:
                break
        
        if len(your_try) == 0:
            your_try = [f'{num2}']
        else:
            your_try.append(f'{num2}')
        
        if num == int(num2):
            api.reward_win_time(sender_id)
            count = 0
            num = 0
            your_try = []
            win = True
            await bot_send(f'<@{sender_id}> WIN!!! :clap:')
        else :
            await bot_send(f'{num2} Maaf kamu belum beruntung \nSilahkan coba lagi')

def setup(client):
    client.add_cog(Reward(client))
