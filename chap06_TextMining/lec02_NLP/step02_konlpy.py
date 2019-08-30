'''
konlpy test
'''

from konlpy.tag import Kkma


# object 생성
kkma = Kkma()


# 문단 -> 문장 추출
para = "형태소 분석을 시작합니다. 나는 홍길동 이고 age는 28세 입니다."
ex_sen = kkma.sentences(para)
print(ex_sen) # list

# 문단 -> 명사 추출
ex_noun = kkma.nouns(para)
print(ex_noun)
# ['형태소', '분석', '나', '홍길동', '28', '28세', '세']

# 문단 -> 형태소 추출
ex_pos = kkma.pos(para)
print(ex_pos)
# [('형태소', 'NNG'), ('분석', 'NNG'), ('을', 'JKO'), ('시작하', 'VV'), ('ㅂ니다', 'EFN'), ('.', 'SF'), ('나', 'NP'), ('는', 'JX'), ('홍길동', 'NNG'), ('이', 'VCP'), ('고', 'ECE'), ('age', 'OL'), ('는', 'JX'), ('28', 'NR'), ('세', 'NNM'), ('이', 'VCP'), ('ㅂ니다', 'EFN'), ('.', 'SF')]

