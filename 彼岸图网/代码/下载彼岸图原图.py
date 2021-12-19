import requests
import 选择下载分类
from bs4 import BeautifulSoup
from queue import Queue
import re
import csv
import 创建重要文件夹以及图片文件夹
import threading


# 请求
def resp(url):
    response = requests.get(url=url)
    response.encoding = 'gbk'
    return response.text


# 获取单页图片链接
def y_html(url, urls):
    开始页数 = input("请输入开始下载页数:")
    结束页数 = input("请输入结束下载页数:")

    for i in range(int(开始页数), int(结束页数)):
        url2 = url + 'index_{页数}.html'.format(页数=i)
        html = resp(url2)
        s_thml = BeautifulSoup(html, 'lxml')
        ul = s_thml.find('ul', class_='clearfix')
        lis = ul.select('li')
        该函数内拼接图片下载 = 'https://pic.netbian.com'
        for li in lis:
            li = li.a['href']
            li = 该函数内拼接图片下载 + li
            urls.put(li)
    return urls


# 获取图片下载地址
def y_text(urls, 存储未下载图片):
    while urls.qsize() != 0:
        a = urls.get()
        # 请求图片页面

        response = resp(a)
        图片名字网页源代码 = response
        图片名字 = re.findall("<h1>(.*)</h1>", 图片名字网页源代码)[0]
        # 获取页面源代码中下载地址
        dz0 = re.findall("<script src=/e/public/(.*)></script>", response)[0]
        # 拼接图片下载地址
        dz0 = str(dz0)
        cla = str(dz0.split('?')[1])
        cla1 = cla.rsplit('&')[0]
        cla2 = cla.rsplit('&')[1]
        # 将拼接地址保存
        zh_url = 'https://pic.netbian.com/downpic.php?{name1}&{name2}'.format(name1=cla2, name2=cla1)

        # 检测准备下载的图片是否存在
        with open('../重要文件/已下载.csv', 'r', newline='') as f:
            reader = csv.reader(f)
            判断是否存在 = 0
            for row in reader:
                # 如果存在则跳过
                if zh_url == row[0]:
                    判断是否存在 = 1
                    print("已存在")
                    break
        if 判断是否存在 != 1 and 存储未下载图片.qsize() <= 199:
            临时存储列表 = [zh_url, 图片名字]
            存储未下载图片.put(临时存储列表)
            print("即将开始下载", 存储未下载图片.qsize(), "张图片")


def 保存到本地(存储未下载图片):
    while 存储未下载图片.qsize() != 0:
        url, 图片名字 = 存储未下载图片.get()
        print(url, 图片名字)
        # 设置cookie
        headers = {
            'cookie': '__yjs_duid=1_585d143347311266b65276bb9ee8e2431634291020055; Hm_lvt_526caf4e20c21f06a4e9209712d6a20e=1634291022; PHPSESSID=2qcq6nm8iisef7s1rbflg190p7; zkhanmlusername=%D1%D5%CB%AA; zkhanmluserid=4685371; zkhanmlgroupid=6; zkhanmlrnd=5zlDkuaZyx4aoRAgWSkL; zkhanmlauth=3188b87d0f0d5296b6c444b4817addbc; Hm_lpvt_526caf4e20c21f06a4e9209712d6a20e=1634291061',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36',
        }
        # 发送请求
        tp = requests.get(url, headers=headers)
        with open(r'../图片/{name}'.format(name=图片名字) + '.jpg', 'wb') as f:
            f.write(tp.content)
        # 写入已下载图片
        存储已下载图片防止下载 = [url]
        with open('../重要文件/已下载.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(存储已下载图片防止下载)


def main():
    # 创建保存文件文件夹
    创建重要文件夹以及图片文件夹.cjwj()
    # 创建安全文件夹
    urls = Queue()
    存储未下载图片 = Queue()
    url = 选择下载分类.home_url()
    y_text(y_html(url[0], urls), 存储未下载图片)
    print('本次将下载' + 存储未下载图片.qsize() + '张图片')
    for i in range(50):
        ys1 = threading.Thread(target=保存到本地, args=(存储未下载图片,))
        ys1.start()
    保存到本地(存储未下载图片)


if __name__ == '__main__':
    main()
