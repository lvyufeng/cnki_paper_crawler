import jieba
import pymongo

def stop_words_list():
    stop_words = [line.strip() for line in open('stopword.txt','r+',encoding='UTF-8').readlines()]

    return stop_words


def cut_words(sentence):
    sentence_cut = jieba.cut(sentence.strip())
    stop_words = stop_words_list()

    output = ''
    for word in sentence_cut:
        if word not in stop_words:
            output += word
            output += ' '
    return output

output_filename = 'abstracts.txt'
outputs = open(output_filename,'w+',encoding='UTF-8')

client = pymongo.MongoClient('202.202.5.140')
collection = client['cnki_papers']
db = collection['paper_detail']

for i in db.find():

    try:
        line = cut_words(i['a_abstract'].replace('\n摘    要：\n',''))
        outputs.write(i['filename']+ '\t' + i['top-title'].strip() + '\t' + line + '\n')
    except Exception as e:
        print(i['filename'])
        db.remove(i)
outputs.close()


