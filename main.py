from config.liveserver import liveserver
import os
import locale
import helper.constants as c

locale.setlocale(locale.LC_ALL, '')
liveserver()

plugins = next(os.walk("./response"), (None, None, []))[2] 

for plugin in plugins:
    c.client.load_extension(f'response.{plugin[:-3]}')
    print(f'{plugin} has been loaded')

# c.client.run(os.getenv('TOKEN'))
c.client.run('OTAwMzkxNjgwNzgyNTEyMTY5.YXApGQ.DqTU6ihxlEd9Mz9lQUSPRE0CGBo')