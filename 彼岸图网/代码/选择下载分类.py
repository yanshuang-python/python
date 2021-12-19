import requests
from lxml import etree
import time


def home_url():
    url = 'https://pic.netbian.com'

    response = requests.get(url=url)
    response.encoding = 'gbk'
    response = response.text
    tree = etree.HTML(response)
    page_list_url = tree.xpath('//*[@id="main"]/div[2]/a/@href')
    print(page_list_url)
    page_list_name = tree.xpath('//*[@id="main"]/div[2]/a/text()')
    while True:
        print("0.风景 1.美女 2.游戏 3.动漫 4.影视 5.明星 6.汽车 7.动物 8.人物 9.美食 10.宗教 11.背景")
        type_name = input("请输入对应数字: ")
        if type_name.isdigit() and 0 <= int(type_name) <= 11:  # 判断是否数字且是否超出可爬取范围
            break
        else:
            print("请重新输入正确的数字")
            continue
    a = int(type_name)
    ab = url + page_list_url[a]

    # 获取下载链接页数
    url1 = ab
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3775.400 QQBrowser/10.6.4208.400'
    }
    response1 = requests.get(url=url1, headers=headers)
    response1.encoding = 'gbk'
    response1 = response1.text
    tree = etree.HTML(response1)
    zongyeshu = tree.xpath('//*[@id="main"]/div[4]/a[7]/text()')
    zongyeshu = zongyeshu[0]
    print('当前类别总页数为' + zongyeshu + '张')

    return ab, page_list_name[a], zongyeshu


if __name__ == '__main__':
    home_url()
