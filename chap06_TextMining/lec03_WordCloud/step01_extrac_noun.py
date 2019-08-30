'''
1. text file 읽기
2. 명사 추출
3. 전처리 : 단어 길이 제한, 숫자 제외
4. word cloud 시각화
'''
from re import match
from konlpy.tag import Kkma

# object 생성
kkma = Kkma() # 기본 생성자

# 1. text file 읽기

f = open("../data/text_data.txt", mode="r", encoding='utf-8')
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
# ['형태소', '분석', '나', '데이터', '직업', '전문가', '기법', '2000', '2000대', '대', '초반', '개발', '기술']


# 3. text 전처리 : 숫자, 1자 제외
noun_count={} # 빈 set

for sent in ex_sen : # '형태소 분석을 시작합니다.'
    for nouns in kkma.nouns(sent) : # '형태소', '분석'
        # 단어 길이, 숫자 제외
        if len(str(nouns)) >1 and not(match('^[0-9]',nouns)) :
            noun_count[nouns] = noun_count.get(nouns,0)+1
            
print(noun_count)
# {'형태소': 1, '분석': 3, '데이터': 2, '직업': 1, '전문가': 1, '기법': 1, '초반': 1, '개발': 1, '기술': 1}


# 단어 카운트
from collections import Counter

word_count = Counter(noun_count)
print(word_count)

word_top5 = word_count.most_common(5)
print(word_top5)
# [('분석', 3), ('데이터', 2), ('형태소', 1), ('직업', 1), ('전문가', 1)]


import pytagcloud

# tag에 color, size, tag 사전 구성 
word_count_list = pytagcloud.make_tags(word_top5, maxsize=80)
# maxsize : 최대 글자크기
print(word_count_list)
'''
[{'color': (91, 34, 34), 'size': 109, 'tag': '분석'}, {'color': (95, 159, 59), 'size': 80, 'tag': '데이터'}, {'color': (194, 214, 193), 'size': 47, 'tag': '형태소'}]
'''
pytagcloud.create_tag_image(word_count_list,
                            'wordcloud.jpg', 
                            size=(900, 600), 
                            fontname='korean', rectangular=False)
