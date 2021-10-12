import discord
from discord.ext import commands
import random


player1 = ""
player2 = ""
turn = ""
end = True

canvas = []
client = commands.Bot(command_prefix='.')

winnerCondition = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]

@client.command()
async def ucingkup(ctx, p1: discord.Member, p2: discord.Member):
    global player1, player2, turn, end
    global count

    if end:
        global canvas
        canvas = [":white_large_square:", ":white_large_square:", ":white_large_square:", 
                  ":white_large_square:", ":white_large_square:", ":white_large_square:",
                  ":white_large_square:",":white_large_square:", ":white_large_square:"]
        turn = ""
        end = False
        count = 0

        player1 = p1
        player2 = p2

            # print canvas
        line = ""
        for x in range(len(canvas)):
            if x == 2 or x == 5 or x == 8:
                line += " " + canvas[x]
                await ctx.send(line)
            else:
                line += " " + canvas[x]

        number = random.randint(1, 2)
        if number == 1:
            turn = player1
            await ctx.send("Giliran " + str(player1.id) + " bermain.")
        elif number == 2:
            turn = player2
            await ctx.send("Giliran " + str(player2.id) + " bermain.")
    else:
        await ctx.send("Cuy lesgo main UCING KUP!!!")

@client.command()
async def map(ctx, pos: int):
    global turn, player1, player2, canvas, count

    if not end:
        mark = ""
        if turn == ctx.author:
            if turn == player1:
                mark = ":regional_indicator_x:"
            elif turn == player2:
                mark = ":o2:"
                if 0 < pos < 10 and canvas[pos - 1] == ":white_large_square:":
                    canvas[pos - 1] = mark
                    count += 1

                    # print canvas
                    line = ""
                    for x in range(len(canvas)):
                        if x == 2 or x == 5 or x == 8:
                            line += " " + canvas[x]
                            await ctx.send(line)
                        else:
                            line += " " + canvas[x]

                    theWinner(winnerCondition, mark)
                    if end:
                        await ctx.send(mark + " menang!")
                    elif count >= 9:
                        await ctx.send("hmmmm....")

                    # turning player
                    if turn == player1:
                        turn = player2
                    elif turn == player2:
                        turn = player1

                else:
                    await ctx.send("Hanya pilih angka dari 1 - 9 saja")
        else:
            await ctx.send("belum giliran kamu cuy, kalem!")
    else:
        await ctx.send("silahkan mulai game dengan cara cuy/main ucingkup")


def theWinner(winnerCondition, mark):
    global end
    for condition in winnerCondition:
        if canvas[condition[0]] == mark and canvas[condition[1]] == mark and canvas[condition[2]] == mark:
            end = True

@client.command()
async def kupError(ctx, err):
    if isinstance(err, commands.MissingRequiredArgument):
        await ctx.send("silahkan mention 2 orang untuk bermain game")
    elif isinstance(err, commands.BadArgument):
        await ctx.send("silahkan mention seseorang di server ini menggunakan user id, misal: <@123j123jh123>")

@client.command()
async def mapError(ctx, err):
    if isinstance(err, commands.MissingRequiredArgument):
        await ctx.send("silahkan pilih posisi untuk ditempati")
    elif isinstance(err, commands.BadArgument):
        await ctx.send("upss....kalem gue error")
