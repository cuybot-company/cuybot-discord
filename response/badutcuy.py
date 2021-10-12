from discord.ext import commands
import random
import os

client = commands.Bot(command_prefix='cuy/badutcuy ')

canvas = []

num = random.randint(0, 9)
end = True

@client.command()
async def start(ctx):
    global count
    global end

    if end:
        global canvas 
        canvas = [":white_large_square:", ":white_large_square:", ":white_large_square:", 
                  ":white_large_square:", ":white_large_square:", ":white_large_square:",
                  ":white_large_square:",":white_large_square:", ":white_large_square:"]
        end = False
        count = 0
        
        # print canvas
        line = ""
        for x in range(len(canvas)):
            if x == 2 or x == 5 or x == 8:
                line += " " + canvas[x]
                await ctx.send(line)
                line = ""
            else:
                line += " " + canvas[x]
        await ctx.send(":clap: Perkenalkan gue **BADUTCUY** :clap:\nCoba tebak gw ngumpet dimana?\n`ketik cuy/badutcuy atk [angka 1 - 9]`")    
    else:
        #game lagi jalan tapi ada user yang pengen ikutan
        await ctx.send("bentar tunggu game selesai dulu cuy! kalem atuh ih...")

@client.command()
async def atk(ctx, pos: int):
    global count
    global end
    global canvas
    if not end:
        mark = ""
        if ctx.author:
            if pos == num:
                mark = ":clown:"
            else:
                mark = ":poop:"
            
            if 0 < pos < 10 and canvas[pos - 1] == ":white_large_square:":
                canvas[pos - 1] = mark
                count += 1

                # print canvas
                line = ""
                for x in range(len(canvas)):
                    if x == 2 or x == 5 or x == 8:
                        line += " " + canvas[x]
                        await ctx.send(line)
                        line = ""
                    else:
                        line +=" " + canvas[x]      
                
                winnerCondition(pos, num)       
                if end == True:
                    await ctx.reply("ANJIM KETAUAN! *badutcuy* ada di posisi **" + str(num) + "**" + "\n\n:clap: SELAMAT :clap:\nlu menang cuy!\nDan lu berhasil dapetin GIVEAWAY berupa....\n..\n..\n**BUG**\nHOREEE!!!!:wave:\n\nmain lagi yu? ketik `cuy/badutcuy start` sekarang! berani?")
                elif count >= 9:
                    end = True
                    await ctx.send("Game selesai GAK ADA YANG MENANG!!! AH elah :mad:")
                else:
                    await ctx.send("Salah taeeekk!! :poop:\nAda yang bisa nebak lagi gw dimana?")
            else:
                await ctx.channel.reply("Maaf jurus itu mungkin udah di pake atau gak available cuy.")
        else:
            await ctx.send("Yo ramein mulai game **BADUTCUY** dengan cara ketik `cuy/badutcuy start` start")


def winnerCondition(pos, num):
    global end
    if pos == num:
        end = True

@start.error
async def kupError(ctx, err):
    if isinstance(err, commands.MissingRequiredArgument):
        await ctx.send("[MISS ARGS] upss..ulangi! ketik game cuy/badutcuy start")
    elif isinstance(err, commands.BadArgument):
        await ctx.send("[BAD ARGS] keknya command lu salah deh cuy, yu maen lagi cuy/badutcuy start")
@atk.error
async def atkError(ctx, err):
    if isinstance(err, commands.MissingRequiredArgument):
        await ctx.send("[MISS ARGS] sorry, gagak atk. error, ulangi lagi. ketik cuy/badutcuy start")
    elif isinstance(err, commands.BadArgument):
        await ctx.send("[BAD ARGS] sorry, gagak atk. error, ulangi lagi. ketik cuy/badutcuy start")
        
client.run(os.getenv('TOKEN'))