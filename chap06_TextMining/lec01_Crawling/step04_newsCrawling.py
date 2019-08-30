'''
 - news Crawling
   url : http://media.daum.net
'''

import requests
from bs4 import BeautifulSoup

url = "http://media.daum.net"

# 1. url 요청
src = requests.get(url)
print(src) # 제대로 됐으면 <Response [200]>

html = src.text
# html 파싱
soup = BeautifulSoup(html, "html.parser")
print(soup)


# 2. tag[속성=값] 요소 추출
atags = soup.select('a[class=link_txt]')
print(atags)
print(len(atags)) # 104

crawling_data = [] # 빈 list

cnt = 0
for atag in atags :
    cnt +=1
    content = str(atag.string)
    print(cnt, '=>', content)
    crawling_data.append(content.strip())
    '''
    string.strip() : 문단 끝부분 공백, tab, \n\r 불용어 제거
    '''
    
print('crawling result')
print(crawling_data)


# text save
file = open('../data/crawling_data.txt',mode='w',encoding='utf-8')
file.write(str(crawling_data)) # save
file.close()
print('text file 확인')

