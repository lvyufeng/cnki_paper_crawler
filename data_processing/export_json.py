import pymongo
import json

client = pymongo.MongoClient('202.202.5.140')
collection = client['cnki_papers']
db = collection['paper_detail']

paper_clusters = {str(i):[] for i in range(0,10)}

with open('cluster.txt','r+',encoding='UTF-8') as f:
    for i in f.readlines():
        line = i.strip().split('\t')
        paper = db.find({'filename':line[0]})[0]

        abstract = paper['a_abstract'].replace('\n摘    要：\n','').strip()
        if '。' in abstract:
            abstract_cut = abstract.split('。')
        else:
            abstract_cut = abstract.split('.')

        abstract_cut.remove('') if '' in abstract_cut else None
        for index,sentence in enumerate(abstract_cut):
            data = {
                'filename':line[0],
                'line_num':index,
                'text':sentence
            }

            paper_clusters[line[-1]].append(data)
f.close()

for key in paper_clusters.keys():
    paper_cluster = paper_clusters[key]
    with open('export_data_{}.json'.format(key),'w+',encoding='UTF-8') as f:
        for i in paper_cluster:
            json_str = json.dumps(i,ensure_ascii=False)
            f.write(json_str + '\n')
    f.close()