import api.data_user_request as api

class User_Request:
  def __init__(self, sender, user_message, bot_send):
    self.sender = sender
    self.user_message = user_message
    self.bot_send = bot_send
  async def save(self):
    if self.user_message.startswith('cuy/request'):
        data = self.user_message.split(" ", 1)
        if len(data) == 1:
            await self.bot_send(':clap: ketik request apa yang mau lu minta cuy! :clap:')
        else:
            api.insert(self.sender, data[1])
            await self.bot_send('Thanks cuy, request lu berhasil **tersimpan** di **database** kita.\n\n*notes: tolong gunain fitur ini dengan bijak ya!*\n\nsemua data request dari kalian bisa di follow up via private channel #request.\n**Dan hanya bisa di akses oleh member dengan privilage minimal @superior**')