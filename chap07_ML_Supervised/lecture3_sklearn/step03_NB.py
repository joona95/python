'''
관련 패키지 : scikit-learn
GaussianNB 함수 이용 
'''

import pandas as pd
from sklearn import model_selection
from sklearn.naive_bayes import GaussianNB

data = pd.read_csv('../data/iris.csv')
print(data.info())

print(data['Species'].value_counts())
'''
virginica     50
setosa        50
versicolor    50
'''


# 6:4 비율 train/test data set 구성 
train_set, test_set = model_selection.train_test_split(
     data, test_size=0.4, random_state=0) # seed값 

print(train_set.shape) # (90, 5)
print(test_set.shape) # (60, 5)
col = ['Sepal.Length', 'Sepal.Width','Petal.Length','Petal.Width'] 

# NB 모델 생성 
gnb = GaussianNB()
fit = gnb.fit(train_set[col], train_set['Species']) # fit(x-영향주는변수, y-영향받는변수)

# model 예측치 생성
pred = fit.predict(test_set[col])
print(pred) # ['virginica' 'versicolor' 'setosa']

# model 평가 : confusion matrix
con_mat = pd.crosstab(pred, test_set['Species']) # 교차 분할표
print(con_mat)
'''
Species     setosa  versicolor  virginica
row_0                                    
setosa          16           0          0
versicolor       0          23          4
virginica        0           0         17
'''

# 분류정확도
# acc = (16+23+17) / len(test_set)
acc = (con_mat.ix[0,0]+con_mat.ix[1,1]+con_mat.ix[2,2]) / len(test_set)
print('accuracy = ',acc)
# accuracy =  0.9333333333333333

