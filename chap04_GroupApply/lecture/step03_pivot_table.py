'''
피벗테이블(pivot table) 
  - DF 객체를 대상으로 행과 열 그리고 교차 셀에 표시될 칼럼을 지정하여 만들어진 테이블 
   형식) pivot_table(DF, values='교차셀 칼럼',
                index = '행 칼럼', columns = '열 칼럼'
                ,aggFunc = '교차셀에 적용될 함수')   
        
'''

import pandas as pd

# file 가져오기 
pivot_data = pd.read_csv('../data/pivot_data.csv')
print(pivot_data.info())
print(pivot_data) 

# 교차 셀 : 매출액(price)
# 행 : 년도(year), 분기(quarter) 
# 열 : 매출규모(size)
# 셀에 적용할 함수 : sum

pivot_result = pd.pivot_table(pivot_data, 
                           values='price',
                           index=['year', 'quarter'],
                           columns='size', 
                           aggfunc= 'sum')
# 피벗테이블 출력 
print(pivot_result)  

import matplotlib.pyplot as plt
pivot_result.plot(kind='barh', stacked= True) # 누적형 막대그래프
plt.show()


# 행 : 평가자, 열:영화제목, 교차셀:영화평점(sum)
movie_rating = pd.read_csv('../data/movie_rating.csv')
print(movie_rating.info())
'''
RangeIndex: 31 entries, 0 to 30
Data columns (total 3 columns):
critic    31 non-null object
title     31 non-null object
rating    31 non-null float64
'''
movie_table = pd.pivot_table(movie_rating,
               index='critic',
               columns='title',
               values='rating',
               aggfunc='sum')

print(movie_table)
'''
title    Just My  Lady  Snakes  Superman  The Night  You Me
critic                                                     
Claudia      3.0   NaN     3.5       4.0        4.5     2.5
Gene         1.5   3.0     3.5       5.0        3.0     3.5
Jack         NaN   3.0     4.0       5.0        3.0     3.5
Lisa         3.0   2.5     3.5       3.5        3.0     2.5
Mick         2.0   3.0     4.0       3.0        3.0     2.0
Toby         NaN   NaN     4.5       4.0        NaN     1.0
'''

# 영화별 평점의 합계
print(movie_table.sum(axis=0)) # 열 단위 함계
# 평가자별 평점의 합계 
print(movie_table.sum(axis=1)) # 행 단위 함계

