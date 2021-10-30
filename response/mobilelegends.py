import api.data_mobilelegends as api
import helper.constants as c

class Mobile_Legends(c.cog):
    def __init__(self, client):
        self.client = client
        
    @c.cmd.command(name="ml", aliases=['mlredeem'])
    async def redeem(client, ctx):
        user_message = ctx.message.content
        bot_send = ctx.message.reply
        if any(x in user_message for x in c.request_mobilelegends):
            data = user_message.split(" ", 3)

            if len(data) == 1:
                await bot_send(":clap: ketik game id mobile legends anda jika ingin mendapatkan verifikasi code :clap: \n jika sudah mendapatkan verifikasi code, silahkan ketik kode redeem anda berdampingan verifikasi kode: \n `cuy/ml [game id] [verifikasi kode] [kode redeem]`")
            elif len(data) == 2:
                game_id = data[1]
                request_verifikasi = api.send_code(game_id)
                await bot_send(request_verifikasi)
            elif len(data) == 4:
                game_id = data[1]
                verifikasi = data[2]
                redeem = data[3]
                request_redeem = api.send_redeem(game_id, verifikasi, redeem)
                await bot_send(request_redeem)
            else:
                await bot_send('command\ncuy/ml [gameid] [verifikasi kode] [kode reedem]')

def setup(client):
    client.add_cog(Mobile_Legends(client))