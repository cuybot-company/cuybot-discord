import helper.constants as c
import api.data_user_request as api

class Reputation:
  def __init__(self, sender, user_message, bot_say):
    self.sender = sender
    self.user_message = user_message
    self.bot_say = bot_say
  async def check(self):
    if self.user_message.startswith('cuy/rep') :
        args = self.user_message[7:].strip().split(' ')
        mention_self = str(self.sender.id) in args[1]
        if args[0] == 'tambah':
            if mention_self:
                await self.bot_say('Enggak boleh dong~ curang tahu!')
            else :
                cell = api.reputation_find(args[1])
                if cell == None:
                    api.reputation_insert(args[1])
                api.reputation_update(args[1], 'add')
                await self.bot_say(f'{args[1]} sekarang ada {api.reputation_value(args[1])} point')
        elif args[0] == 'kurang':
            if mention_self:
                await self.bot_say('Kamu.. engak menghargai dirimu sendiri ya?')
            else :
                cell = api.reputation_find(args[1])
                if cell == None:
                    api.reputation_insert(args[1])
                api.reputation_update(args[1], 'reduce')
                await self.bot_say(f'{args[1]} sekarang ada {api.reputation_value(args[1])} point')
        elif args[0] == 'cek':
            val = api.reputation_value(args[0])
            await self.bot_say(f'{args[0]} ada {api.reputation_value(args[0])} point')
