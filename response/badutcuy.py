import random
import api.data_user_request as api
import helper.constants as c
from discord_components import DiscordComponents, Button, ButtonStyle

#initial game badut
end = True
turn = 0
message = ""
component = []
badut = 0
ketemu = True

class BadutStart(c.cog):
    def __init__(self, client):
        self.client = client

        DiscordComponents(self.client)
    @c.cmd.command(name="badut")
    async def begin(self, ctx):
        user_message = ctx.message.content
        bot_say = ctx.message.channel.send
        bot_send = ctx.message.reply
        if 'start' in user_message:
            global end
            global turn
            global message
            global component
            global badut
            global ketemu

            buttons = ['{}'.format(x) for x in range(1,10)]
            
            if end:
                end = False
                ketemu = False
                turn = 4
                message = ""
                badut = random.randint(1, 9)

                component = [
                    [Button(label="-", custom_id="1"),Button(label="-", custom_id="2"),Button(label="-", custom_id="3")],
                    [Button(label="-", custom_id="4"),Button(label="-", custom_id="5"),Button(label="-", custom_id="6")],
                    [Button(label="-", custom_id="7"),Button(label="-", custom_id="8"),Button(label="-", custom_id="9")]
                ]

                message = await bot_say(f":clap: Perkenalkan gue **BADUTCUY** :clap:\nCoba tebak gw ngumpet dimana?\n`pilih salah satu button`",components=component)
                
                while True:
                    if turn == 0 and ketemu == False:
                        end = True
                        await message.edit(":person_juggling: **Game selesai** :person_juggling:\ngak ada yang menang cuy!\nkesempatan cuma 4x tebak dalam 1 permainan, AH elah gimanasiiiii! :rage:\n\nYo ramein mulai game **BADUTCUY** dengan cara ketik `cuy/. start`", components=[])
                    elif end and ketemu:
                        await message.edit("ANJIM KETAUAN! *badutcuy* ada di posisi **" + str(badut)  + "**" + "\n\n:first_place: CONGRATS :first_place:\nSebagai hadiahnya cuybot ngasih lu **1 point** reputasi di *cuyhub community* :star_struck:\ncek total point lu dengan cara `cuy/rep @mention`\n\nmain lagi yu? ketik `cuy/. start` sekarang! berani?", components=[])
                            
                    interaction = await self.client.wait_for("button_click", check = lambda i: i.custom_id in buttons)
                    button_select = int(interaction.custom_id)

                    pesan_jalan = f'Anda tinggal {turn-1} jalan lagi' if turn-1 > 0 else "Woops, kesempatan jalan sudah tidak ada lagi"
                    await interaction.send(pesan_jalan)

                    if button_select == badut:
                        if button_select >= 1 and button_select <= 3:
                            component[0][button_select - 1] = Button(style=ButtonStyle.green, emoji=u"\U0001F921", custom_id=interaction.custom_id, disabled=True)
                            end = True
                            ketemu = True
                            addPoint(interaction.user.id)
                        elif button_select >= 4 and button_select <= 6:
                            component[1][button_select - 4] = Button(style=ButtonStyle.green, emoji=u"\U0001F921", custom_id=interaction.custom_id, disabled=True)
                            end = True
                            ketemu = True
                            addPoint(interaction.user.id)
                        elif button_select >= 7 and button_select <= 9:
                            component[2][button_select - 7] = Button(style=ButtonStyle.green, emoji=u"\U0001F921", custom_id=interaction.custom_id, disabled=True)
                            end = True
                            ketemu = True
                            addPoint(interaction.user.id)
                    else:
                        if button_select >= 1 and button_select <= 3:
                            component[0][button_select - 1] = Button(style=ButtonStyle.red, emoji=u"\U0001F4A9", custom_id=interaction.custom_id, disabled=True)
                        elif button_select >= 4 and button_select <= 6:
                            component[1][button_select - 4] = Button(style=ButtonStyle.red, emoji=u"\U0001F4A9", custom_id=interaction.custom_id, disabled=True)
                        elif button_select >= 7 and button_select <= 9:
                            component[2][button_select - 7] = Button(style=ButtonStyle.red, emoji=u"\U0001F4A9", custom_id=interaction.custom_id, disabled=True)

                    turn -= 1
                    await message.edit(":poop: Salah yeeee... :poop:\nAda yang bisa nebak lagi gw dimana?", components=component)
            else:
                await bot_send(":raised_hand: bentar tunggu game selesai dulu cuy! chill...:raised_hand:")

        elif 'stop' in user_message:
            await message.edit(':rage: PAYAH! Permainan **badutcuy dihentikan** :rage:', components=[])
            end = True

def addPoint(person):
    print('id => ', person)
    win = str(person)
    winner = f'<@{win}>'
    cell = api.reputation_find(winner)
    if cell == None:
        api.reputation_insert(winner)
    api.reputation_update(winner, 1)

def setup(client):
    client.add_cog(BadutStart(client))