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
        if merk_hp == 'baru':
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
          await self.bot_send(':clap: saya tidak mengerti apa yang anda maksud :clap:')