import requests
from bs4 import BeautifulSoup
# import pymongo

def generate_issue_url(year,issue,pykm):
    url = 'http://navi.cnki.net/knavi/JournalDetail/GetArticleList?year={}&issue={}&pykm={}'.format(year,issue,pykm)

    return url

def get_article_list(year,issue,pykm):
    url = generate_issue_url(year,issue,pykm)
    wb = requests.get(url)
    soup = BeautifulSoup(wb.text,'lxml')
    article_list = []
    for i in soup.select('body > dd'):
        if 'HTML阅读' in str(i) :
            article_list.append(i.select('span.name > a')[0].get('href').split('&')[2])

    return article_list

# list = get_article_list(2018,12,'JSJX')

# pass

