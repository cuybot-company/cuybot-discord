import discord
import api.data_user_request as api
import re

class Reputation:
  def __init__(self, sender, user_message, bot_say):
    self.sender = sender
    self.user_message = user_message
    self.bot_say = bot_say
  async def check(self):
    if self.user_message.startswith('cuy/rep') :
        args = self.user_message[7:].strip().split(' ')
        id_pattern = re.compile("^<@!?\d+>")
        try :
            mention_self = str(self.sender.id) in args[0]
            if args[0] == 'help':
                embed=discord.Embed(title="Reputation", description="List of argument needed for Reputation", color=0x50d396)
                embed.add_field(name="Untuk melihat reputasi member saat ini", value="@mention", inline=True)
                embed.add_field(name="Untuk memberikan member point", value="@mention *point*", inline=True)
                await self.bot_say(embed=embed)
            elif bool(id_pattern.match(args[0])) and len(args) < 2:
                args[0] = args[0].replace('!', '')
                await self.bot_say(f':tada: reputasi {args[0]} saat ini: :tada:\n`{api.reputation_value(args[0])} point`\n\n *tips: lempar reputasi ke member yang dirasa membantu komunitas ini menjadi lebih berkembang lagi.*\ngunakan `cuy/rep help` untuk penggunaan command reputasi.')
            elif isinstance(int(args[1]), int):
                if mention_self:
                    await self.bot_say('Sorry cuy gak bisa ngasih point ke diri sendiri ya!')
                elif int(args[1]) > 10 or int(args[1]) < -10:
                    await self.bot_say('Maksimal cuma bisa lempar 10 point plus ataupun 10 point minus')
                else :
                    args[0] = args[0].replace('!', '')
                    if args[1].startswith('+'):
                        args[1] = args[1][1:]
                    cell = api.reputation_find(args[0])
                    if cell == None:
                        api.reputation_insert(args[0])
                    api.reputation_update(args[0], int(args[1]))
                    await self.bot_say(f':clap: thanks udah apresiasi {args[0]} dan menambahkan {str(args[1])} point :clap:')
        except:
            pass