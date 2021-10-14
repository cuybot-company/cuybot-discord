import api.data_mobilelegends as api
import helper.constants as c

class Mobile_Legends(object):
    def __init__(self, user_message, bot_send):
        self.user_message = user_message
        self.bot_send = bot_send
    
    async def redeem(self):
        if any(x in self.user_message for x in c.request_mobilelegends):
            data = self.user_message.split(" ", 3)

            if len(data) == 1:
                await self.bot_send(":clap: ketik game id mobile legends anda jika ingin mendapatkan verifikasi code :clap: \n jika sudah mendapatkan verifikasi code, silahkan ketik kode redeem anda berdampingan verifikasi kode: \n `cuy/ml [game id] [verifikasi kode] [kode redeem]`")
            elif len(data) == 2:
                game_id = data[1]
                request_verifikasi = api.send_code(game_id)
                await self.bot_send(request_verifikasi)
            elif len(data) == 4:
                game_id = data[1]
                verifikasi = data[2]
                redeem = data[3]
                request_redeem = api.send_redeem(game_id, verifikasi, redeem)
                await self.bot_send(request_redeem)
            else:
                await self.bot_send('command\ncuy/ml [gameid] [verifikasi kode] [kode reedem]')