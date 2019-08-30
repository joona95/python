'''
Pandas 객체를 이용한 시각화
   형식) obj.plot(param); plt.show() 
  obj : Series, DataFrame
''' 

from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. Series 객체 시각화 
ser = Series(np.random.randn(10),
             index = np.arange(0, 100, 10)) # 0~100, 10단위 
print(ser)

ser.plot(color = 'g')
plt.show()

# 2. DataFrame 객체 시각화 
df = DataFrame(np.random.randn(10, 4), 
               columns=['one', 'two', 'three', 'four'])
print(df)

# 기본 차트 
df.plot() # default = line
plt.show()

# 막대차트(세로막대) 
df.plot(kind='bar', title='bar chart plotting')
plt.show()
# 막대차트(가로막대) 
df.plot(kind='barh', title='bar chart plotting')
plt.show()


'''
tips.csv 파일 이용 
'''

tips = pd.read_csv('../data/tips.csv')
print(tips.info())
print(tips.head())

# 요일(day)과 파티규모(size) 범주 확인 
# print(tips['day'].unique()) # ['Sun' 'Sat' 'Thur' 'Fri']

# 요일(day)과 파티규모(size)의 교차테이블 
# 형식) pd.crosstab(행칼럼, 열칼럼)
party_table = pd.crosstab(tips['day'], tips['size']) # 행,열
print(party_table)
'''
size  1   2   3   4  5  6
day                      
Fri   1  16   1   1  0  0
Sat   2  53  18  13  1  0
Sun   0  39  15  18  3  1
Thur  1  48   4   5  1  3
'''

# label이 숫자라면 label-based index 적용 
party_result = party_table.ix[:, 2:5] # [row, col]
'''
size   2   3   4  5
day                
Fri   16   1   1  0
Sat   53  18  13  1
Sun   39  15  18  3
Thur  48   4   5  1
'''
print(party_result)

party_result.plot(kind = 'barh', stacked=True,
                  title = 'day and size plotting')
plt.show()

'''
dataset.csv
 - 특정 칼럼으로 산점도 시각화 
'''

dataset = pd.read_csv('../data/dataset.csv')
# print(dataset.info()) 
# print(dataset.head())
# print(dataset.tail())

data_col = dataset[ ['resident', 'gender','age', 'price'] ]
# print(data_col)

# 산점도 시각화 
plt.scatter(data_col['age'], data_col['price'])
plt.show()

'''
data.csv
 - 산점도 matrix 시각화 
'''

data = pd.read_csv('../data/data.csv')
# print(data.info())
# print(data.head())

data_result = data[['E', 'C', 'A']]
# print(data_result)

pd.scatter_matrix(data_result) # 산점도 matrix
plt.show()


iris = pd.read_csv('../data/iris.csv')
cols = list(iris.columns) # 칼럼 추출

col4 = iris[cols[:4]]
pd.scatter_matrix(col4)
plt.show()