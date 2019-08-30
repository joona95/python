'''
문) weatherAUS.csv 파일을 시용하여 NB 모델을 생성하시오
  조건1> NaN 값을 가진 모든 row 삭제 
  조건2> 1,2,8,10,11,22,23 칼럼 제외 
  조건3> 7:3 비율 train/test 데이터셋 구성 
  조건4> formula 구성  = RainTomorrow ~ 나머지 변수(17)
'''
import pandas as pd

data = pd.read_csv('../data/weatherAUS.csv')
print(data.head())
print(data.info())

# NaN 값을 가진 모든 row 삭제
data=data.dropna()
print(data.head())

# 조건1> 1,2,8,10,11,22,23 칼럼 제외 
col = list(data.columns)
for i in [1,2,8,10,11,22,23] :
    col.remove(list(data.columns)[i-1])
print(col)

new_data = data[col]
print(new_data.head())

# 조건2> 7:3 비율 train/test 데이터셋 구성 
from sklearn import model_selection

train_set, test_set = model_selection.train_test_split(
new_data, test_size=0.3, random_state=0) # seed값 

# 조건3> formula 구성 = RainTomorrow ~ 나머지 변수
from sklearn.naive_bayes import GaussianNB
col_x = col.copy()
col_x.remove('RainTomorrow')
print(col_x)

gnb = GaussianNB()
fit = gnb.fit(train_set[col_x], train_set['RainTomorrow'])

preds = fit.predict(test_set[col_x]) # model 예측치 

# 혼돈 matrix
con_mat=pd.crosstab(preds, test_set['RainTomorrow'],
rownames=['예측치'], 
colnames=['관측치'])
print(con_mat)
print((con_mat.No[0]+con_mat.Yes[1])/len(test_set))

