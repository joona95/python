'''
Decision Tree 함수 이용 
'''

import pandas as pd
from sklearn import model_selection
from sklearn.tree import DecisionTreeClassifier

data = pd.read_csv('../data/iris.csv')

# 6:4 비율 train/test data set 구성 
train_set, test_set = model_selection.train_test_split(
     data, test_size=0.4, random_state=0)

print(train_set.shape) # (90, 5)
print(test_set.shape) # (60, 5)
col = ['Sepal.Length', 'Sepal.Width','Petal.Length','Petal.Width'] # 복수 열 검색

# DT 모델 생성 
dt_model = DecisionTreeClassifier()
fit = dt_model.fit(train_set[col], train_set['Species'])

# model 예측치 
preds = fit.predict(test_set[col])

# 혼돈 matrix
print('DT 분류 결과')
con_mat=pd.crosstab(preds, test_set['Species'],
                       rownames=['예측치'], colnames=['관측치'])
print(con_mat)

