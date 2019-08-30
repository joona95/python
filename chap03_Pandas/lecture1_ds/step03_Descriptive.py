'''
1. DataFrame 요약통계량
2. 변수 간의 상관성 분석
'''

import pandas as pd

name = ['hong', 'lee', 'kang']
bonus = [50, 150, 200]
pay = [250, 350, 450]

frame = pd.DataFrame({'name':name, 'bonus':bonus, 'pay':pay}, columns = ['name','pay','bonus'])

print(frame)
'''
   name  pay  bonus
0  hong  250     50
1   lee  350    150
2  kang  450    200
'''


# 기술통계량 구하기
fsum = frame.sum() # axis = 0
print(fsum)
fsum = frame.sum(axis = 0) # 행축(열 단위)
print(fsum)
fsum = frame.sum(axis = 1) # 열축(행 단위)
print(fsum)

fvar = frame.var() # axis = 0
print(fvar)
'''
pay      10000.000000
bonus     5833.333333
'''

# 요약통계량 : summary
summ = frame.describe()
print(summ)

# 구조보기 : str()
product = pd.read_csv('../data/product.csv')
print(product.info())

# 내용보기 : head(), tail()
print(product.head())
print(product.tail())


#빈도수
a_count = product['a'].value_counts() # product.a
print(a_count) 
'''
3    126
4     64
2     37
1     30
5      7
'''

#unique
b_unique = product['b'].unique()
print(b_unique) # [4 3 2 5 1]


# 변수 간의 상관분석
cor = product.corr()
print(cor)

iris = pd.read_csv('../data/iris.csv')
print(iris.info())

# subset 생성
cols = list(iris.columns)
iris_df = iris[cols[:4]]
print(iris_df.corr())
'''
              Sepal.Length  Sepal.Width  Petal.Length  Petal.Width
Sepal.Length      1.000000    -0.117570      0.871754     0.817941
Sepal.Width      -0.117570     1.000000     -0.428440    -0.366126
Petal.Length      0.871754    -0.428440      1.000000     0.962865
Petal.Width       0.817941    -0.366126      0.962865     1.000000
'''


