import helper.constants as c
import helper.discord as d
import os
import subprocess
import json

class Server(object):
    def __init__(self, sender, server, user_message, bot_send):
        self.id_user = sender.id
        self.server = server
        self.user_message = user_message
        self.bot_send = bot_send
    async def control(self):
        # ID_ADMIN = [12345678910]
        if self.user_message.startswith('cuy/server'):
            data = self.user_message.split(" ", 1)
            title = "Server Info"   
            # if not self.id_user in id_admin:
            
            if not self.id_user in json.loads(os.getenv('ID_ADMIN')):
                embed = d.embeed(title, ":warning: Anda tidak berhak memakai fitur ini, hanya boleh para admin saja :warning:")
                return await self.bot_send(embed=embed)

            if any(x in data for x in c.request_update):  
                output = subprocess.check_output('git pull origin dev', shell=True)
                if not b"Already up to date" in output:
                    embed = d.embeed(title, ":clap: Server up to date :clap:")
                    return await self.bot_send(embed=embed)
                    
                embed = d.embeed(title, ":clap: Server Already up to date :clap:")
                return await self.bot_send(embed=embed)

            if any(x in data for x in c.request_disconnect):
                embed = d.embeed(title, "Server akan dimatikan")
                await self.bot_send(embed=embed)
                exit()
                
            embed = d.embeed(title, "Untuk update server ketik `cuy/server up` \n untuk mematikan server ketik `cuy/server dc`")
            await self.bot_send(embed=embed)