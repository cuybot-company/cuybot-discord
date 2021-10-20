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
        # fungsi
        if len(data) == 3:
            match = int(data[1])
            wrawal = int(data[2])
            tWin = (match) * (wrawal/100)
            tLose = (match) - (tWin)
            await bot_send(f"Total kemenangan anda : {int(tWin)} \nTotal kekalahan anda  : {int(tLose)}")
        elif len(data) == 4:
            if data[3] < data[2]:
                #var
                match = int(data[1])
                wrawal = int(data[2])
                wrakhir = int(data[3])
                # anak bangke yg mau ke wr 100% padahal udh pernah kalah sama yg minta wr di atas 100%
                if int(data[3]) == 100:
                    await bot_send('Mana bisa bambang "-_ ')
                elif int(data[3]) > 100:
                    await bot_send('Iyain aja bang suka suka lu...')
                else:
                # var kalkulasi 
                    tWin = (match) * (wrawal/100)
                    tLose = (match) - (tWin)
                    sisaWr = 100 - (wrakhir)
                    wrResult = 100 / sisaWr
                    seratusPersen = (tLose) * (wrResult)
                    final = seratusPersen - match
                    lose = abs(int(final))
                    # await bot_send(f'{data[0]} ,{data[1]},{data[2]},{data[3]}')
                    await bot_send(f'Anda membutuhkan {lose} lose tanpa win untuk mendapatkan Win Rate {int(data[3])}%')
            else:
                match = int(data[1])
                wrawal = int(data[2])
                wrakhir = int(data[3])
                # anak bangke yg mau ke wr 100% padahal udh pernah kalah sama yg minta wr di atas 100%
                if int(data[3]) == 100:
                    await bot_send('Mana bisa bambang "-_ ')
                elif int(data[3]) > 100:
                    await bot_send('Iyain aja bang suka suka lu...')
                else:
                    tWin = (match) * (wrawal/100)
                    tLose = (match) - (tWin)
                    sisaWr = 100 - (wrakhir)
                    wrResult = 100 / sisaWr
                    seratusPersen = (tLose) * (wrResult)
                    final = seratusPersen - match
                    win = int(final)
                    await bot_send(f'Anda membutuhkan {win} win tanpa lose untuk mendapatkan Win Rate {int(data[3])}%')
        else:
            await bot_send("Command Help : cuy/wrcal [total match] [total wr] [target wr]")
            
def setup(client):
    client.add_cog(wrmlbb(client))