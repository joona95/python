'''
영화 추천 시스템 알고리즘
 - 추천 대상자 : User   
 - 유사도 평점 = 기존 영화평점 * User 유사도
 - 추천 영화 예측 = 유사도 평점 / User 유사도 
'''

import pandas as pd

# 1. 데이터 가져오기 
ratings = pd.read_csv('../data/movie_rating.csv')
print(ratings)
#  평론가[critic]   영화[title]  평점[rating]

# reset_index() : default index 첫번째 칼럼 삽입(이유 : index -> 칼럼)  

# 2. pivot table 작성 : row(영화제목), column(평가자), content(평점)
print('movie_ratings')
movie_ratings = pd.pivot(index = ratings.title, columns = ratings.critic, 
                         values = ratings.rating).reset_index()
print(movie_ratings) # default index 추가 
# critic      title  Claudia  Gene  Jack  Lisa  Mick  Toby
# 0         Just My      3.0   1.5   NaN   3.0   2.0   NaN
# 1            Lady      NaN   3.0   3.0   2.5   3.0   NaN
# 2          Snakes      3.5   3.5   4.0   3.5   4.0   4.5
# 3        Superman      4.0   5.0   5.0   3.5   3.0   4.0
# 4       The Night      4.5   3.0   3.0   3.0   3.0   NaN
# 5          You Me      2.5   3.5   3.5   2.5   2.0   1.0

# [추가] toby 평균 영화평점 
# print(movie_ratings.Toby.mean()) # 3.1666666666666665
# [추가] 결측치가 포함된 관측치 제거 : DF.dropna()
#print(movie_ratings.dropna())

# 3. 사용자별 유사도(상관계수 R) 계산 : 번호 행 추가 효과 
sim_users = movie_ratings.corr(method='pearson').reset_index()
print(sim_users) # default index 추가 
'''
critic   critic   Claudia      Gene      Jack      Lisa      Mick      Toby
0       Claudia  1.000000  0.314970  0.028571  0.566947  0.566947  0.893405
1          Gene  0.314970  1.000000  0.963796  0.396059  0.411765  0.381246
2          Jack  0.028571  0.963796  1.000000  0.747018  0.211289  0.662849
3          Lisa  0.566947  0.396059  0.747018  1.000000  0.594089  0.991241
4          Mick  0.566947  0.411765  0.211289  0.594089  1.000000  0.924473
5          Toby  0.893405  0.381246  0.662849  0.991241  0.924473  1.000000
'''

# 4. Toby 미관람 영화 + 유사도 
# 1) movie_ratings data에서 title, Toby 칼럼으로 subset 작성 
toby_rating = movie_ratings[['title', 'Toby']] # index 칼럼 추가 
print(toby_rating.columns) # Index(['title', 'Toby']
# 칼럼명 교체 
toby_rating.rename(columns={'Toby':'rating'}, inplace = True)
print(toby_rating)
'''
critic title  rating
0    Just My     NaN
1       Lady     NaN
2     Snakes     4.5
3   Superman     4.0
4  The Night     NaN
5     You Me     1.0
'''

# 2) Toby 미관람 영화 추출 : rating null 조건으로 title 추출 
print('Toby 미 관람 영화 제목 추출')
# 형식) DF.추출칼럼[DF.조건칼럼.isnull()]
toby_not_see = toby_rating.title[toby_rating.rating.isnull()] 
print(toby_not_see)
'''
0      Just My
1         Lady
4    The Night
'''
print(type(toby_not_see)) # Series
toby_not_see = list(toby_not_see) # Series -> list
'''
Name: title, dtype: object
['Just My' 'Lady' 'The Night']
'''
# list 값 포함 유무 리턴 
title='Just My'
print(title in toby_not_see) # True

# 3) raw data에서 Toby가 미관람 영화 관측치 가져오기
# ratings 열축(행단위) 단위로 람다 함수 호출 : if ratings.title == toby_not_see
# 람다 함수 리턴 결과로 subset 생성 
rating_t = ratings[ratings.apply(lambda x : x.title in toby_not_see, axis=1)]
print(rating_t)
'''
     critic      title  rating
0      Jack       Lady     3.0
4      Jack  The Night     3.0
5      Mick       Lady     3.0
:
30     Gene  The Night     3.0
'''

# 4) Toby 미관람 영화 + Toby 유사도 join
toby_sim = sim_users[['critic','Toby']]
#help(pd.merge)
# on='critic' : critic 칼럼으로 DF 병합(join)
rating_t = pd.merge(rating_t, toby_sim, on='critic')
# 칼럼명 수정 
rating_t.rename(columns={'Toby':'similarity'}, inplace = True)
print(rating_t)
'''
     critic      title  rating  similarity
0      Jack       Lady     3.0    0.662849
1      Jack  The Night     3.0    0.662849
2      Mick       Lady     3.0    0.924473
'''

# 5. 영화 등급 예측/추천
# 1) 유사도 평점 계산 = Toby미관람 영화 평점 * Tody 유사도 
rating_t['similarity_rating'] = rating_t.rating * rating_t.similarity
print(rating_t)
'''
     critic      title  rating  similarity  sim_rating
0      Jack       Lady     3.0    0.662849    1.988547
1      Jack  The Night     3.0    0.662849    1.988547
2      Mick       Lady     3.0    0.924473    2.773420
[해설] 평점과 유사도가 클 수록 유사도 평점은 커진다.
'''
# 2) Toby 영화추천 예측 = 유사도 평점 / Tody 유사도 
tgroup = rating_t.groupby(['title']).sum() # 영화 제목별 평점과 유사도  
tgroup['predict'] = tgroup.similarity_rating / tgroup.similarity
print(tgroup)
'''
           rating  similarity  similarity_rating   predict
title                                                     
Just My       9.5    3.190366           8.074754  2.530981
Lady         11.5    2.959810           8.383808  2.832550
The Night    16.5    3.853215          12.899752  3.347790
'''

# 3) Toby 영화 추천 결과 시각화
import matplotlib.pyplot as plt
toby_movie_recomm = tgroup.sort_values('predict', ascending=True)
print(toby_movie_recomm) 
toby_movie_recomm[['similarity_rating', 'predict']].plot(kind='barh', 
                                                         title='movie recommend  result')
plt.show()






