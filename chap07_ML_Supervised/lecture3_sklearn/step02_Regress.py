'''
Created on 2018. 8. 11.

@author: user
'''

from sklearn.model_selection import train_test_split # train/test set
from sklearn.linear_model import LinearRegression # model 생성
from sklearn.metrics import mean_squared_error # MSE
import pandas as pd


#################################
### iris.csv file
#################################

iris = pd.read_csv('../data/iris.csv')
print(iris.info())
cols = list(iris.columns)

iris_df = iris[cols[:4]] # 1~4칼럼 선택
print(iris_df.head())

# 7:3비율 train/test set 생성
train_set, test_set = train_test_split(iris_df, test_size = 0.3, random_state=123)

print(train_set.shape) # (105, 4)
print(test_set.shape) # (45, 4)

# model 생성 : train set 이용
# x(2~4) -> y(1)

#print(train_set)
cols = list(train_set.columns)
iris_x = train_set[cols[1:]]
iris_y = train_set[cols[0]]
print(iris_x)
print(iris_y)

# 회귀 모델 생성
model = LinearRegression()
iris_model = model.fit(iris_x, iris_y)

print('회귀 계수 = ', iris_model.coef_) # 기울기
# 회귀 계수 =  [ 0.63924286  0.75744562 -0.68796484]


# 회귀 예측치 생성 : test set 이용
iris_x = test_set[cols[1:]]
iris_y = test_set[cols[0]]

pred = iris_model.predict(iris_x) # 예측치
Y = iris_y # 정답

# 회귀모델 평가(MSE)
import numpy as np
mse = np.mean((pred - Y)**2)
print("MSE = ", mse) # 평균적 오차
# MSE =  0.11633863200224717

mse2 = mean_squared_error(Y, pred)
print("MSE2 = ", mse2)
# MSE2 =  0.11633863200224713

print(pred[:5])
print(Y[:5])
'''
[6.13857983 6.49988973 6.37898923 5.98983773 5.15383808]
72     6.3
112    6.8
132    6.4
88     5.6
37     4.9
'''


# 회귀모델 평가(CORR)
df = pd.DataFrame({'Y' : Y, 'pred' : pred})
corr = df['Y'].corr(df['pred'])
print("상관계수 : ",corr)
# 상관계수 :  0.9251592254176362



#########################
## load_iris()
#########################
from sklearn.datasets import load_iris

iris = load_iris()
iris_x = iris.data # 1~4개 칼럼
iris_y = iris.target # 5번째 칼럼
print(iris_x)
print(iris_y)


'''
다중선형회귀모델 : x(4) -> y(1)
'''

# 7:3비율 (train/test)
x_train, x_test, y_train, y_test = train_test_split(
    iris_x, iris_y, test_size = 0.3, random_state = 123)

model = LinearRegression()
iris_model = model.fit(x_train, y_train) # train set

# model 예측치 생성
pred = iris_model.predict(x_test) # test set
Y = y_test

# model 평가
MSE = np.mean((Y - pred)**2)
print('MSE = ',MSE)

# CORR
df = pd.DataFrame({'pred':pred, 'Y':Y})
corr = df['pred'].corr(df['Y'])
print("CORR = ", corr)

'''
MSE =  0.04447086315865546
CORR =  0.9765335510463404
'''