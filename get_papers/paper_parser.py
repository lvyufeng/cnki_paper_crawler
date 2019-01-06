from bs4 import BeautifulSoup
from bs4.element import Tag
# import pymongo
import requests

def get_article_detail(filename):
    url = 'http://kns.cnki.net/KXReader/Detail?dbcode=CJFD&{}&uid='.format(filename)

    wb = requests.get(url)
    soup = BeautifulSoup(wb.text,'lxml')
    content = soup.select('body > div.main > div.content')[0]
    paper = {}
    paper[filename.split('=')[0]] = filename.split('=')[-1]
    h2,brief = [],[]
    for i in content.contents:
        if type(i) == Tag:
            if i.name == 'div':
                if 'id' in i.attrs:
                    if i.get('class')[0] == 'area_img':
                        # if i.select('a'):
                        #     area_img = []
                        #     area_img.append(i.text)
                        #     area_img.append(i.select('a')[0].get('href'))
                        #     paper[i.get('id')] = area_img
                        # else:
                        paper[i.get('id')] = str(i)
                    else:
                        paper[i.get('id')] = i.text
                elif 'class' in i.attrs:
                    if i.get('class')[0] == 'brief':
                        brief.append(i.text)
                        paper['brief'] = brief
                    elif i.get('class')[0] == 'p1':
                        p = i.select('p')[0]
                        paper[p.get('id')] = p.text
                    else:
                        paper[i.get('class')[0]] = i.text
                # elif 'p1' in i.attrs:
                #     p = i.select('p')

            elif i.name == 'h1':
                paper['h1'] = i.text
            elif i.name == 'h2':
                h2.append(i.text)
                paper['h2'] = h2
            elif i.name == 'h3':
                paper[i.get('id')] = i.text
            elif i.name == 'h4':
                paper[i.get('id')] = i.text

    return paper


# get_article_detail('filename=JSJX201812002')