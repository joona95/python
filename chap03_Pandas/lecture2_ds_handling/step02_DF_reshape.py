'''
Data Frame의 모양 변경
'''

from pandas import Series, DataFrame
import pandas as pd
import numpy as np

df = DataFrame(1000 + np.arange(6).reshape(2,3),
        index = ['대전시', '서울시'],
        columns = ['2015','2016','2017'] )
print(df)
print(df.shape) # (2, 3)
'''
     2015  2016  2017
대전시  1000  1001  1002
서울시  1003  1004  1005
'''

# 1. 1:N -> 1:1 변경
df_row = df.stack() # wide -> long
print(df_row)
print(df_row.shape) # (6,)
'''
대전시  2015    1000
     2016    1001
     2017    1002
서울시  2015    1003
     2016    1004
     2017    1005
'''

# 2. 1:1 -> 1:N 
df_col = df_row.unstack() # long -> wide
print(df_col)
'''
     2015  2016  2017
대전시  1000  1001  1002
서울시  1003  1004  1005
'''

# 3. 전치행렬
print(df_col.T)
'''
       대전시   서울시
2015  1000  1003
2016  1001  1004
2017  1002  1005
'''

# 4. 중복데이터 제거 
data = {'data1' : ['a']*4, 'data2' : [1,1,2,2]}
df2 = DataFrame(data)
print('df2 : ', df2)
'''
0     a      1
1     a      1
2     a      2
3     a      2
'''

result = df2.drop_duplicates()
print(result)
'''
0     a      1
2     a      2
'''


# 5. 특정 칼럼으로 index 지정
buy = pd.read_csv('../data/buy_data.csv')
print(buy.info())
'''
RangeIndex: 22 entries, 0 to 21
Data columns (total 3 columns):
Date           22 non-null int64
Customer_ID    22 non-null int64
Buy            22 non-null int64
'''

print(buy.head())
'''
       Date  Customer_ID  Buy
0  20150101            1    3
1  20150101            2    4
2  20150102            1    2
3  20150101            2    3
4  20150101            1    2
'''

# 'Date' 칼럼으로 index 지정
new_buy = buy.set_index('Date')
print(new_buy)

buy_0101 = new_buy.ix[20150101,:]
print(buy_0101)
'''
          Customer_ID  Buy
Date                      
20150101            1    3
20150101            2    4
20150101            2    3
20150101            1    2
'''

