import requests
import json

def data_news(param):
    data_news =  requests.get('https://api-berita-indonesia.vercel.app/cnn/' + param)
    datas = json.loads(data_news.text)
    news = datas['data']
    
    if len(news) > 0 :
        for data in news:
            title = data['posts']['title']
            link = data['posts']['link']
            date = data['posts']['pubDate']
            description = data['posts']['description']
            return('Berita '+param+'hari ini: \n' + title + '\n\n' + link + '\n' + date + '\n' + description + '\n\n')
    else:
        return('saat ini tidak ada data berita')