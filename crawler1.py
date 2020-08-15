import requests
from bs4 import BeautifulSoup
#url = 'http://ehappy.tw/bsdemo1.htm'
#html = requests.get(url)
#html.encoding = 'UTF-8'
#sp = BeautifulSoup(html.text, 'lxml')
#print(sp.title)
#print(sp.title.text)


html = '''
    <html>
        <head>
            <meta charset="UTF-8">
            <title>我是網頁標題</title>
        </head>
    <body>
        <img src="http://www.ehappy.tw/python.png">
        <a href="http://www.e-happy.com.tw">超連結</a>
    </body>
</html>
'''
sp = BeautifulSoup(html, 'lxml')
print(sp.find('a'))
print(sp.find_all('a'))
print(sp.find('p', id='p2',class_='red'))
print(sp.select('a'))
print(sp.select('img')[0].get('src'))
print(sp.select('a')[0].get('href'))
print(sp.select('img')[1]['src'])
print(sp.select('a')[0]['href'])
