import api.data_user_request as api
import random
import helper.constants as c
import discord
from discord.ext import commands

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
            num = random.randint(1, 45)
            count = 1
            win = False
            await bot_send(f'<@{sender_id}> lu harus dapatin angka **{num}**, goodluck! ketik `cuy/gacha` untuk menebak angka')
        else:
            await bot_send(f'Upsss! slot reward sudah dikeluarkan, angka sebelum nya **{num}** belum selesai di gacha. ketik `cuy/gacha` untuk lanjutin games')    
    else:
        await bot_send('maaf lu gak punya akses untuk eksekusi command ini')
  @commands.cooldown(1, 15, commands.BucketType.user)
  @c.cmd.command(name="gacha")
  async def gacha(self, ctx):
    global num
    global count
    global win
    sender_id = ctx.message.author.id
    bot_send = ctx.message.reply
    num2 = random.randint(1, 45)
    if win == True:
        await bot_send(':clap: Game udah selesai ya cuy, selamat kepada pemenang reward :clap:')
    else:
        if num == int(num2):
            api.reward_win_time(sender_id, num2)
            count = 0
            num = 0
            win = True
            await bot_send(f':clap: <@{sender_id}> WIN!!\n langsung DM instagram bang de ya cuy @dea.afrizal buat dikirim reward nya. selamat!\n\n*reward didapatkan untuk pemenang yang paling cepat menang diantara pemenang2 lainnya. thank u* :clap:')
        else :
            if num != 0:
              await bot_send(f'angka reward adalah **{num}**, Lu kurang beruntung (tebakan lu **{num2}**) \nSilahkan coba lagi kuy!')
            else:
              print('blm mulai')
              return
  @c.cmd.command(name="gcstop")
  async def gcstop(self, ctx):
    bot_send = ctx.message.reply
    global win
    global count
    global num
    if discord.utils.get(ctx.message.author.roles, name="Moderator 🔑") and num != 0:
      win = False
      count = 0
      num = 0
      await bot_send("**Gacha telah dihentikan**")
    else:
      return
    
  @gacha.error
  async def gacha_error(self, ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
      if num != 0:
        await ctx.message.reply('`Tunggu antrian cuy, Lu dapet giliran ' + f'{round(error.retry_after, 2)}' + ' detik kemudian `')
      else:
        print('blm mulai')
        return
def setup(client):
    client.add_cog(Reward(client))
