import discord

def embeed(title, desc, arr = {}):
    embed = discord.Embed(title=title, description=desc, color=discord.Color.random())
    
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