import helper.constants as c

class Bot_Welcome(c.cog):
  def __init__(self, client):
    self.client = client
  @c.cmd.command(name='hi', aliases=['hello', 'helo', 'halo'])
  async def message(self, ctx):
    bot_send = ctx.message.reply
    user_message = ctx.message.content
    await bot_send(':partying_face: Oy cuy! :partying_face: \n\nperkenalkan cuy gw bot buatannya dea dan tim :yum:\ngw siap bantu ngasih info info sesuatu yang lu butuhin')

def setup(client):
    client.add_cog(Bot_Welcome(client))