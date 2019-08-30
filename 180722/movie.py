import requests
from bs4 import BeautifulSoup

r = requests.get("http://www.cgv.co.kr/movies/?ft=0")
c = r.content
# print(c)
html = BeautifulSoup(c, 'html.parser')

# print(html)
# print(type(html))

ol = html.find("ol")

li = ol.find_all("li")

# print(li[0])
# print(len(li))

for x in li:
    div = x.find("div",{"class":"box-contents"})
    strong = div.find("strong").text
    print(strong)


print("parsing End")