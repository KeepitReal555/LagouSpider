# -*- coding: utf-8 -*-

import requests
from lxml import etree
import json
import random
import time

#获得网页源代码
def getContent(url,headers):
    html = requests.get(url,headers = headers)
    content = html.content
    return content

#获得跳转下一页的网页
def findNextPage(content):
    tree = etree.HTML(content)
    nextPage = tree.xpath(u"//div[@class = 'item_con_pager']/div[@class = 'pager_container']/a[last()]/@href")
    return nextPage

#找出含有网页地址的结点
def findNodes(content):
    tree = etree.HTML(content)
    nodes = tree.xpath(u"//div[@class = 'position']/div[@class = 'p_top']/a/@href")
    return nodes

#获得职位网站的tree
def get_position_tree(node):
    tempUrl = 'http:' + node
    positionContent = getContent(tempUrl, headers=headers)
    positionTree = etree.HTML(positionContent)
    return positionTree

#对每个职位进行爬取

def find_company(tree):
    companys = []
    companyNodes = tree.xpath(u"//div[@class='company']/text()")
    companys.append(companyNodes)
    return companys

def find_names(tree):
    #命名信息列表
    names = []
    #爬取信息
    namesNodes = tree.xpath(u"//div[@class='job-name']/span[@class='name']/text()")
    #录入信息
    names.append(namesNodes)
    #返回爬取的结果
    return names

def find_salary(tree):
    salarys = []
    salaryNodes = tree.xpath(u"//span[@class='salary']/text()")
    salarys.append(salaryNodes)
    return salarys

def find_request(tree):
    requests = []
    request = tree.xpath(u"//dd[@class='job_request']/p/span[position()>1]/text()")

    requests.append(request)
    return requests
def find_type(tree):
    types= []
    type = tree.xpath(u"//li[@class='labels']/text()")
    types.append(type)
    return types

def find_publishTime(tree):
    publishTimes = []
    publishTime = tree.xpath(u"//p[@class='publish_time']/text()")
    publishTimes.append(publishTime)
    return publishTimes

def find_advantage(tree):

    advantage = tree.xpath(u"//dd[@class = 'job-advantage']/p/text()")

    return advantage

def find_description(tree):
    descriptions = []
    description = tree.xpath(u"//dd[@class='job_bt']/div//p/text()")
    descriptions.append(description)
    return descriptions

def find_address(tree):
    addresses = []
    address = tree.xpath(u"//div[@class='work_addr']//a[position()<4]/text()")
    addresses.append(address)
    return addresses


def find_fourSquare(tree):
    fourSquare = tree.xpath(u"//ul[@class='c_feature']/li[1]/text()")
    return fourSquare
def find_trend(tree):
    trend = tree.xpath(u"//ul[@class='c_feature']/li[2]/text()")
    return trend
def find_doller(tree):
    doller = tree.xpath(u"/ul[@class='c_feature']/li[3]/text()")
    return doller
def find_figure(tree):
    figure = tree.xpath(u"//ul[@class='c_feature']/li[4]/text()")
    return figure
def find_home(tree):
    home = tree.xpath(u"//ul[@class='c_feature']/li/a/@href")
    return home




#完整过程
if __name__ == '__main__':
    url = 'http://www.lagou.com/zhaopin/'
    #随机头信息
    USER_AGENTS = [
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
        "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
        "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
        "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
        "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
        "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
        "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
        "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
        "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10"
    ]
    headers = {'User-Agent': random.choice(USER_AGENTS)}

    count = 0
    #打开txt文件
    file = open('lagouZhaopin.txt','wr')

    page_count = 1
    position_count = 1

    print '开始爬取'

    while count<30:
        #开始爬取

        #一个网页中所有的职位链接
        content = getContent(url, headers=headers)
        time.sleep(random.randint(1, 3))

        nodes = findNodes(content)

        print '现在爬取第'+str(page_count)+'页'
        #对一页开始爬取
        for positionUrl in nodes:
            print '现在爬取第'+str(position_count)+'个职位'
            tree = get_position_tree(positionUrl)

            # 爬取一个完整的职业
            company = find_company(tree)
            time.sleep(random.randint(1,3))
            name = find_names(tree)
            time.sleep(random.randint(1, 3))
            salary = find_salary(tree)
            time.sleep(random.randint(1, 3))
            request = find_request(tree)
            time.sleep(random.randint(1, 3))
            type = find_type(tree)
            time.sleep(random.randint(1, 3))
            publishTime = find_publishTime(tree)
            time.sleep(random.randint(1, 3))
            advantage = find_advantage(tree)
            time.sleep(random.randint(1, 3))
            description = find_description(tree)
            time.sleep(random.randint(1, 3))
            address = find_address(tree)
            time.sleep(random.randint(1, 3))
            fourSquare = find_fourSquare(tree)
            time.sleep(random.randint(1, 3))
            trend = find_trend(tree)
            time.sleep(random.randint(1, 3))
            doller = find_doller(tree)
            time.sleep(random.randint(1, 3))
            figure = find_figure(tree)
            time.sleep(random.randint(1, 3))
            home = find_home(tree)

            list = {'公司': company,
                    '职业': name,
                    '薪水': salary,
                    '要求': request,
                    '类型': type,
                    '发布时间': publishTime,
                    '职业诱惑': advantage,
                    '职业描述': description,
                    '地址': address,
                    '领域': fourSquare,
                    '投资机构': doller,
                    '发展阶段': trend,
                    '规模': figure,
                    '公司主页': home
                    }

            #写入txt文件中
            json_of_list = json.dumps(list,indent=4)
            file.write(json_of_list+'\n')
            position_count = position_count + 1
        # 爬取完一整页
        count = count + 1

        #获取下一页链接
        for url in findNextPage(content):
            url = 'http:' + url
        #获取下一页的文本
        page_count = page_count + 1

    #关闭文件
    file.close()

