#威力彩爬蟲
import requests
from bs4 import BeautifulSoup
url = 'https://www.taiwanlottery.com.tw/'
html = requests.get(url)
html.encoding = 'UTF-8'
sp = BeautifulSoup(html.text, 'lxml')
print('郭柏辰')
block = sp.find('div',class_='contents_box02')
issue = block.find('span', class_='font_black15')
num = block.find_all('div',class_='ball_tx ball_green')
snum = block.find('div',class_='ball_red')
print('威力彩期數:', issue.text)
print('開出順序:', end='')
for i in range(0,6):
    print(num[i].text, end='')
print('\n大小順序:', end='')
for i in range(6,12):
    print(num[i].text, end='')
print('\n第2區:', snum.text)