'''  lecture2 관련 문제  
문4) iris.csv 파일을 읽어와서 다음과 같이 처리하시오.
   조건1> 1~4 칼럼 대상 vector 생성(col1, col2, col3, col4)    
   조건2> 각 칼럼 대상 합계, 평균, 표준편차 구하기 
   조건3> 1,2 칼럼과 3,4 칼럼을 대상으로 각 df1, df2 데이터프레임 생성
   조건4> df1과 df2 칼럼 단위 결합 iris_df 데이터프레임 생성      
'''

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

col1 = iris.ix[:,0] # 열 index 이용
col2 = iris['Sepal.Width'] # column 명 이용
col3 = iris['Petal.Length']
col4 = iris['Petal.Width']