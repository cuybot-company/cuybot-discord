import requests
import json
import random

def data_news(param):
    data_param = param.split()[1]
    data_news =  requests.get('https://api-berita-indonesia.vercel.app/cnn/' + data_param)
    datas = json.loads(data_news.text)
    news = datas['data']
    
    if news is None :
        return('saat ini kategori berita ' +data_param+' tidak ada\n\nmasukkan kategori berita, contoh: \n`/berita nasional`\n`/berita internasional`\n`/berita ekonomi`\n`/berita olahraga`\n`/berita teknologi`\n`/berita hiburan`')
    else:
        numbers = list(range(len(news['posts'])))
        random.shuffle(numbers)
        x = random.choice(numbers)
        title = news['posts'][x]['title']
        link = news['posts'][x]['link']
        date = news['posts'][x]['pubDate']
        description = news['posts'][x]['description']
        return('Berita '+data_param+' hari ini: \n' + title + '\n\n' + link + '\n' + date + '\n' + description + '\n\n')
    