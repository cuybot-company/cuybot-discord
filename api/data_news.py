import requests
import json

def data_news():
    data_news =  requests.get('https://api-berita-indonesia.vercel.app/cnn/teknologi')
    datas = json.loads(data_news.text)
    news = datas['data']['posts']
    
    if len(news) > 0 :
        datas = []
        for data in news:
            title = data['title']
            link = data['link']
            date = data['pubDate']
            description = data['description']
            datas.append('Berita teknologi hari ini: \n' + title + '\n\n' + link + '\n' + date + '\n' + description + '\n\n')
        return(''.join(datas))
    else:
        return('saat ini tidak ada data berita')