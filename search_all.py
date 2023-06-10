import requests
from config import RAPIDAPI_HEADERS, SERPSTACK_KEY


# https://rapidapi.com/contextualwebsearch/api/web-search/
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


# https://serpstack.com/dashboard
def serpstack_search(QUERY):
    url = f'http://api.serpstack.com/search?access_key={SERPSTACK_KEY}&query={QUERY}'
    response = requests.get(url).json()
    search_results = response['organic_results']
    print(search_results)