#spider for DOUBAN
#UTF - 8
#For py -3
#fist succee
import urllib.request
import urllib3
import re
import pandas as pd
from lxml import etree
def function_getURL(url):
    headers1={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0'}
    headers2={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
    request=urllib.request.Request(url,headers=headers1)
    respon=urllib.request.urlopen(url)
    html=respon.read()
    html=html.decode(encoding='UTF-8')#将网页源码转换为UTF-8格式
    return html
#url解析模块


def function_getcontext(html):
    html=etree.HTML(html)
    list=html.xpath("//ol[@class='grid_view']/li")
    for li in list:
            filmname = li.xpath(".//a/span[@class='title']/text()")
            filmname = filmname [0]
            filmcontext = li.xpath(".//div[@class='bd']/p/text()") [0]
            filmcontext = filmcontext.strip()
            filmcontext = filmcontext.strip('/...')
            filminfo = li.xpath(".//div[@class='bd']/p/text()") [1]
            filminfo = filminfo.strip()
            filmscores = li.xpath(".//div[@class='star']/span[2]/text()")
            filmspeople = li.xpath(".//div[@class='star']/span[4]/text()")
            filmintro = li.xpath(".//p[@class='quote']/span/text()")
            #print(filmcontext)#test
            film = {'电影名称': filmname, '导演及主演': filmcontext, '电影简介': filminfo, '电影评分': filmscores, '评论人数': filmspeople,'电影鉴赏': filmintro}
            films.append(film)
    return films
#信息获取与保存模块


if __name__=='__main__':
    films = []
    page=1
    while page<=10:
        url = ('https://movie.douban.com/top250?start='+str((page-1)*25)+'&filter=')
        html = function_getURL(url)
        t = function_getcontext(html)
        page=page+1
    df=pd.DataFrame(films)
    df.to_csv('C:/Users/香香猪/.PyCharmCE2019.1/config/scratches/TIEBA/DOUBANtop250_clear.csv')
    print('DOWN!')

















