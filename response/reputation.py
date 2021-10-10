import helper.constants as c
import api.data_user_request as api

class Reputation:
  def __init__(self, sender, user_message, bot_say):
    self.sender = sender
    self.user_message = user_message
    self.bot_say = bot_say
  async def check(self):
    # I'm sure there's a better way to do this - Cendy
    args = self.user_message.split(' ')
    mention_self = str(self.sender.id) in args[0]
    if len(args) == 2:
        if args[1] == '++':
            if mention_self:
                await self.bot_say('Enggak boleh dong~ curang tahu!')
            else :
                cell = api.reputation_find(args[0])
                if cell == None:
                    api.reputation_insert(args[0])
                api.reputation_update(args[0], 'add')
                await self.bot_say(f'{args[0]} sekarang ada {api.reputation_value(args[0])} point')
        elif args[1] == '--':
            if mention_self:
                await self.bot_say('Kamu.. engak menghargai dirimu sendiri ya?')
            else :
                cell = api.reputation_find(args[0])
                if cell == None:
                    api.reputation_insert(args[0])
                api.reputation_update(args[0], 'reduce')
                await self.bot_say(f'{args[0]} sekarang ada {api.reputation_value(args[0])} point')
        elif args[1] == 'check':
            val = api.reputation_value(args[0])
            await self.bot_say(f'{args[0]} ada {api.reputation_value(args[0])} point')