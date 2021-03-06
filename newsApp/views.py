from django.shortcuts import render
from newsapi import NewsApiClient

# Create your views here.
def index(request):
    newsApi = NewsApiClient(api_key = '4c305be601eb47288e73472fa8aaaf2b')
    headLines = newsApi.get_top_headlines(sources = 'ign')
    articles = headLines['articles']
    desc = []
    news = []
    img = []
    url = []

    for i in range(len(articles)):
        article = articles[i]
        desc.append(article['description'])
        news.append(article['title'])
        img.append(article['urlToImage'])
        url.append(article['url'])

    mylist = zip(news, desc, img, url)

    return render(request, "index.html", context = {'mylist' : mylist})