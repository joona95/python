'''
1. group 객체 요약통계량 구하기
2. group 객체 대상 외부함수 적용
 - agg(), apply()
3. data 정규화 
'''

import pandas as pd 

# 1. 그룹 객체 요약통계량

# tips.csv 파일 가져오기 
tips = pd.read_csv('../data/tips.csv')
print(tips.info())
print(tips.head())
print(tips.tail())

# 팁 비율 
tips['tip_pct'] = tips['tip'] / tips['total_bill']
print(tips.head())

# 칼럼명 복제
tips['gender'] = tips['sex']
print(tips.head())

# 칼럼 삭제
del tips['sex']
print(tips.head())


# 1) 그룹객체 생성 : 팁비율 칼럼 <- 성별,흡연자 그룹화
print('tip_pct_group')
tip_pct_group = tips['tip_pct'].groupby([tips['gender'], tips['smoker']]) 
#tip_pct_group = tips['tip_pct'].groupby([tips['gender', 'smoker']]) 
print(tip_pct_group) # 객체 정보 
print(tip_pct_group.size())
'''
sex     smoker
Female  No        54
        Yes       33
Male    No        97
        Yes       60
'''

# 2) 요약통계량
result = tip_pct_group.describe() 
print(result)

print(tip_pct_group.sum()) #long
print(tip_pct_group.sum().unstack()) #long -> wide
print(tip_pct_group.mean()) 


# 2. 그룹 객체 대상 외부함수 적용 

# 1) 내장함수 적용 

# print(tip_pct_group.agg('sum'))
# # tip_pct_group.sum()
# print(tip_pct_group.agg('mean'))
# print(tip_pct_group.agg('max'))
# print(tip_pct_group.agg('var'))


result2 = tip_pct_group.agg(['var','mean', 'max','min'])
print(result2)
'''
                    var      mean       max       min
gender smoker                                        
Female No      0.001327  0.156921  0.252672  0.056797
       Yes     0.005126  0.182150  0.416667  0.056433
Male   No      0.001751  0.160669  0.291990  0.071804
       Yes     0.008206  0.152771  0.710345  0.035638
'''


import matplotlib.pyplot as plt
result2.plot(kind = 'barh', 
             title='agg Function result', stacked=True)
plt.show()

# 2) 사용자 함수 적용
print(tip_pct_group.apply(sum))


# 3. data 정규화 : 다양한 특징은 갖는 값을 일정한 범위로 맞추는 작업 
from numpy import min, max # 주의 : numpy 임포트

# 사용자 함수 : 0 ~ 1 사이 정규화 
def normal(x):
    n = (x - min(x)) / (max(x) - min(x))
    return(n)

# 1차원 data 정규화 : 함수 호출 
x = [10, 20005, -100, 0]
print(normal(x)) # 함수 호출 
# [ 0.00547128  1.          0.          0.00497389]

x = pd.Series([10, 20005, -100, 0])
print(normal(x))

# 2차원 data 정규화  : apply 함수 
xy_df = pd.DataFrame({'x':x, 'y': [1,2,3,4]})
df_normal = xy_df.apply(normal)
print(df_normal)
'''
          x         y
0  0.005471  0.000000 
1  1.000000  0.333333
2  0.000000  0.666667
3  0.004974  1.000000
'''

# [응용] iris 데이터 적용 
iris = pd.read_csv('../data/iris.csv')
cols = list(iris.columns)
x_cols = cols[:4]

iris2 = iris[x_cols]
print('data_df2')
print(iris2)

# 정규화 
print('iris 정규화')
iris2_nor = iris2.apply(normal)
print(iris2_nor)


# 전체 칼럼을 Species 칼럼으로 그룹화
iris_g = iris.groupby('Species')

# agg() : 다수 함수 적용
iris_summ = iris_g.agg(['var','mean', 'max','min', ]) # ['내장함수']
print(iris_summ)
'''
           Sepal.Length                  Sepal.Width                   \
                    var   mean  max  min         var   mean  max  min   
Species                                                                 
setosa         0.124249  5.006  5.8  4.3    0.143690  3.428  4.4  2.3   
versicolor     0.266433  5.936  7.0  4.9    0.098469  2.770  3.4  2.0   
virginica      0.404343  6.588  7.9  4.9    0.104004  2.974  3.8  2.2   

           Petal.Length                  Petal.Width                   
                    var   mean  max  min         var   mean  max  min  
Species                                                                
setosa         0.030159  1.462  1.9  1.0    0.011106  0.246  0.6  0.1  
versicolor     0.220816  4.260  5.1  3.0    0.039106  1.326  1.8  1.0  
virginica      0.304588  5.552  6.9  4.5    0.075433  2.026  2.5  1.4  
'''

# apply() : 하나의 함수 적용
iris_nor = iris2.apply(normal) # 1~4칼럼
print(iris.head())
print(iris_nor.head())

