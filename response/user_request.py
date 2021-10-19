import api.data_user_request as api
import discord
import helper.constants as c
class User_Request(c.cog):
  def __init__(self, client):
    self.client = client
  @c.cmd.command(name="request")
  async def save(self, ctx):
    sender = ctx.message.author
    bot_send = ctx.message.reply
    user_message = ctx.message.content
    data = user_message.split(" ", 1)
    if len(data) == 1:
        embed=discord.Embed(
          title="Request", 
          description=":clap: ketik request apa yang mau lu minta cuy! :clap:", 
          color=discord.Color.random()
        )
        await bot_send(embed=embed)
    else:
        api.insert(sender, data[1])
        embed=discord.Embed(
          title="Request", 
          description="Thanks cuy, request lu berhasil **tersimpan** di **database** kita.\n\n*notes: tolong gunain fitur ini dengan bijak ya!*\n\nsemua data request dari kalian bisa di follow up via private channel #request.\n**Dan hanya bisa di akses oleh member dengan privilage minimal @superior**", 
          color=discord.Color.random()
        )
        await bot_send(embed=embed)

def setup(client):
    client.add_cog(User_Request(client))