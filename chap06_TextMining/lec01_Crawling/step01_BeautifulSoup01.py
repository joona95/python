'''
1. Tab 이름으로 추출
2. find()함수로 추출
'''

from bs4 import BeautifulSoup

# 1. html source 가져오기
file = open('../html/html01.html', mode='r', encoding='utf-8')
html = file.read()
print(html)

# 2. html 파싱
soup = BeautifulSoup(html, 'html.parser')
print(soup)

# 3. 태그 내용 가져오기

# 1) tab 이용
h1 = soup.html.body.h1
print('h1 : ', h1.string)
# h1 :   시멘틱 태그 ?

# 2) find()함수 : 태그 찾기
h2 = soup.find("h2") # 태그가 여러개 있어도 제일 첫번째꺼만 찾아줌
print("h2 : ", h2.string)
# h2 :   주요 시멘틱 태그 


# 3) find_all()함수
lis = soup.find_all('li') # 값 여러개일 경우 list 반환
print(lis)
# [<li> header : 문서의 머리말(사이트 소개, 제목, 로그 )</li>, <li> nav : 네이게이션(메뉴) </li>, <li> section : 웹 문서를 장(chapter)을 볼 때 절을 구분하는 태그</li>, <li> aside : 문서의 보조 내용(광고, 즐겨찾기, 링크) </li>, <li> footer : 문서의 꼬리말(작성자, 저작권, 개인정보보호) </li>]

for li in lis :
    print(li.string)
'''
 header : 문서의 머리말(사이트 소개, 제목, 로그 )
 nav : 네이게이션(메뉴) 
 section : 웹 문서를 장(chapter)을 볼 때 절을 구분하는 태그
 aside : 문서의 보조 내용(광고, 즐겨찾기, 링크) 
 footer : 문서의 꼬리말(작성자, 저작권, 개인정보보호)
'''
    
    
    
