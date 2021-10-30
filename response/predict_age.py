import api.data_age_prediction as api
import helper.constants as c
import helper.command_help as cmd
from discord.ext import commands

command = next(filter(lambda x: x['name'] == "usia", cmd.list_help_cmd))
class Predict_Age(c.cog):
  def __init__(self, client):
    self.client = client
    
  @c.cmd.command(aliases=command["alias"])
  @commands.cooldown(1, command["cooldown"], commands.BucketType.user)
  async def prediction(self, ctx):
    user_message = ctx.message.content
    bot_send = ctx.message.reply
    data = user_message.split(" ", 1)
    if len(data) == 1:
        await bot_send(':x: Masukin dulu nama lu cuy :x:')
    elif len(data) > 2:
        await bot_send(':x: Hanya support menebak 1 kata nama (nama panggilan atau real name) :x:')
    else:
        requested_name = user_message.split(" ", 1)[1]
        predicting = api.predict(requested_name)
        await bot_send(predicting)

def setup(client):
    client.add_cog(Predict_Age(client))