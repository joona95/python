from sklearn import model_selection
from sklearn import svm
import pandas as pd

data = pd.read_csv('../data/iris.csv')
print(data)

# 6:4 비율 train/test data set 구성 
train_set, test_set = model_selection.train_test_split(
     data, test_size=0.4, random_state=0)

print(train_set.shape) # (90, 5)
print(test_set.shape) # (60, 5)
col = ['Sepal.Length', 'Sepal.Width','Petal.Length','Petal.Width'] # 복수 열 검색

# svm model 생성  
clf = svm.SVC(kernel='linear')

fit = clf.fit(train_set[col], train_set['Species'])
                        
# model 예측치 
preds = fit.predict(test_set[col])
# 혼돈 matrix
con_mat=pd.crosstab(preds, test_set['Species'],  
                       rownames=['예측치'], colnames=['관측치'])
print(con_mat)

acc = ((con_mat.ix[0,0]+con_mat.ix[1,1]+con_mat.ix[2,2]) / len(test_set))
print("분류정확도 = ",acc)
# 분류정확도 =  0.9666666666666667


