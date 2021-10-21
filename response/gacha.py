import api.data_user_request as api
import random
from random import choice
import helper.constants as c
import discord

win = False
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
            await bot_send(f'Upsss! slot reward sudah dikeluarkan, angka sebelum nya **{num}** belum selesai di gacha. ketik `cuy/gacha` untuk lanjutin games')    
    else:
        await bot_send('maaf lu gak punya akses untuk eksekusi command ini')
  
  @c.cmd.command(name="gacha")
  async def gacha(self, ctx):
    global num
    global count
    global win
    sender_id = ctx.message.author.id
    bot_send = ctx.message.reply
    num2 = random.randint(1, 100)
    if win == True:
        await bot_send(':clap: Game udah selesai ya cuy, selamat kepada pemenang reward :clap:')
    else:
        if num == int(num2):
            api.reward_win_time(sender_id)
            count = 0
            num = 0
            win = True
            await bot_send(f':clap: <@{sender_id}> WIN!!\n langsung DM instagram bang de ya cuy @dea.afrizal buat dikirim reward nya. selamat!\n\n*reward didapatkan untuk pemenang yang paling cepat menang diantara pemenang2 lainnya. thank u* :clap:')
        else :
            await bot_send(f'angka reward adalah **{num}**, Lu kurang beruntung (tebakan lu **{num2}**) \nSilahkan coba lagi kuy!')

def setup(client):
    client.add_cog(Reward(client))
