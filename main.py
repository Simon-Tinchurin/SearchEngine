import requests
import pprint
from config import *


def search_nyt(QUERY):
    nyt_url = f'https://api.nytimes.com/svc/search/v2/articlesearch.json?q={QUERY}&api-key={NYT_API_KEY}&page=1'
    response = requests.get(url=nyt_url).json()['response']['docs']
    headlines = []
    for i in range(len(response)):
        print('----------------------------------')
        print(response[i]['headline']['main'])
        print(response[i]['pub_date'])
        print(response[i]['web_url'])
        print('')
        # titles.append(response[i]['abstract'])
    # print(response)


search_nyt('Ukraine')