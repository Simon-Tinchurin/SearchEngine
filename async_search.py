import asyncio
import datetime
import aiohttp
from config import *

# sync main 15.832384
# async 8.49841

news = []


# def process_data(data):
#     patterns = {'rapid_search': ['title', 'url', 'description', 'datePublished'],
#                 'bing_search': ['name', 'url', 'description', 'datePublished'],
#                 'serpstack_search': ['title', 'url'],
#                 }
#     for item in data:
#         news_dict = {'title': item['title'],
#                      'url': item['url'],
#                      'description': [item['description'] if 'description' in item.keys() else ''],
#                      'date': [item['datePublished'] if 'datePublished' in item.keys() else '']}
#         news.append(news_dict)
#     return news


# https://rapidapi.com/contextualwebsearch/api/web-search/


def show_results(NEWS):
    for item in NEWS:
        print('--------------------')
        print(item['title'])
        print(item['url'])
        print(item['description'])
        print(item['date'])
        print(item['resource'])
        print()


async def rapid_search(session, QUERY):
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
                         'date': item['datePublished'],
                         'resource': 'Rapid'
                         }
            news.append(news_dict)
    return news


async def bing_search(session, QUERY):
    url = "https://bing-web-search1.p.rapidapi.com/search"
    querystring = {"q": f"{QUERY}", "freshness": "Day", "textFormat": "Raw",
                   "safeSearch": "Off", "mkt": "en-us"}
    async with session.get(url, headers=BING_HEADERS,
                                params=querystring) as response:
        result = await response.json()
        result = result['value']
        for item in result:
            news_dict = {'title': item['name'],
                         'url': item['url'],
                         'description': item['description'],
                         'date': item['datePublished'],
                         'resource': 'Bing'
                         }
            news.append(news_dict)
    return news


# https://serpstack.com/dashboard
async def serpstack_search(session, QUERY):
    url = f'http://api.serpstack.com/search?access_key={SERPSTACK_KEY}&query={QUERY}&num=10'
    async with session.get(url) as response:
        result = await response.json()
        result = result['organic_results']
        for item in result:
            news_dict = {'title': item['title'],
                         'url': item['url'],
                         'description': '',
                         'date': '',
                         'resource': 'Serpstack'
                         }
            news.append(news_dict)
        return news


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


if __name__ == '__main__':
    start_time = datetime.datetime.now()
    asyncio.run(main('Python'))
    show_results(news)
    print((datetime.datetime.now()-start_time).total_seconds())
