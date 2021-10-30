import random
import helper.tictactoe as ttt
from discord_components import DiscordComponents, Button, ButtonStyle
import helper.constants as c
import helper.command_help as cmd
from discord.ext import commands

command = next(filter(lambda x: x['name'] == "tictactoe", cmd.list_help_cmd))

class TicTacToeBot(c.cog):
    def __init__(self, client):
        self.client = client
        self.component = []
        self.giliran = ""
        self.end = True
        self.menang = True
        self.seri = True
        self.message = ''
        self.papan = None
        DiscordComponents(self.client)

    @c.cmd.command(aliases=command["alias"])
    @commands.cooldown(1, command["cooldown"], commands.BucketType.user)
    async def begin(self, ctx):

        user_message = ctx.message.content
        bot_send = ctx.message.reply

        if 'start' in user_message:
            buttons = ['{}'.format(x) for x in range(1,10)]

            if self.end:
                self.end = False
                self.menang = False
                self.seri = False
                self.papan = ["bot", "player"]
                self.giliran = self.papan[random.randint(0,1)]

                self.component = [
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

                if self.giliran == "bot":
                    move = ttt.computerMove()+1
                    if move >= 1 and move <= 3:
                        self.component[0][move - 1] = Button(style=ButtonStyle.green, emoji=u"\u274C", disabled=True)
                    elif move >= 4 and move <= 6:
                        self.component[1][move - 4] = Button(style=ButtonStyle.green, emoji=u"\u274C", disabled=True)
                    elif move >= 7 and move <= 9:
                        self.component[2][move - 7] = Button(style=ButtonStyle.green, emoji=u"\u274C", disabled=True)
                    
                    self.giliran = "player"

                self.message = await bot_send(f"Game Tic Tac Toe started \n {self.giliran.capitalize()} Jalan", components=self.component)

                while True:

                    if self.end and self.menang:
                        await self.message.edit("Anjer Jago bener lu bro, sampe kalahin bot ini", components=[])
                        ttt.clearGame()
                    elif self.end and self.seri:
                        await self.message.edit("Masa seri ama bot :moyai: ", components=[])
                        ttt.clearGame()
                    elif self.end and not self.menang:
                        await self.message.edit("Masa kalah ama bot :moyai: ", components=[])
                        ttt.clearGame()
                    
                    interaction = await self.client.wait_for("button_click", check = lambda i: i.custom_id in buttons)
                    button_select = int(interaction.custom_id)

                    pesan_jalan = f'Bot lagi mikir'
                    await interaction.send(pesan_jalan)

                    if not ttt.getWins():

                        if self.giliran == "player":
                            if button_select >= 1 and button_select <= 3:
                                self.component[0][button_select - 1] = Button(style=ButtonStyle.green, emoji=u"\u2B55", custom_id=interaction.custom_id, disabled=True)
                                ttt.setPosition(button_select - 1)
                                ttt.playerMove()
                                self.giliran = "bot"

                            elif button_select >= 4 and button_select <= 6:
                                self.component[1][button_select - 4] = Button(style=ButtonStyle.green, emoji=u"\u2B55", custom_id=interaction.custom_id, disabled=True)
                                ttt.setPosition(button_select - 1)
                                ttt.playerMove()
                                self.giliran = "bot"

                            elif button_select >= 7 and button_select <= 9:
                                self.component[2][button_select - 7] = Button(style=ButtonStyle.green, emoji=u"\u2B55", custom_id=interaction.custom_id, disabled=True)
                                ttt.setPosition(button_select - 1)
                                ttt.playerMove()
                                self.giliran = "bot"

                        if self.giliran == "bot":
                            move = ttt.computerMove()+1
                            if move >= 1 and move <= 3:
                                self.component[0][move - 1] = Button(style=ButtonStyle.green, emoji=u"\u274C", disabled=True)
                                self.giliran = "player"
                            elif move >= 4 and move <= 6:
                                self.component[1][move - 4] = Button(style=ButtonStyle.green, emoji=u"\u274C", disabled=True)
                                self.giliran = "player"
                            elif move >= 7 and move <= 9:
                                self.component[2][move - 7] = Button(style=ButtonStyle.green, emoji=u"\u274C", disabled=True)
                                self.giliran = "player"

                    if ttt.getWins():
                        if ttt.getWins() == "bot":
                            self.end = True
                        elif ttt.getWins() == "player":
                            self.end = True
                            self.menang = True
                        else:
                            self.end = True
                            self.seri = True

                    
                    await self.message.edit("Jalan Lagi bro", components=self.component)

            else:
                await bot_send(":raised_hand: bentar tunggu game selesai dulu cuy! chill...:raised_hand:")

        elif 'stop' in user_message:
            await self.message.edit(':rage: PAYAH! Permainan **TicTacToe dihentikan** :rage: \n kena mental boss?', components=[])
            ttt.clearGame()
            self.end = True

def setup(client):
    client.add_cog(TicTacToeBot(client))
