'''
DataFrame 그룹화
 - DF 객체 대상 특정 칼럼으로 그룹화
 형식) DF.groupby('칼럼').수학통계함수()
 칼럼 : 범주형 변수(성별)
'''

from pandas import DataFrame

# dict -> DF 생성
data = { 'key' : ['a','a','b','a','b','b'],
         'data1' : [20,10,20,10,20,10],
         'data2' : [100,100,200,100,200,100]    
         }

data_df = DataFrame(data, columns=['key','data1','data2'])
print(data_df)
'''
  key  data1  data2
0   a     20    100
1   a     10    100
2   b     20    200
3   a     10    100
4   b     20    200
5   b     10    100
'''

# 1. DF 전체 칼럼 대상 1개 칼럼으로 그룹화
# 형식) DF.groupby('칼럼')
group = data_df.groupby('key')
print(group)

print(group.size())
'''
key
a    3
b    3
'''
print(group.sum())
'''     data1  data2
key              
a       40    300
b       50    500
'''
print(group.mean())
'''
         data1       data2
key                       
a    13.333333  100.000000
b    16.666667  166.666667
'''

# 2. DF 특정 칼럼 대상 1개 칼럼으로 그룹화
# 형식) DF['칼럼'].groupby(DF['칼럼'])
group2 = data_df['data1'].groupby(data_df['key'])
print(group2.size())
print(group2.mean())
'''
key
a    3
b    3
Name: data1, dtype: int64
key
a    13.333333
b    16.666667
Name: data1, dtype: float64
'''

# 3. DF 전체 칼럼 대상 2개 칼럼으로 그룹화
# 형식) DF.groupby(['칼럼1', '칼럼2']) # 1차 key(칼럼1), 2차 key(칼럼2)

group3 = data_df.groupby(['key', 'data1'])
print(group3.size())
'''
key  data1
a    10       2
     20       1
b    10       1
     20       2
dtype: int64
'''
print(type(group3.size())) 
# <class 'pandas.core.series.Series'>

# long -> wide
print(group3.size().unstack())
'''
data1  10  20
key          
a       2   1
b       1   2
'''
print(type(group3.size().unstack()))
# <class 'pandas.core.frame.DataFrame'>

print(group3.mean())
'''
           data2
key data1       
a   10       100
    20       100
b   10       100
    20       200
'''


# 4. iris 적용
import pandas as pd
iris = pd.read_csv('../data/iris.csv')
print(iris.info())
'''
RangeIndex: 150 entries, 0 to 149
Data columns (total 5 columns):
Sepal.Length    150 non-null float64
Sepal.Width     150 non-null float64
Petal.Length    150 non-null float64
Petal.Width     150 non-null float64
Species         150 non-null object
'''

# 1) 전체 칼럼 대상 Species 칼럼 그룹화

iris_g = iris.groupby('Species')
print(iris_g.size())
'''
Species
setosa        50
versicolor    50
virginica     50
'''

print(iris_g.mean())
'''
            Sepal.Length  Sepal.Width  Petal.Length  Petal.Width
Species                                                         
setosa             5.006        3.428         1.462        0.246
versicolor         5.936        2.770         4.260        1.326
virginica          6.588        2.974         5.552        2.026
'''


# 2) 2개 칼럼 대상 Species 칼럼 그룹화
iris_g2 = iris[['Sepal.Length', 'Petal.Length']].groupby(iris['Species'])
print(iris_g2.size())
print(iris_g2.mean())
'''
            Sepal.Length  Petal.Length
Species                               
setosa             5.006         1.462
versicolor         5.936         4.260
virginica          6.588         5.552
'''


