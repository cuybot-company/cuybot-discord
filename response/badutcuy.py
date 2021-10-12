import random

canvas = []

num = random.randint(0, 9)
end = True

class BadutStart:
    def __init__(ctx, sender, user_message, bot_say, bot_send):
        ctx.sender = sender
        ctx.user_message = user_message
        ctx.bot_say = bot_say
        ctx.bot_send = bot_send

    async def begin(ctx):
        if ctx.user_message.startswith('cuy/badut start'):
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
                        await ctx.bot_say(line)
                        line = ""
                    else:
                        line += " " + canvas[x]
                await ctx.bot_say(":clap: Perkenalkan gue **BADUTCUY** :clap:\nCoba tebak gw ngumpet dimana?\n`ketik cuy/badut atk [angka 1 - 9]`")    
            else:
                #game lagi jalan tapi ada user yang pengen ikutan
                await ctx.bot_send("bentar tunggu game selesai dulu cuy! kalem atuh ih...")
                
    async def atk(ctx):
        if ctx.user_message.startswith('cuy/badut atk'):    
            pos = int(ctx.user_message.split(' ')[2])
            global count
            global end
            global canvas
            if not end:
                mark = ""
                if ctx.sender:
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
                                await ctx.bot_say(line)
                                line = ""
                            else:
                                line +=" " + canvas[x]      
                        
                        winnerCondition(pos, num)       
                        if end == True:
                            await ctx.bot_send("ANJIM KETAUAN! *badutcuy* ada di posisi **" + str(num) + "**" + "\n\n:clap: SELAMAT :clap:\nlu menang cuy!\nDan lu berhasil dapetin GIVEAWAY berupa....\n..\n..\n**BUG**\nHOREEE!!!!:wave:\n\nmain lagi yu? ketik `cuy/badut start` sekarang! berani?")
                        elif count >= 9:
                            end = True
                            await ctx.bot_say("Game selesai GAK ADA YANG MENANG!!! AH elah :mad:")
                        else:
                            await ctx.bot_say("Salah taeeekk!! :poop:\nAda yang bisa nebak lagi gw dimana?")
                    else:
                        await ctx.bot_send("Maaf jurus itu mungkin udah di pake atau gak available cuy.")
                else:
                    await ctx.bot_say("Yo ramein mulai game **BADUTCUY** dengan cara ketik `cuy/badut start` start")

def winnerCondition(pos, num):
    global end
    if pos == num:
        end = True