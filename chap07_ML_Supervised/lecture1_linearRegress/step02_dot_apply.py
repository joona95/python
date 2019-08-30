'''
회귀모형 예측에 행렬곱 함수(dot) 적용 예
'''

import pandas as pd
import numpy as np

# 1. data set 가져오기
score = pd.read_csv('../data/score_iq.csv')
print(score.info())

# 2. 3개 변수 subset 생성
score_arr = np.array(score[['score', 'iq', 'academy']])
print(score_arr)
print(score_arr.shape) # (150, 3)

# 3. X, Y변수 생성
score_X = score_arr[:, 1:] # iq, academy
score_Y = score_arr[:, 0] # score[정답, 관측치]
print(score_X.shape) # 2차원 : (150, 2)
print(score_Y.shape) # 1차원 : (150,)

# 4. 기울기와 절편 변수
'''
Intercept    25.229141 : y절편
iq            0.376966 : x1 기울기
academy       2.992800 : x2 기울기
'''
slope = np.array([[0.376966],[2.992800]])
print(slope.shape) # (2, 1)
intercept = 25.229141

# 5. 행렬곱(dot) 적용

matmul = np.dot(score_X, slope) # (150, 2) * (2, 1) = (150, 1)
print(matmul.shape) # (150, 1)

# Y = Xa + b
fitted_value = matmul + intercept # 예측치
print(fitted_value.shape) # (150, 1)

# 6. model 평가(정답 = 예측치)

# 예측치 1차원
fitted_value1d = fitted_value.reshape(150)
print(fitted_value1d.shape) # (150,)

# 상관계수 평가 : pandas
df = pd.DataFrame({'fitted' : fitted_value1d, 'Y' : score_Y})
corr = df.fitted.corr(df.Y)
print('corr=', corr)
# corr= 0.9727792069594755

print(df.fitted[:5]) # 예측치
print(df.Y[:5])