from googleapiclient.discovery import build
from config import GOOGLE_KEY


def search_google():
    res = build('SearchEngine', developerKey=GOOGLE_KEY).cse()
    return res.list()


print(search_google())
