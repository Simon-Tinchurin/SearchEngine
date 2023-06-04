import requests
from config import CUSTOM_API_KEY

# https://rapidapi.com/contextualwebsearch/api/web-search/

url = "https://contextualwebsearch-websearch-v1.p.rapidapi.com/api/Search/WebSearchAPI"

querystring = {"q": "taylor swift", "pageNumber": "1", "pageSize": "10", "autoCorrect": "true"}

headers = {
    "X-RapidAPI-Key": CUSTOM_API_KEY,
    "X-RapidAPI-Host": "contextualwebsearch-websearch-v1.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())
