'''
문1) movie_rating.csv 파일을 대상으로 다음과 같이 단계별로 그룹화 하시오.
   <단계1> critic(평가자), title(영화제목)으로  rating(평점) 그룹화 
   <단계2> critic(평가자) 행으로, title(영화제목) 열로 테이블 생성 
   <단계3> 영화별  rating(평점) 합계 출력 및 오름차순 정렬            
'''
import pandas as pd

rating = pd.read_csv('../data/movie_rating.csv')

print(rating.info())
'''
RangeIndex: 31 entries, 0 to 30
Data columns (total 3 columns):
critic    31 non-null object  -> 평가자 (6명)
title     31 non-null object  -> 영화제목(6편)
rating    31 non-null float64 -> 영화평점(1~5)
'''

# <단계1> critic(평가자), title(영화제목)으로  rating(평점) 그룹화 
rating_g = rating.groupby(['critic','title'])
print(rating_g.size())
'''critic   title    
Claudia  Just My      1
         Snakes       1
         Superman     1
         The Night    1
         You Me       1
Gene     Just My      1
         Lady         1
         Snakes       1
         Superman     1
         The Night    1
         You Me       1
Jack     Lady         1
         Snakes       1
         Superman     1
         The Night    1
         You Me       1
Lisa     Just My      1
         Lady         1
         Snakes       1
         Superman     1
         The Night    1
         You Me       1
Mick     Just My      1
         Lady         1
         Snakes       1
         Superman     1
         The Night    1
         You Me       1
Toby     Snakes       1
         Superman     1
         You Me       1
'''

print(type(rating_g.size()))
# <class 'pandas.core.series.Series'>

print(rating_g.sum())
'''
                   rating
critic  title            
Claudia Just My       3.0
        Snakes        3.5
        Superman      4.0
        The Night     4.5
        You Me        2.5
Gene    Just My       1.5
        Lady          3.0
        Snakes        3.5
        Superman      5.0
        The Night     3.0
        You Me        3.5
Jack    Lady          3.0
        Snakes        4.0
        Superman      5.0
        The Night     3.0
        You Me        3.5
Lisa    Just My       3.0
        Lady          2.5
        Snakes        3.5
        Superman      3.5
        The Night     3.0
        You Me        2.5
Mick    Just My       2.0
        Lady          3.0
        Snakes        4.0
        Superman      3.0
        The Night     3.0
        You Me        2.0
Toby    Snakes        4.5
        Superman      4.0
        You Me        1.0
'''


# <단계2> critic(평가자) 행으로, title(영화제목) 열로 테이블 생성 
# 힌트) unstack() : long -> wide
rating_table = rating_g.sum().unstack()
print(rating_table)
'''
         rating                                      
title   Just My Lady Snakes Superman The Night You Me
critic                                               
Claudia     3.0  NaN    3.5      4.0       4.5    2.5
Gene        1.5  3.0    3.5      5.0       3.0    3.5
Jack        NaN  3.0    4.0      5.0       3.0    3.5
Lisa        3.0  2.5    3.5      3.5       3.0    2.5
Mick        2.0  3.0    4.0      3.0       3.0    2.0
Toby        NaN  NaN    4.5      4.0       NaN    1.0
'''


# <단계3> 영화별  rating(평점) 합계 출력 및 오름차순 정렬   
movie_sum = rating_table.sum(axis=0) # 칼럼 단위 합계
print(movie_sum)
'''
        title    
rating  Just My       9.5
        Lady         11.5
        Snakes       23.0
        Superman     24.5
        The Night    16.5
        You Me       15.0
'''

movie_sum_sorted = rating_table.sum(axis=0).sort_values() #오름차순 정렬
print(movie_sum_sorted)
'''
        title    
rating  Just My       9.5
        Lady         11.5
        You Me       15.0
        The Night    16.5
        Snakes       23.0
        Superman     24.5
'''

# 평가자별 평점 합계 출력
user_sum = rating_table.sum(axis=1) # 행 단위 합계
print(user_sum)
'''
critic
Claudia    17.5
Gene       19.5
Jack       18.5
Lisa       18.0
Mick       17.0
Toby        9.5
'''

