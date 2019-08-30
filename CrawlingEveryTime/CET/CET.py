from bs4 import BeautifulSoup
import urllib.request

html = urllib.request.urlopen("https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=cur&date=20180821")

soup=BeautifulSoup(html, 'lxml')

titles = soup.find_all('td','title')
scores=list(soup.find_all('td','point'))

print(scores)

'''
movie = {}
score = []

for s in scores:
    score.append(s.text)
    
i=0
rank = 1
for title in titles:
    movie[title.find('a').text]=score[i]
    print(str(rank)+"위: "+title.find('a').text+ ", 평점: "+movie[title.find('a').text])
    i+=1
    rank+=1
'''

'''
rank = 1
for title in titles:
    print(str(rank)+"위: "+title.find('a').text+ ", 평점: "+scores.text)
    rank+=1
'''
    

