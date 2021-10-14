import random
import api.data_user_request as api

canvas = []
end = True

class BadutStart:
    def __init__(ctx, sender, user_message, bot_say, bot_send):
        ctx.sender = sender
        ctx.user_message = user_message
        ctx.bot_say = bot_say
        ctx.bot_send = bot_send
    async def begin(ctx):
        if ctx.user_message.startswith('cuy/. start'):
            global num
            num = random.randint(1, 9)      
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
                i = 0
                while i < 9:
                  if i == 0:
                    line = canvas[i]
                  elif i == 3 or i == 6:
                    line = line + canvas[i]
                  elif i == 2 or i == 5 or i == 8:
                    line = line + '     ' + canvas[i] +'\n\n'
                  else:
                    line = line + '     ' + canvas[i]
                  i += 1
                  if i == 9:
                    break
                await ctx.bot_say(line)
                # for x in range(len(canvas)):
                #     if x == 2 or x == 5 or x == 8:
                #         line += " " + canvas[x]
                #         await ctx.bot_say(line)
                #         line = ""
                #     else:
                #         line += " " + canvas[x]
                await ctx.bot_say(":clap: Perkenalkan gue **BADUTCUY** :clap:\nCoba tebak gw ngumpet dimana?\n`ketik cuy/. atk [angka 1 - 9]`")    
            else:
                #game lagi jalan tapi ada user yang pengen ikutan
                await ctx.bot_send(":raised_hand: bentar tunggu game selesai dulu cuy! chill...:raised_hand:")
                
    async def atk(ctx):
        if ctx.user_message.startswith('cuy/. a'):    
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
                        i = 0
                        while i < 9:
                          if i == 0:
                            line = canvas[i]
                          elif i == 3 or i == 6:
                            line = line + canvas[i]
                          elif i == 2 or i == 5 or i == 8:
                            line = line + '     ' + canvas[i] +'\n\n'
                          else:
                            line = line + '     ' + canvas[i]
                          i += 1
                          if i == 9:
                            break
                        await ctx.bot_say(line)
                        winnerCondition(pos)    
                        if end == True:
                            addPoint(ctx.sender.id)
                            await ctx.bot_send("ANJIM KETAUAN! *badutcuy* ada di posisi **" + str(num) + "**" + "\n\n:first_place: CONGRATS :first_place:\nSebagai hadiahnya cuybot ngasih lu **1 point** reputasi di *cuyhub community* :star_struck:\ncek total point lu dengan cara `cuy/rep @mention`\n\nmain lagi yu? ketik `cuy/. start` sekarang! berani?")
                        elif count >= 3:
                            end = True
                            await ctx.bot_say(":person_juggling: **Game selesai** :person_juggling:\ngak ada yang menang cuy!\nkesempatan cuma 3x tebak dalam 1 permainan, AH elah gimanasiiiii! :rage:\n\nYo ramein mulai game **BADUTCUY** dengan cara ketik `cuy/. start`")
                        else:
                            await ctx.bot_say(":poop: Salah yeeee... :poop:\nAda yang bisa nebak lagi gw dimana?")
                    else:
                        await ctx.bot_send("Sorry cuy mungkin atk itu udah di pake atau gak available")
                else:
                    await ctx.bot_say("Yo ramein mulai game **BADUTCUY** dengan cara ketik `cuy/. start`")
    async def stop(ctx):
      if ctx.user_message.startswith('cuy/. stop'):    
        global end
        global canvas
        global count
        print('stop the game')
        await ctx.bot_say(':rage: PAYAH! Permainan **badutcuy dihentikan** :rage:')
        end = True
        canvas = []
        count = 0

def addPoint(person):
  print('id => ', person)
  win = str(person)
  winner = f'<@{win}>'
  cell = api.reputation_find(winner)
  if cell == None:
    api.reputation_insert(winner)
  api.reputation_update(winner, 1)      
      
def winnerCondition(pos):
    global end
    global num
    if pos == num:
        end = True