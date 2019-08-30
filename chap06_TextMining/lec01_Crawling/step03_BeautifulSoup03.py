'''
 - 선택자(selector) 이용 내용 추출하기
   -> 웹 문서 디자인(css)용으로 사용
   -> 선택자 : id(#), class(.)
   -> soup.select_one(tag#id) : 하나의 요소 추출 
   -> soup.select(tag.class) : 여러 개의 요소 추출
'''

from bs4 import BeautifulSoup

# 1. html source 가져오기
file = open('../html/html03.html', mode='r', encoding='utf-8')
html = file.read()
print(html)

# 2. html 파싱
soup = BeautifulSoup(html, 'html.parser')
print(soup)

# 3. 선택자 이용 태그 내용 가져오기

# 1) id 선택자 : 형식) tag#id명
table = soup.select_one("table#tab")
print(table)

# 2) id 선택자 > 하위 태그 
th = soup.select_one("table#tab > tr > th") # 계층적 접근 : 제목 열
print(th) # <th id="id"> 학번 </th>

ths = soup.select("table#tab > tr > th")
print(ths) # list 반환   # [<th id="id"> 학번 </th>, <th id="name"> 이름 </th>, <th id="major"> 학과 </th>, <th id="email"> 이메일 </th>]

for th in ths :
    print(th.string)
    
# 3) 태그[속성=값] 요소 가져오기
trs = soup.select("tr[class=odd]")
print(trs)

print('*** tr > td 출력  ***')
for tr in trs : # 2회 반복
    #print(tr)
    tds = tr.find_all('td')
    for td in tds:
        print(td.string)
        
        