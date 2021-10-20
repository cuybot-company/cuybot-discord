import helper.constants as c
import api.data_user_request as api
import random

class Gacha(c.cog):
    def __init__(self, client):
        self.client = client
    
    @c.cmd.command(name="reward")
    async def booking_angka(self, ctx):
        sender = ctx.message.author
        bot_send = ctx.message.reply
        user_message = ctx.message.content
        random_angka = random.randint(1, 200)
        message = user_message.split(" ", 1)
        member_id = sender.id
        
        if "semifinal" in message:
            await bot_send("semi final")
        else:
            insertNumberGacha(member_id, random_angka)
            await bot_send(f"No Toggel Anda adalah: {random_angka}")
    
    @c.cmd.command(name="gacha")
    async def pilih_pemenang(self, ctx):
        sender = ctx.message.author
        member_id = sender.id
        bot_send = ctx.message.reply
        user_message = ctx.message.content
        random_angka = random.randint(1, 200)

        if "gacha" in user_message:
            if checkNumber(member_id, random_angka):
                await bot_send("yeay selamat anda menang")
            else:
                await bot_send('Ooops, Anda Kurang Beruntung, silahkan coba lagi')


def setup(client):
    client.add_cog(Gacha(client))

def insertNumberGacha(person, number):
    person = f'{str(person)}'
    api.gacha_insert(person, number)

def checkNumber(person, number):
    person = f'{str(person)}'
    number = f'{str(number)}'

    return api.gacha_tebak(person, number)