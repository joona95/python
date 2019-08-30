'''
교차검정(cross validation)
'''

import pandas as pd
from sklearn import model_selection # cross validation
from sklearn.ensemble import RandomForestClassifier # RM

iris = pd.read_csv('../data/iris.csv')
print(iris.head())

cols = list(iris.columns)

x_data = iris[cols[:4]] # 1~4칼럼
y_data = iris[cols[-1]] # 5번째 칼럼

# model 생성
rfc = RandomForestClassifier()
model = rfc.fit(x_data, y_data)


# 교차검정 : cv=5 (다섯개로 균등분할  30,30,30,30,30)
score = model_selection.cross_validate(model, x_data, y_data, cv=5)
print(score)
print(score['test_score'])
# [0.96666667 0.96666667 0.9        0.9        1.        ]

# 각 모델의 산술평균
print(score['test_score'].mean())
