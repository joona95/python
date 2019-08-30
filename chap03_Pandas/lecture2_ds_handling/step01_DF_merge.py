'''
data frame 병합(합치기) 
'''

from pandas import DataFrame, Series
import pandas as pd

key1 = ['a','b','c','d','e']
key2 = ['e','a','c']

# range(n) : 0 ~ n-1 정수 = np.arange(n)
df1 = DataFrame({'id':key1, 'data1':range(5) })
df2 = DataFrame({'id':key2, 'data2':range(3) })

# id 칼럼 공통 포함
print(df1); print(df2)

# 1. id 칼럼으로 DF 병합
df_merge = pd.merge(df1, df2) # how='inner'
print(df_merge) # id 칼럼 기준
'''
   data1 id  data2
0      0  a      1
1      2  c      2
2      4  e      0
'''

df_outer = pd.merge(df1, df2, how='outer')
print(df_outer)
'''
   data1 id  data2
0      0  a    1.0
1      1  b    NaN
2      2  c    2.0
3      3  d    NaN
4      4  e    0.0
'''

# 2. Series 객체 병합
s1 = Series([1,3], index=['a','b'])
s2 = Series([5,6,7], index=['a','b','c'])
s3 = Series([11,13], index=['a','b'])

# 행 단위 결합 
result = pd.concat([s1, s2, s3], axis = 0) # 행 단위 결합 
print(result)
print(type(result)) # Series
'''
a     1
b     3
a     5
b     6
c     7
a    11
b    13
dtype: int64
<class 'pandas.core.series.Series'>
'''

# 열 단위 결합 : DF 생성 
result2 = pd.concat([s1, s2, s3], axis = 1) # 열 단위(index) 결합 
print(result2)
print(type(result2)) # DataFrame
'''
     0  1     2
a  1.0  5  11.0
b  3.0  6  13.0
c  NaN  7   NaN
<class 'pandas.core.frame.DataFrame'>
'''

# 3. DataFrame 객체 결합 

import numpy as np

df1 = DataFrame(np.arange(1, 7).reshape(3,2), index=['a','b','c'],
                columns=['one', 'two'])
df2 = DataFrame(3 + np.arange(4).reshape(2,2), index=['a','b'],
                columns=['three', 'four'])

print(df1); print(df2)


# 칼럼단위 df 붙이기
result3 = pd.concat([df1, df2], axis = 1) # 열 단위(index) 결합 
# print(result3)

