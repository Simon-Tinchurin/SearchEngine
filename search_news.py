import requests
from functools import wraps
import datetime
from config import *

functions_work_time = {}


def timer(func):
    @wraps(func)
    def decorator(*args, **kwargs):
        def wrapper(*args, **kwargs):
            start_time = datetime.datetime.now()
            result = func(*args, **kwargs)
            end_time = datetime.datetime.now()
            delta = (end_time - start_time).total_seconds()
            functions_work_time[func.__name__] = delta
            return result
        return wrapper
    return decorator(func)


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