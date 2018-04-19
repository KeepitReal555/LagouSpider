# -*- coding: utf-8 -*-

import requests
from lxml import etree
import json
import random
import time
import datetime
from pymongo import MongoClient
import re

client = MongoClient()

#存储数据到Mongodb
def save(data): #data为存储的单条记录
    db = client.Lagou_database
    coll = db.Zhaopin_collection
    result = db.coll.insert_one(data)






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

    headers = {'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20"}

    count = 0
    # #打开txt文件
    # file = open('lagouZhaopin.txt','wr')

    page_count = 1
    position_count = 1

    print '开始爬取'

    # while count<30:
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


        positionIdlist = re.findall(r'\d*\d',positionUrl)
        positionId = ''.join(positionIdlist)
            # 爬取一个完整的职业
        company = find_company(tree)
        time.sleep(random.randint(1,2))
        name = find_names(tree)

        salary = find_salary(tree)
        time.sleep(random.randint(1,2))
        request = find_request(tree)

        type = find_type(tree)
        time.sleep(random.randint(1,2))
        publishTime = find_publishTime(tree)

        advantage = find_advantage(tree)
        time.sleep(random.randint(1,2))
        description = find_description(tree)

        address = find_address(tree)
        time.sleep(random.randint(1,2))
        fourSquare = find_fourSquare(tree)
        time.sleep(random.randint(1,2))
        trend = find_trend(tree)

        doller = find_doller(tree)
        time.sleep(random.randint(1,2))
        figure = find_figure(tree)
        time.sleep(random.randint(1,2))
        home = find_home(tree)


        list = {
                'positionId': positionId,
                '公司': company,
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
                '公司主页': home,
                'datetime': datetime.datetime.now()
                }

        #写入txt文件中

        save(list)
        # file.write(json_of_list+'\n')
        position_count = position_count + 1
        # 爬取完一整页
        # count = count + 1


        # #获取下一页链接
        # for url in findNextPage(content):
        #     url = 'http:' + url
        # #获取下一页的文本
        # page_count = page_count + 1

    # #关闭文件
    # file.close()

