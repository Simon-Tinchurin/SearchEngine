import requests
from config import *
from functions import timer


# https://developer.nytimes.com/docs/articlesearch-product/1/overview
@timer
def search_nyt(QUERY):
    nyt_url = f'https://api.nytimes.com/svc/search/v2/articlesearch.json?q={QUERY}&api-key={NYT_API_KEY}'
    try:
        response = requests.get(url=nyt_url).json()['response']['docs']
        headlines = []
        for i in range(len(response)):
            print('----------------------------------')
            print(response[i]['headline']['main'])
            print(response[i]['pub_date'])
            print(response[i]['web_url'])
            print('')
    except Exception as ex:
        print('Error in search: ', ex)
        # titles.append(response[i]['abstract'])
    # print(response)


# search_nyt('metallica')

# https://open-platform.theguardian.com/documentation/
@timer
def search_the_guardian(QUERY):
    url = f'https://content.guardianapis.com/search?q={QUERY}&api-key={THE_GUARDIAN_KEY}'
    response = requests.get(url).json()['response']['results']
    for item in response:
        print(item['webTitle'])
        print(item['webUrl'])
        print(item['webPublicationDate'])
        print('-----------------------')
    # print(response)


search_the_guardian('metallica')