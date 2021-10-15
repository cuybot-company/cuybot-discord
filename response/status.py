import helper.constants as c

class Bot_Status(c.cog):
  def __init__(self, client):
    self.client = client
  @c.cmd.command(name='status', aliases=['stat', 'stats', 'test', 'ping'])
  async def check(self, ctx):
    bot_send = ctx.message.reply
    await bot_send(':partying_face: CuyBot Masih Aktif! :partying_face:')

def setup(client):
    client.add_cog(Bot_Status(client))