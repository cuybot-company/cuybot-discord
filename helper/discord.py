import discord
import datetime

def embeed(title, desc, color="", arr = {}):
    if color == "":
        color = discord.Color.random()

    embed = discord.Embed(title=title, description=desc, color=color, timestamp=datetime.datetime.utcnow())

    if len(arr) > 0:

        if "footer" in arr:
            if not "icon" in arr["footer"]:
                arr["footer"]["icon"] = ""

            embed.set_footer(text=arr["footer"]["text"], icon_url=arr["footer"]["icon"])
        
        if "image" in arr:
            embed.set_image(url=arr["image"])

        if "thumbnail" in arr:
            embed.set_thumbnail(url=arr["thumbnail"])
        
        if "author" in arr:
            if not "url" in arr["author"]:
                arr["author"]["url"] = ""

            if not "icon" in arr["author"]:
                arr["author"]["icon"] = ""

            embed.set_author(name=arr["author"]["name"], url=arr["author"]["url"], icon_url=arr["author"]["icon"])
        
        if "field" in arr:
            for i in range(0, len(arr["field"])):

                if not "inline" in arr["field"][i]:
                    arr["field"][i]["inline"] = False

                embed.add_field(name=arr["field"][i]["name"], value=arr["field"][i]["value"], inline=arr["field"][i]["inline"])

    return embed


def embeed_help(color="", arr = {}):
    if color == "":
        color = discord.Color.random()

    embed = discord.Embed(title=":pencil: INFO TENTANG COMMAND :pencil:", description=f'```{arr["command"]}```', color=color, timestamp=datetime.datetime.utcnow())

    if len(arr) > 0:
        embed.add_field(name="**Description**", value=f'```{arr["desc"].capitalize()}```', inline=False)
        embed.add_field(name="**Usage**", value=f'```{arr["usage"]}```', inline=False)
        embed.add_field(name="**Aliases**", value=f'```{", ".join(arr["alias"])}```', inline=True)
        embed.add_field(name="**Cooldown**", value=f'```{arr["cooldown"]} seconds```', inline=True)
    
    # embed.set_footer(text="Anda juga dapat menyebutkan bot (dengan @) untuk peganti prefix command.")
    
    return embed