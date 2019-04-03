import requests
import json
import xlwt

def get_projects(url,headers):

    wb = requests.get(url,headers=headers)
    data = json.loads(wb.text)

    ids = [i['id'] for i in data]

    return ids

def get_json(ids,headers):
    data = []
    for i in ids:
        url = 'http://202.202.5.140:8080/projects/{}/download_file?format=json'.format(i)
        wb = requests.get(url,headers=headers)
        data.extend(wb.content.decode('utf-8').split('\n'))

    return data

def classification(datas):
    classification = {}
    for i in datas:
        try:
            data = json.loads(i)
        except Exception as e:
            continue
        for j in data['entities']:
            # classification[j[2]] = [] if j[2] not in classification.keys() else classification[j[2]].append([data['text'],data['text'][j[0]:j[1]]])

            tag = [] if j[2] not in classification.keys() else classification[j[2]]
            tag.append([data['text'],data['text'][j[0]:j[1]]])
            classification[j[2]] = tag
    return classification

def relations(datas):
    relations = {}
    for i in datas:
        try:
            data = json.loads(i)
        except Exception as e:
            continue
        if len(data['entities']) > 1:
            # entities = [data['text'][j[0]:j[1]] for j in data['entities']]
            # classification[j[2]] = [] if j[2] not in classification.keys() else classification[j[2]].append([data['text'],data['text'][j[0]:j[1]]])
            entities = {j[2]:data['text'][j[0]:j[1]] for j in data['entities']}
            keys = sorted(entities)
            len_keys = len(keys)
            if len_keys == 1:
                key = keys[0]
                keys = [key for i in range(len(data['entities']))]

            tag = [] if '-'.join(keys) not in relations.keys() else relations['-'.join(keys)]
            rel = [data['text']]
            if len_keys == 1:
                rel.extend([data['text'][j[0]:j[1]] for j in data['entities']])
            else:
                rel.extend([entities[key] for key in keys])
            tag.append(rel)
            relations['-'.join(keys)] = tag
    return relations

headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8,en;q=0.7',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': '_ga=GA1.1.1529689878.1546591174; csrftoken=qeCXhK2gdurUFqhCEwjn3GP8RWlB9FqqDEZZDRYfBMkvFGMVHL2rWgibPP1vqcGq; sessionid=1epvlu9sfrntt9w4tk40yow0j2qnpj83; _gid=GA1.1.2057543101.1547411511',
        'Host': '202.202.5.140:8080',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.98 Chrome/71.0.3578.98 Safari/537.36'
    }

url = 'http://202.202.5.140:8080/api/projects/?format=json'
ids = get_projects(url,headers)
datas = get_json(ids,headers)
classification = classification(datas)
relations = relations(datas)

for key,value in classification.items():
    wb = xlwt.Workbook()
    ws = wb.add_sheet('A Test Sheet')
    for index,i in enumerate(value):
        try:
            for idx,j in enumerate(i):
                ws.write(index, idx ,j)
        except:
            continue

    # ws.write(1, 0, datetime.now(), style1)
    # ws.write(2, 0, 1)
    # ws.write(2, 1, 1)
    # ws.write(2, 2, xlwt.Formula("A3+B3"))

    wb.save('/home/lv/PycharmProjects/cnki_h5_papers_auto_downloader/get_annotation/classification_xls/'+key+'.xls')

    # with open('/home/lv/PycharmProjects/cnki_h5_papers_auto_downloader/get_annotation/classification/'+key+'.csv','w+') as f:
    #     for i in value:
    #         # print('\\'.join(i)+'\n')
    #         try:
    #             f.write('\\'.join(i)+'\n')
    #         except:
    #             continue
    # f.close()

for key,value in relations.items():
    wb = xlwt.Workbook()
    ws = wb.add_sheet('A Test Sheet')
    for index, i in enumerate(value):
        try:
            for idx, j in enumerate(i):
                ws.write(index, idx, j)
        except:
            continue
    wb.save('/home/lv/PycharmProjects/cnki_h5_papers_auto_downloader/get_annotation/relation_xls/'+key+'.xls')

    # with open('/home/lv/PycharmProjects/cnki_h5_papers_auto_downloader/get_annotation/relation/'+key+'.csv','w+') as f:
    #     for i in value:
    #         # print('\\'.join(i)+'\n')
    #         try:
    #             f.write('\\'.join(i)+'\n')
    #         except:
    #             continue
    # f.close()