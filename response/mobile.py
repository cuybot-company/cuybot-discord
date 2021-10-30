import api.data_mobile as api
import helper.constants as c

class Mobile(c.cog):
  def __init__(self, client):
    self.client = client
    
  @c.cmd.command(name="mobile", aliases=['hp'])
  async def find_latest(self, ctx):
    user_message = ctx.message.content
    bot_send = ctx.message.reply
    message = user_message.split(" ", 1)
    if len(message) == 1:
      await bot_send(':clap: tambahkan merk hp :clap:')
    else:
      merk_hp = user_message.split(" ", 1)[1]
      if any(x in merk_hp for x in c.request_new_mobile):
        data = api.get_mobile_latest()
        data_mobile = ''
        length = len(data) - 1
        i = 0
        while i < length:
          data_mobile = data_mobile +'Nama Hp : '+ data[i]['phone_name'] + '\n'
          i += 1
          if i == length:
            break
        await bot_send(data_mobile)
      else:
        data = api.get_mobile_spec(merk_hp)
        if data == 'empty':
          await bot_send('maaf saya tidak menemukan data hp yang kamu maksud\nketikan cuy/hp [spasi] brand [spasi] merk')
        else:
          data_spec = data['specifications']
          spec_hp = ''
          length_spec = len(data_spec) - 1
          idx = 0
          while idx < length_spec:
            idx_spec = 0
            while idx_spec < len(data_spec[idx]['specs']) - 1:
              spec_hp = spec_hp + '\n '+ data_spec[idx]['specs'][idx_spec]['key'] + ': ' + data_spec[idx]['specs'][idx_spec]['val'][0]
              idx_spec += 1
              if idx_spec == len(data_spec[idx]['specs']) - 1:
                break
            idx += 1
            if idx == length_spec:
              break
          await bot_send('**'+data['brand'] + ' ' + data['phone_name'] + '**' + '\n ' + spec_hp )

def setup(client):
    client.add_cog(Mobile(client))