import helper.constants as c
import helper.discord as d
import os
import subprocess
import json

class Server(c.cog):
    def __init__(self, client):
        self.server = client
        
    @c.cmd.command(name="server")
    async def control(self, ctx):
        user_message = ctx.message.content
        id_user = ctx.message.author.id
        bot_send = ctx.message.reply
        # ID_ADMIN = [12345678910]
        data = user_message.split(" ", 1)
        title = "Server Info"   
        # if not self.id_user in id_admin:
        
        if not id_user in json.loads(os.getenv('ID_ADMIN')):
            embed = d.embeed(title, ":warning: Anda tidak berhak memakai fitur ini, hanya boleh para admin saja :warning:")
            return await bot_send(embed=embed)

        if any(x in data for x in c.request_update):  
            output = subprocess.check_output('git pull origin dev', shell=True)
            if not b"Already up to date" in output:
                embed = d.embeed(title, ":clap: Server up to date :clap:")
                return await bot_send(embed=embed)
                
            embed = d.embeed(title, ":clap: Server Already up to date :clap:")
            return await bot_send(embed=embed)

        if any(x in data for x in c.request_disconnect):
            embed = d.embeed(title, "Server akan dimatikan")
            await bot_send(embed=embed)
            exit()
            
        embed = d.embeed(title, "Untuk update server ketik `cuy/server up` \n untuk mematikan server ketik `cuy/server dc`")
        await bot_send(embed=embed)

def setup(client):
    client.add_cog(Server(client))