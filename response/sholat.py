import api.data_sholat as api
import helper.constants as c

class Sholat(c.cog):
  def __init__(self, client):
    self.client = client
  @c.cmd.command(name='sholat', aliases=['shalat', 'solat'])
  async def find_one(self, ctx):
    user_message = ctx.message.content
    bot_send = ctx.message.reply
    await bot_send('Mohon Bersabar Yaa:)')
    data = api.get_jadwal_sholat(user_message)
    await bot_send(data)

def setup(client):
    client.add_cog(Sholat(client))