'''
NB vs SVM
'''

from sklearn import model_selection
from sklearn.naive_bayes import GaussianNB
from sklearn import svm
import pandas as pd
from sklearn.cross_validation import train_test_split

sms = pd.read_csv('../data/sms_spam_df.csv', encoding='ms949')
print(sms.info())
# RangeIndex: 5558 entries, 0 to 5557
print(sms.head(1))


# 7:3비율 - train/test
train_set, test_set = train_test_split(sms, test_size = 0.3, random_state = 123)
cols = list(sms.columns)

x_cols = train_set[cols[1:]] # terms
y_cols = train_set[cols[0]] # sms_type

# NB model
nb = GaussianNB()
model = nb.fit(x_cols, y_cols)

x_cols = test_set[cols[1:]] # terms
y_cols = test_set[cols[0]] # sms_type

pred = model.predict(x_cols)
nb_max = pd.crosstab(pred, y_cols)
print('NB 분류정확도')
print(nb_max)

acc = (nb_max.ix[0,0]+nb_max.ix[1,1])/len(test_set)
print("acc = ",acc)


# SVM model
x_cols = train_set[cols[1:]] # terms
y_cols = train_set[cols[0]] # sms_type

svm = svm.SVC(kernel = 'linear')
model = svm.fit(x_cols, y_cols)

x_cols = test_set[cols[1:]] # terms
y_cols = test_set[cols[0]] # sms_type

pred = model.predict(x_cols)
svm_max = pd.crosstab(pred, y_cols)
print("SVM 분류정확도")
print(svm_max)

acc=(svm_max.ix[0,0]+svm_max.ix[1,1])/len(test_set)
print("acc = ",acc)

'''
[1 rows x 6823 columns]
NB 분류정확도
sms_type   ham  spam
row_0               
ham       1167    26
spam       266   209
acc =  0.8249400479616307

SVM 분류정확도
sms_type   ham  spam
row_0               
ham       1431    37
spam         2   198
acc =  0.9766187050359713
'''