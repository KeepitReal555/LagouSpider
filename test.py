import requests
from lxml import etree

url = 'http://news.sohu.com'

def getContent(url,headers):
    html = requests.get(url,headers = headers)
    content = html.content
    return content

def find_newsurl(url):
    tree = etree.HTML(content)
    newsurl = tree.xpath(u"//@href")
    return newsurl

if __name__ == '__main__':

    url = 'http://news.sohu.com'
    headers = {'User-Agent':"Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52"}
    content = getContent(url, headers=headers)
    nodes = find_newsurl(content)
