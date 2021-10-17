import random
import helper.tictactoe as ttt
from discord_components import DiscordComponents, Button, ButtonStyle

component = []
papan = []
giliran = ""
end = True
menang = True
seri = True
message = ""

class TicTacToeBot(object):
    def __init__(self, sender, client, user_message, bot_say, bot_send):
        self.sender = sender
        self.user_message = user_message
        self.bot_say = bot_say
        self.bot_send = bot_send
        self.client = client

        DiscordComponents(self.client)

    async def begin(self):
        if self.user_message.startswith("cuy/tic start"):
            global papan
            global giliran
            global end
            global message
            global menang
            global seri
            global component
            
            buttons = ['{}'.format(x) for x in range(1,10)]

            if end:
                end = False
                menang = False
                seri = False
                papan = ["bot", "player"]
                giliran = papan[random.randint(0,1)]

                component = [
                    [
                        Button(label="-", custom_id="1", disabled=False),
                        Button(label="-", custom_id="2", disabled=False),
                        Button(label="-", custom_id="3", disabled=False)
                    ],
                    [
                        Button(label="-", custom_id="4", disabled=False),
                        Button(label="-", custom_id="5", disabled=False),
                        Button(label="-", custom_id="6", disabled=False)
                    ],
                    [
                        Button(label="-", custom_id="7", disabled=False),
                        Button(label="-", custom_id="8", disabled=False),
                        Button(label="-", custom_id="9", disabled=False)
                    ]
                ]

                if giliran == "bot":
                    move = ttt.computerMove()+1
                    if move >= 1 and move <= 3:
                        component[0][move - 1] = Button(style=ButtonStyle.green, emoji=u"\u274C", disabled=True)
                    elif move >= 4 and move <= 6:
                        component[1][move - 4] = Button(style=ButtonStyle.green, emoji=u"\u274C", disabled=True)
                    elif move >= 7 and move <= 9:
                        component[2][move - 7] = Button(style=ButtonStyle.green, emoji=u"\u274C", disabled=True)
                    
                    giliran = "player"

                message = await self.bot_send(f"Game Tic Tac Toe started \n {giliran.capitalize()} Jalan", components=component)

                while True:

                    if end and menang:
                        await message.edit("Anjer Jago bener lu bro, sampe kalahin bot ini", components=[])
                        ttt.clearGame()
                    elif end and seri:
                        await message.edit("Masa seri ama bot :moyai: ", components=[])
                        ttt.clearGame()
                    elif end and not menang:
                        await message.edit("Masa kalah ama bot :moyai: ", components=[])
                        ttt.clearGame()
                    
                    interaction = await self.client.wait_for("button_click", check = lambda i: i.custom_id in buttons)
                    button_select = int(interaction.custom_id)

                    pesan_jalan = f'Bot lagi mikir'
                    await interaction.send(pesan_jalan)

                    if not ttt.getWins():

                        if giliran == "player":
                            if button_select >= 1 and button_select <= 3:
                                component[0][button_select - 1] = Button(style=ButtonStyle.green, emoji=u"\u2B55", custom_id=interaction.custom_id, disabled=True)
                                ttt.setPosition(button_select - 1)
                                ttt.playerMove()
                                giliran = "bot"

                            elif button_select >= 4 and button_select <= 6:
                                component[1][button_select - 4] = Button(style=ButtonStyle.green, emoji=u"\u2B55", custom_id=interaction.custom_id, disabled=True)
                                ttt.setPosition(button_select - 1)
                                ttt.playerMove()
                                giliran = "bot"

                            elif button_select >= 7 and button_select <= 9:
                                component[2][button_select - 7] = Button(style=ButtonStyle.green, emoji=u"\u2B55", custom_id=interaction.custom_id, disabled=True)
                                ttt.setPosition(button_select - 1)
                                ttt.playerMove()
                                giliran = "bot"

                        if giliran == "bot":
                            move = ttt.computerMove()+1
                            if move >= 1 and move <= 3:
                                component[0][move - 1] = Button(style=ButtonStyle.green, emoji=u"\u274C", disabled=True)
                                giliran = "player"
                            elif move >= 4 and move <= 6:
                                component[1][move - 4] = Button(style=ButtonStyle.green, emoji=u"\u274C", disabled=True)
                                giliran = "player"
                            elif move >= 7 and move <= 9:
                                component[2][move - 7] = Button(style=ButtonStyle.green, emoji=u"\u274C", disabled=True)
                                giliran = "player"

                    if ttt.getWins():
                        if ttt.getWins() == "bot":
                            end = True
                        elif ttt.getWins() == "player":
                            end = True
                            menang = True
                        else:
                            end = True
                            seri = True

                    
                    await message.edit("Jalan Lagi bro", components=component)

            else:
                await self.bot_send(":raised_hand: bentar tunggu game selesai dulu cuy! chill...:raised_hand:")

        elif self.user_message.startswith("cuy/tic stop"):
            await message.edit(':rage: PAYAH! Permainan **TicTacToe dihentikan** :rage: \n kena mental boss?', components=[])
            ttt.clearGame()
            end = True
            