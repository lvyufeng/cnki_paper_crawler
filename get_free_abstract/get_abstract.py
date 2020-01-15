from bs4 import BeautifulSoup
import requests

# cnki dbcode
# CJFD      中国学术期刊网络出版总库
# SSJD      国际期刊数据库
# CRLDENG   外文题录数据库
# RefType
# 1     参考文献
# 2     二级参考文献
# 3     引证文献
# 4     二级引证文献
# 5     共引文献
# 6     同被引文献 

def get_one_paper(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text,'lxml')
    summary = soup.select('#ChDivSummary')
    title = soup.select('#mainArea > div.wxmain > div.wxTitle > h2')
    author = soup.select('#mainArea > div.wxmain > div.wxTitle > div.author')
    org = soup.select('#mainArea > div.wxmain > div.wxTitle > div.orgn')
    keywords = soup.select('#mainArea > div.wxmain > div.wxInfo > div.wxBaseinfo > p:nth-of-type(4)')
    print(title,author,org,summary)

def get_reference():
    """
    test url: http://kns.cnki.net/kcms/detail/frame/list.aspx?dbcode=CJFD&filename=jsjx201712015&dbname=CJFDLAST2018&RefType=1&vl=
    web url: http://wap.cnki.net/touch/web/Article/GetArticleYinWenList
    """
    url = 'http://wap.cnki.net/touch/web/Article/GetArticleYinWenList'
    parameters = {
        'fileName': 'WXYJ201710023',
        'yinwenType': 0,
        'articleType': 'CJFD',
        'pageIndexs': 1,
        'pageSizes': 10,
    }
    r = requests.post(url,data=parameters)

    pass

# url = 'http://kns.cnki.net/kcms/detail/detail.aspx?dbcode=CJFD&filename=JSJX201712015&dbname=CJFDLAST2018'
# get_one_paper(url)

get_reference()