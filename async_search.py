import asyncio
import aiohttp
import requests
from functions import timer
from config import *


def process_data(data, func_name):
    patterns = {'rapid_search': ['title', 'url', 'description', 'datePublished'],
                'bing_search': ['name', 'url', 'description', 'datePublished'],
                'serpstack_search': ['title', 'url'],
                }
    news = []
    for item in data:
        news_dict = {'title': item['title'],
                     'url': item['url'],
                     'description': [item['description'] if 'description' in item.keys() else ''],
                     'date': [item['datePublished'] if 'datePublished' in item.keys() else '']}
        news.append(news_dict)
    return news


# https://rapidapi.com/contextualwebsearch/api/web-search/
@timer
def rapid_search(QUERY):
    url = "https://contextualwebsearch-websearch-v1.p.rapidapi.com/api/Search/WebSearchAPI"
    querystring = {"q": QUERY, "pageNumber": "1", "pageSize": "10", "autoCorrect": "true"}
    response = requests.get(url,
                            headers=RAPIDAPI_HEADERS,
                            params=querystring).json()['value']
    return process_data(data=response, func_name=rapid_search.__name__)


def bing_search(QUERY):
    url = "https://bing-web-search1.p.rapidapi.com/search"
    querystring = {"q": f"{QUERY}", "freshness": "Day", "textFormat": "Raw",
                   "safeSearch": "Off", "mkt": "en-us"}
    response = requests.get(url,
                            headers=BING_HEADERS,
                            params=querystring).json()['value']


# https://serpstack.com/dashboard
@timer
def serpstack_search(QUERY):
    url = f'http://api.serpstack.com/search?access_key={SERPSTACK_KEY}&query={QUERY}&num=10'
    response = requests.get(url).json()['organic_results']
    # return process_data(data=search_results)
    print(response)

serpstack_search('Python')

# async def main(QUERY):
#     async with aiohttp.ClientSession as session:
#         tasks = []
#         task1 = asyncio.ensure_future(rapid_search(session, QUERY))
#         task2 = asyncio.ensure_future(serpstack_search(session, QUERY))
#         tasks.append(task1)
#         tasks.append(task2)


# def main(QUERY):
#     res1 = rapid_search(QUERY)
#     print('----------------')
#     print(res1)
#     res2 = bing_search(QUERY)
#     print('----------------')
#     print(res2)
#     res3 = serpstack_search(QUERY)
#     print('----------------')
#     print(res3)
#
#
# if __name__ == '__main__':
#     main('Python')
