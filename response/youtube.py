import helper.constants as c
import urllib.parse, re, urllib.request
import requests

class Youtube(c.cog):
    def __init__(self, client):
        self.client = client
    @c.cmd.command(name="youtube")
    async def youtube(self, ctx):
        author = ctx.message.author
        bot_send = ctx.message.reply
        user_message = ctx.message.content

        search = user_message.split(" ", 1)
        
        search_query = urllib.parse.urlencode({
            'search_query': search[1]
        })
        
        content = requests.get(
            'https://youtube.com/result?' + search_query
        )
        
        result = re.findall('href=\"\\/watch\\?v=(.{11})', content.text)
        await bot_send("https://youtube.com/watch?v=" + result[0])

def setup(client):
    client.add_cog(Youtube(client))

# run oy ulang coba
# get apaan anjer ini