'''
 문) 당료병(diabetes.csv) 데이터 셋을 이용하여 다음과 같이 DT 모델을 생성하시오.
 <조건1> 6:4비율 train/test 데이터 셋 구성 
 <조건2> y변수 : 9번째 칼럼, x변수 : 1 ~ 8번째 칼럼 

'''
import pandas as pd
from sklearn import model_selection
from sklearn.tree import DecisionTreeClassifier


# 당료병 데이터 셋 
dia = pd.read_csv('../data/diabetes.csv', header=None) # 제목 없음
print(dia.info()) 
'''
RangeIndex: 759 entries, 0 to 758
Data columns (total 9 columns):
'''
print(dia.head()) 

# <조건1> 6:4비율 train/test 데이터 셋 구성 
train_set, test_set = model_selection.train_test_split(dia, test_size = 0.4, random_state = 123)

# model 생성
dt = DecisionTreeClassifier()
model = dt.fit(train_set.ix[:,0:7],train_set.ix[:,8]) # <조건2> y변수 : 9번째 칼럼, x변수 : 1 ~ 8번째 칼럼 

# prediction 생성
pred = model.predict(test_set.ix[:,0:7])


# model 평가 : confusion matrix
mat = pd.crosstab(pred, test_set.ix[:,8])
print(mat)

print(55+169/len(test_set))
