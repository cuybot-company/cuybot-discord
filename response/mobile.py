import api.data_mobile as api
import helper.constants as c

class mobile(object):
  def __init__(self, user_message, bot_send):
    self.user_message = user_message
    self.bot_send = bot_send
  async def find_latest(self):
    if any(x in self.user_message for x in c.request_mobile):
      message = self.user_message.split(" ", 1)
      if len(message) == 1:
        await self.bot_send(':clap: tambahkan merk hp :clap:')
      else:
        merk_hp = self.user_message.split(" ", 1)[1]
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
          await self.bot_send(data_mobile)
        else:
          data = api.get_mobile_spec(merk_hp)
          if data == 'empty':
            await self.bot_send(':clap: Maaf saya tidak tau handphone '+ merk_hp + ' :clap:')
          else:
            await self.bot_send.reply('> `Brand : ' + data['brand'] + '`'+'\n > `Nama handphone : ' + data['phone_name'] + '`'+'\n > `Release : '+data['release_date']+ '`'+'\n > `Dimensi : '+data['dimension']+ '`'+'\n > `OS : '+data['os']+'`'+'\n > `Storage : '+data['storage']+ '`'+'\n > `Network : '+data['specifications'][0]['specs'][0]['val'][0]+ '`'+'\n > `Status : '+data['specifications'][1]['specs'][1]['val'][0]+'`'+'\n > `Berat : '+ data['specifications'][2]['specs'][1]['val'][0] + '`'+'\n > `Build : ' + data['specifications'][2]['specs'][2]['val'][0] + '`'+'\n > `SIM : ' + data['specifications'][2]['specs'][3]['val'][0] + '`', mention_author=True)