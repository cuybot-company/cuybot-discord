import requests
import json

def data_news():
    data_news =  requests.get('https://api-berita-indonesia.vercel.app/cnn/teknologi')
    datas = json.loads(data_news.text)
    news = datas['data']['posts']
    
    if len(news) > 0 :
        for data in news:
            title = data['title']
            result = beritas(title)
        return(result)
    else:
        return('saat ini tidak ada data berita')
    
def beritas(title):
    return(title)