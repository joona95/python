'''
daum crawling data 시각화 
'''

from konlpy.tag import Kkma

# object 생성 
kkma = Kkma() # 기본 생성자 

# 1. text file 읽기

f = open("../data/crawling_data.txt", mode='r', encoding='utf-8')
doc = f.read() # 전체 읽기 
f.close()

# doc -> sentence
ex_sen = kkma.sentences(doc)
print(ex_sen)
'''
for s in ex_sen :
    print(s)
'''

# 2. doc -> nouns 추출 
ex_nouns = kkma.nouns(doc)
print(ex_nouns)


from re import match

# 3. text 전처리 : 숫자, 1자 제외 
noun_count= {} # 빈 set

for sent in ex_sen : # '형태소 분석을 시작합니다.'
    for nouns in  kkma.nouns(sent) : # '형태소', '분석'
        #  단어 길이, 숫자 제외 
        if len(str(nouns)) > 1 and not(match('^[0-9]', nouns)) :
            noun_count[nouns] = noun_count.get(nouns, 0) + 1
            
print(noun_count)            
   

# 단어 카운트 
from collections import Counter

word_count = Counter(noun_count)
print(word_count)

word_top10 = word_count.most_common(10)
print(word_top10)
# [('확인', 3), ('전쟁', 2), ('특검', 2), ('조사', 2), ('소개', 2), ('보상', 2), ('화재', 2), ('폭염', 2), ('국민', 2), ('국민연금', 2)]

import pytagcloud

# tag에 color, size, tag 사전 구성 
word_count_list = pytagcloud.make_tags(word_top10, maxsize=80)
# maxsize : 최대 글자크기
print(word_count_list)

pytagcloud.create_tag_image(word_count_list,
                            'newsCrawlingData.jpg', 
                            size=(900, 600), 
                            fontname='korean', rectangular=False)




