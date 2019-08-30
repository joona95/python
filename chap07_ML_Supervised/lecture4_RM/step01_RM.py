'''
Created on 2018. 8. 12.

@author: user
'''

import pandas as pd
import numpy as np

from sklearn.ensemble import RandomForestClassifier # RM object
from sklearn.model_selection import train_test_split # train/test set
from sklearn.datasets import load_wine # data set
from sklearn import metrics # 분류정확도, 평가 report


# 1. data set load
wine = load_wine()
wine_x = wine.data
wine_y = wine.target

print(np.shape(wine_x)) # (178, 13)
print(np.shape(wine_y)) # (178,)

# data 보기
print(wine_x[:5,:])
print(wine_y[:5]) # [0 0 0 0 0]
print(wine_y[170:175]) # [2 2 2 2 2]

# 2. 7:3 비율(train/test)

x_train, x_test, y_train, y_test = train_test_split(wine_x, wine_y, test_size = 0.3, random_state = 123)

# 3. RM model 
rfc = RandomForestClassifier()
model = rfc.fit(x_train, y_train)

# 4. 예측치
pred = model.predict(x_test)
Y = y_test

# 5. model 평가
con_max = pd.crosstab(pred, Y)
print(con_max)
'''
col_0   0   1   2
row_0            
0      17   1   0
1       0  19   0
2       0   1  16
'''

acc = (con_max.ix[0,0]+con_max.ix[1,1]+con_max.ix[2,2]) / len(y_test)
print("accuracy = ",acc) 



# 6. 평가 report 출력
acc2 = metrics.accuracy_score(Y, pred)
print("accuracy = ",acc2)

report = metrics.classification_report(Y, pred)
print('model report : ')
print(report)


###################################
## RM model tuning
###################################
#help(RandomForestClassifier)
'''
n_estimators : tree 수 (400~500)
min_samples_split : 변수 갯수 : np.sqrt(n)
'''
from math import sqrt

val_size = sqrt(13)
print(val_size)

# 3. RM model 
rfc = RandomForestClassifier(n_estimators=400, min_samples_split=3)
model = rfc.fit(x_train, y_train)

# 4. 예측치
pred = model.predict(x_test)
Y = y_test


# 5. 평가 report 출력
acc = (con_max.ix[0,0]+con_max.ix[1,1]+con_max.ix[2,2]) / len(y_test)
print("accuracy = ",acc) 

report = metrics.classification_report(Y, pred)
print('model report : ')
print(report)

