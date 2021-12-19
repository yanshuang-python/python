import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

headers = {
    "User-Agent": UserAgent().chrome
}

url = 'https://zhuanlan.zhihu.com/p/382420453'
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'lxml')
eirong = soup.find_all('div', class_='RichText ztext Post-RichText css-hnrfcf')
for i in eirong:
    print(i.text)
