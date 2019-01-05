import pymongo
from paper_list_parser import get_article_list
from paper_parser import get_article_detail
import time

years = [2018,2017,2016]

journals = ['JSJY','JSGG','WJFZ','JSJA','KXTS','SJSJ','RJXB','JFYZ','JSJF','JSJX','XXWX','JSJK']

article_list = []
client = pymongo.MongoClient('202.202.5.140')
collection = client['cnki_papers']
db = collection['paper_detail']

for year in years:
    for i in range(1,13):
        for pykm in journals:
            # time.sleep(1)
            article_list.extend(get_article_list(year,"%02d" % i
,pykm))

for i in article_list:
    time.sleep(1)
    paper = get_article_detail(i)
    db.insert_one(paper)