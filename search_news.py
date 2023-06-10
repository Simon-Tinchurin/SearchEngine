import requests
from config import *
from functions import timer

functions_work_time = {}


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


search_nyt('Ukraine')
print(functions_work_time)