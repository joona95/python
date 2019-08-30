'''
문) Load_boston() 함수를 이용하여 보스턴 시 주택 가격 예측 회귀모델 생성
    조건1> train/test - 7:3비율
    조건2> y 변수 : boston.target
    조건3> x 변수 : boston.data
    조건4> 모델 평가 : MSE, corr
'''

from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd

# 1. data load
boston = load_boston()
print(boston)

x_boston = boston.data
y_boston = boston.target
print(np.shape(x_boston)) # (506, 13) : matrix
print(np.shape(y_boston)) # (506,) : vector

# 2. train/test set(7:3비율)
x_train, x_test, y_train, y_test = train_test_split(x_boston, y_boston, random_state =123)
print(x_train.shape) # (379, 13)
print(x_test.shape) # (127, 13)

# 3. model 생성
model = LinearRegression()
boston_model = model.fit(x_train, y_train)


# 4. prediction 생성
pred = boston_model.predict(x_test)
Y = y_test


# 5. model 평가(MSE, CORR)
MSE = np.mean((pred - Y)**2)
print("MSE = ",MSE)

df = pd.DataFrame({'pred':pred, 'Y':Y})
CORR = df['pred'].corr(df['Y'])
print("CORR = ",CORR)

'''
MSE =  24.753484525964748
CORR =  0.8307863370402285
'''

print(pred[:5])
print(Y[:5])
'''
[16.32374912 27.89137092 39.41392684 18.36901852 30.16392284]
[15.  26.6 45.4 20.8 34.9]
'''

