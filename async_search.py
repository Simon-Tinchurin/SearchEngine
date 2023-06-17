import asyncio
import datetime
import aiohttp
from config import *

# sync main 15.832384
# async 8.49841


def process_data(data):
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
async def rapid_search(session, QUERY):
    news = []
    url = "https://contextualwebsearch-websearch-v1.p.rapidapi.com/api/Search/WebSearchAPI"
    querystring = {"q": QUERY, "pageNumber": "1", "pageSize": "10", "autoCorrect": "true"}
    async with session.get(url, headers=RAPIDAPI_HEADERS,
                           params=querystring) as response:
        result = await response.json()
        result = result['value']
        for item in result:
            news_dict = {'title': item['title'],
                         'url': item['url'],
                         'description': item['description'],
                         'date': item['datePublished']}
            news.append(news_dict)
    print(news)


async def bing_search(session, QUERY):
    url = "https://bing-web-search1.p.rapidapi.com/search"
    querystring = {"q": f"{QUERY}", "freshness": "Day", "textFormat": "Raw",
                   "safeSearch": "Off", "mkt": "en-us"}
    async with session.get(url, headers=BING_HEADERS,
                                params=querystring) as response:
        result = await response.json()
        result = result['value']
        news = []
        for item in result:
            news_dict = {'title': item['name'],
                         'url': item['url'],
                         'description': item['description'],
                         'date': item['datePublished']}
            news.append(news_dict)
    print(news)


# https://serpstack.com/dashboard
async def serpstack_search(session, QUERY):
    url = f'http://api.serpstack.com/search?access_key={SERPSTACK_KEY}&query={QUERY}&num=10'
    async with session.get(url) as response:
        result = await response.json()
        result = result['organic_results']
        news = []
        for item in result:
            news_dict = {'title': item['title'],
                         'url': item['url'],
                         'description': '',
                         'date': '',
                         }
            news.append(news_dict)
        print(news)


async def main(QUERY):
    async with aiohttp.ClientSession() as session:
        tasks = []
        task1 = asyncio.ensure_future(rapid_search(session, QUERY))
        task2 = asyncio.ensure_future(serpstack_search(session, QUERY))
        task3 = asyncio.ensure_future(bing_search(session, QUERY))
        tasks.append(task1)
        tasks.append(task2)
        tasks.append(task3)
        await asyncio.gather(*tasks)

# @timer
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


if __name__ == '__main__':
    t0 = datetime.datetime.now()
    asyncio.run(main('Ukraine'))
    print((datetime.datetime.now()-t0).total_seconds())
