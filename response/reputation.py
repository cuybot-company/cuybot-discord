import discord
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
        try :
            mention_self = str(self.sender.id) in args[0]
            if args[0] == 'help':
                embed=discord.Embed(title="Reputation", description="List of argument needed for Reputation", color=0x50d396)
                embed.add_field(name="Check user reputation", value="check @mention                      ", inline=True)
                embed.add_field(name="Add/decrease user reputation", value="@mention *point*", inline=True)
                await self.bot_say(embed=embed)
            elif args[0] == 'check':
                await self.bot_say(f'{args[1]} ada {api.reputation_value(args[1])} point')
            elif isinstance(int(args[1]), int):
                if mention_self:
                    await self.bot_say('Not allowed')
                elif int(args[1]) > 10 or int(args[1]) < -10:
                    await self.bot_say('Point not allowed')
                else :
                    if args[1].startswith('+'):
                        args[1] = args[1][1:]
                    cell = api.reputation_find(args[0])
                    if cell == None:
                        api.reputation_insert(args[0])
                    api.reputation_update(args[0], int(args[1]))
                    await self.bot_say(f'{args[0]} sekarang ada {api.reputation_value(args[0])} point')
        except:
            pass
