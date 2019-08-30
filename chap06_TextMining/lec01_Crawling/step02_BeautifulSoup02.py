'''
 - tab 속성과 내용 가져오기
   <a href="www.naver.com"> 네이버 </a>
 - 정규표현식으로 속성값 추출 
'''

from bs4 import BeautifulSoup

# 1. html source 가져오기
file = open('../html/html02.html', mode='r', encoding='utf-8')
html = file.read()
print(html)

# 2. html 파싱
soup = BeautifulSoup(html, 'html.parser')
print(soup)

# 3. a 태그 내용 가져오기
links = soup.find_all('a')
print(links)
# [<a href="www.naver.com">네이버</a>, <a href="http://www.naver.com">네이버</a>, <a href="http://www.naver.com" target="_blank">네이버 새창으로</a>, <a href="www.duam.net">다음</a>, <a href="http://www.duam.net">다음</a>]

for link in links :
    print(link.string) # 내용
    '''
    print(link.attrs) # 속성 : {'속성':'값'} # {'href': 'www.naver.com'}
    print(link.attrs['href']) # www.naver.com
    '''
    
    if 'target' in link.attrs :
        print(link.attrs['href'], link.attrs['target'])
    else :
        print(link.attrs['href'])
'''
네이버
www.naver.com
네이버
http://www.naver.com
네이버 새창으로
http://www.naver.com _blank
다음
www.duam.net
다음
http://www.duam.net
'''


# 4. 정규표현식으로 속성값 가져오기
import re

# href = "http://~
links = soup.find_all(href=re.compile("http://"))
print(links)
print(len(links)) # 3

for link in links :
    print(link.string) # 내용
    print(link.attrs['href']) # 속성값
    