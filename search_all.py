import requests
from functions import timer
from config import RAPIDAPI_HEADERS, SERPSTACK_KEY


def process_data(data):
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
    return process_data(data=response)


# https://serpstack.com/dashboard
@timer
def serpstack_search(QUERY):
    url = f'http://api.serpstack.com/search?access_key={SERPSTACK_KEY}&query={QUERY}&num=10'
    response = requests.get(url).json()
    search_results = response['organic_results']
    return process_data(data=search_results)


def main(QUERY):
    total_result = rapid_search(QUERY) + serpstack_search(QUERY)
    print(total_result)


main(QUERY='Ukraine')
