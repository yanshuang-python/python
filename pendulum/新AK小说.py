import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import re
from queue import Queue
from time import sleep


def html(url, ulrs):
    headers = {
        "User-Agent": UserAgent().chrome
    }
    response = requests.get(url, headers=headers)
    response = response.text
    soup = BeautifulSoup(response, 'lxml')
    html = soup.find('div', class_="all")
    html = html.find('ul')
    li = html.select('li > a')
    for i in li:
        i = str(i)
        i = re.findall('href="(.*?)"', i)[0]
        ulrs.put(i)


def html_1(urls, xiaoshuoming):
    sleep(0.5)
    while urls.qsize() != 0:
        headers = {
            "User-Agent": UserAgent().chrome
        }
        response = requests.get(urls.get(), headers=headers)
        response = response.text
        name = re.findall('<h1>(.*?)</h1>', response)[0]

        neirong = re.findall('<div id="booktxt">(.*?)</div>', response)[0]
        neirong = str(neirong)
        neirong = neirong.replace(r'\u3000', '')
        neirong = neirong.replace(r'<p>', '')
        neirong = neirong.replace(r'</p>', '')
        with open('/{xsm}.txt'.format(xsm=xiaoshuoming), 'a', encoding='utf-8') as f:
            f.write(name + '\n')
            f.write(neirong + '\n' + '\n' + '\n')
        print('剩余', urls.qsize(), '张-未下载')
        sleep(0.5)

        下一页 = re.findall('<a href=".*" rel="next" id="next_url">(.*?)</a>', response)[0]
        if 下一页 == '下一页':
            print('检测到当前章节有第二页,正在下载...')

            下一页链接 = re.findall('<a rel="next" href="(.*?)">下一页</a>', response)[0]
            第二页url = 'https://www.x23ak.com' + 下一页链接


response_2 = requests.get(第二页url, headers=headers)
response_2 = response_2.text
name_2 = re.findall('<h1>(.*?)</h1>', response_2)[0]
neirong_2 = re.findall('<div id="booktxt">(.*?)</div>', response_2)[0]
neirong_2 = str(neirong_2)
neirong_2 = neirong_2.replace(r'\u3000', '')
neirong_2 = neirong_2.replace(r'<p>', '')
neirong_2 = neirong_2.replace(r'</p>', '')
with open('/{xsm}.txt'.format(xsm=xiaoshuoming), 'a', encoding='utf-8') as f:
    f.write(name_2 + '\n')
    f.write(neirong_2 + '\n' + '\n' + '\n')
    sleep(0.5)

print('章节第二页下载完成')


def main():
    urls = Queue()
    print('原网址是:' + 'http://www.x23ak.com')
    print('示例:http://www.x23ak.com/ak/508208/')
    url = input('请输入下载链接:')
    xiaoshuoming = input('请输入小说名:')
    html(url, urls)
    html_1(urls, xiaoshuoming)


if __name__ == '__main__':
    main()
