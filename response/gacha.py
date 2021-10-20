import api.data_user_request as api
import random
import helper.constants as c
import asyncio

# This variable value should persist until the bot shut-off
semi_final_player = []
semi_final_number = None
win = False

class Reputation(c.cog):
  def __init__(self, client):
    self.client = client
  @c.cmd.command(name="semifinal")
  @c.cmd.has_role('Moderator 🔑')
  async def semifinal(self, ctx):
    global semi_final_player
    global semi_final_number
    user_message = ctx.message.content
    sender_id = ctx.message.author.id

    if len(semi_final_player) == 3:
        semi_final_number = random.randint(1, 100)
        message = await ctx.send(f'Semi-final bakal dimulai, dan dimulai oleh <@{sender_id}> dan angka yang di generate adalah...')
        asyncio.sleep(5)
        await message.edit(content=f'Semi-final bakal dimulai, dan dimulai oleh <@{sender_id}> dan angka yang di generate adalah {semi_final_number}')

  @c.cmd.command(name="reward")
  async def reward(self, ctx):
    sender_id = ctx.message.author.id
    bot_send = ctx.message.reply
    num = random.randint(1, 100)
    exist = api.reward_find(sender_id)
    
    if exist == None:
        api.reward_insert(sender_id, num)
        await bot_send(f'<@{sender_id}> kamu harus dapatin angka **{num}**, goodluck!')
  
  @c.cmd.command(name="gacha")
  async def gacha(self, ctx):
    global semi_final_player
    sender_id = ctx.message.author.id
    bot_send = ctx.message.reply
    user_db_num = api.reward_value(sender_id)
    num = random.randint(1, 100)
    
    if win or user_db_num == None:
        return
    if len(semi_final_player) == 3:
        if sender_id in semi_final_player:
            if num == semi_final_number:
                await bot_send(f'<@{sender_id}> Kamu menang! dengan angka : **{num}**')
                semi_final_player.append(sender_id)
            else :
                await bot_send(f'{num}')
        else:
            return

    if num == int(user_db_num):
        await bot_send(f'<@{sender_id}> Kamu masuk ke semi final! angka : **{num}**')
        semi_final_player.append(sender_id)
    else :
        await bot_send(f'{num}')

def setup(client):
    client.add_cog(Reputation(client))