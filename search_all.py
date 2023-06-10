import requests
from config import RAPIDAPI_HEADERS


def rapid_search(QUERY):
    url = "https://contextualwebsearch-websearch-v1.p.rapidapi.com/api/Search/WebSearchAPI"
    querystring = {"q": QUERY, "pageNumber": "1", "pageSize": "10", "autoCorrect": "true"}
    response = requests.get(url, headers=RAPIDAPI_HEADERS, params=querystring)
    # print(response.json()['value'])
    for item in response.json()['value']:
        print(item['title'])
        print(item['url'])
        print(item['description'])
        print(item['datePublished'])


rapid_search(QUERY='metallica')