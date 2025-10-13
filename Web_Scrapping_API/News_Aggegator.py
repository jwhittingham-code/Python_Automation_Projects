import requests

api_key = "-"


param = {
    'apiKey': api_key,
    'country':'us',
    #note: there appears to not be anything coming from au, so using us instead
    'category': 'technology'

}

response = requests.get('https://newsapi.org/v2/top-headlines?',param)
collection = response.json()
articles = list()
for file in collection["articles"]:
    article = {}
    article["title"] = file['title']
    article["blurb"] = file['description']
    article["author"] = file['author']
    article["link"]= file['url']
    articles.append(article)
    

for i in range(5):
    article = articles[i]
    print(article['title'].upper())
    print("By: ", article['author'])
    print(article['blurb'])
    print("")
    print('Link: ', article['link'])
    print("")
    print('--------------------------------------------------------------------------------------')
    print("")