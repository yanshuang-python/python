# 完成后需要下载FFmpeg
# 运行方法:
# FFmpeg -i video.mp4 -i audio.mp3 -c:v copy -c:a aas -strict experimental output.mp4

import requests
from fake_useragent import UserAgent
import re
import json
from bs4 import BeautifulSoup

def html_url(url):
    headers={
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36',
        'referer': 'https://www.bilibili.com/'
    }
    response= requests.get(url, headers=headers)
    return response

def video_text(html):
    html = html.text
    script = re.findall('window\.__playinfo__=(.*?)</script>', html)[0]
    title_html = html
    xiushi = BeautifulSoup(title_html, 'lxml')
    name = xiushi.find('title').text
    script_json = json.loads(script)
    shipin_url = script_json['data']['dash']['video'][0]['base_url']
    shengyin_url = script_json['data']['dash']['audio'][0]['base_url']
    return shipin_url, shengyin_url, name

def wenjian(mv, mu, name, ys):
    shipin = html_url(mv).content
    yinyue = html_url(mu).content
    with open(ys + name + '.mp4', 'wb') as f:
        f.write(shipin)
    with open(ys + name + '音频.mp3', 'wb') as f:
        f.write(yinyue)


if __name__ == '__main__':

    url=input('请输入想爬取的视频url:')
    print('输入一个  .  为保存到当前代码所在路径')
    ys = input('请输入保存地址:')
    ys = ys + '\\'
    html = html_url(url)
    shipin, yinpin, name = video_text(html)
    wenjian(shipin, yinpin, name, ys)




'''
完成后安装ffmpeg运行以下代码
ffmpeg -i 绝命响应：第1话_国创_bilibili_哔哩哔哩.mp4 -i 绝命响应：第1话_国创_bilibili_哔哩哔哩音频.mp3 -c:v copy -c:a aac -strict experimental output.mp4
ffmpeg -i 绝命响应：第1话_国创_bilibili_哔哩哔哩.mp4(为mp4地址) -i 绝命响应：第1话_国创_bilibili_哔哩哔哩音频.mp3(为mp3地址) -c:v copy -c:a aac(为解码方式) -strict experimental output.mp4(
'''