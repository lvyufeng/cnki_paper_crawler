import pymongo
import time

client = pymongo.MongoClient('202.202.5.140')
collection = client['cnki_papers']
db = collection['paper_detail']

while True:
    print(db.count())
    time.sleep(5)
