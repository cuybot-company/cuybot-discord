import helper.constants as c
import discord

class wrmlbb(c.cog):
    def __init__(self, client):
        self.client = client
    @c.cmd.command(name="wrcal")
    async def itung(client, ctx):
        user_message = ctx.message.content
        bot_send = ctx.message.reply
        data = user_message.split(' ', 3)

        tWin = int(data[1]) * (int(data[2])/100)
        tLose = int(data[1]) - tWin
        
        if len(data) == 1:
            await bot_send(f"Total match anda adalah {data[1]}")
        elif len(data) == 2:
          await bot_send(f'Total kemenangan : {tWin}\n Total kekalahan : {tLose}')        
        elif len(data) == 3:
            if int(data[3]) == 100:
                await bot_send('Ga bisa bro jgn maksa...')
            elif int(data[3]) >= 100:
                await bot_send('Punten bang wr max 100% "-_ ...')
            elif (int(data[3]) <= int(data[2])):
                sisaWr = 100 - int(data[3])
                wrResult = 100 / int(sisaWr)
                seratusPersen = int(tLose) * int(wrResult)
                final = int(seratusPersen) - int(data[3])
                lose = abs(final)
                await bot_send(f'Anda membutuhkan {lose} lose untuk menjadikan Win Rate {data[3]}%')
            else:
                sisaWr = 100 - int(data[3])
                wrResult = 100 / int(sisaWr)
                seratusPersen = int(tLose) * int(wrResult)
                final = int(seratusPersen) - int(data[3])
                win = final
                await bot_send(f'Anda membutuhkan {win} win untuk menjadikan Win Rate {data[3]}%')

def setup(client):
    client.add_cog(wrmlbb(client))