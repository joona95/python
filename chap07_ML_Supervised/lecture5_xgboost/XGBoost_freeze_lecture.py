'''
big 콘테스트 data set
동파유무 분류를 위한 data set 
'''

import pandas as pd
from sklearn import model_selection
from sklearn import metrics

from xgboost import XGBClassifier # model 생성
from xgboost import plot_importance # 중요변수(x) 시각화

from matplotlib import pyplot
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)
import time 


# 정제된 data set 
freeze = pd.read_csv("../data/freeze_dataset.csv",encoding="MS949",thousands=',')
print(freeze.info())
'''
RangeIndex: 37089 entries, 0 to 37088
Data columns (total 95 columns):
'''

print('칼럼명 수정 : 공백 -> _')
freeze.columns = freeze.columns.str.replace(' ', '_')
print(freeze.info())
print(freeze.head())


###############################
## 1. 동파유무1,0 비율 맞추기
###############################
print(freeze['동파유무'].value_counts())
'''
동파유무 : 비율(불균형)
0.0    34130 : 동파=1
1.0     2959 : 동파=0
'''

# 동파유무에 따른 subset 생성 
freeze1 = freeze[freeze['동파유무']==1]
freeze0 = freeze[freeze['동파유무']==0]
print("동파1:",freeze1.shape) # 동파1: (2959, 95)
print("동파0:",freeze0.shape) # 동파0: (34130, 95)

# 동파1 vs 동파0 비율 맞추기(9:1 sampling)
freeze0_9, freeze0_1 = model_selection.train_test_split(
    freeze0, test_size=0.1)

print("refined0_9:",freeze0_9.shape) # (30717, 95)
print("refined0_1:",freeze0_1.shape) # (3413, 95)

# 동파1+동파0(10%) : rbind(2959, 3413)=6372
train = pd.concat([freeze1,freeze0_1]) 
print("refined shape:",train.shape) # (6372, 95)
#[해설] '동파1'과 '동파0'의 10%와 결합하여 비율 맞춤 

chktime=time.time()

##############################
## 2. 훈련/검정 데이터셋 생성
##############################
print("6:4 비율 샘플링")

# 학습용 : y 비율 균형 
train_set, test_set = model_selection.train_test_split(
    train, test_size=0.4)

# 검정용 : 학습용외 나머지[rbind(2549,30717)=33266]  
test_set = pd.concat([test_set, freeze0_9])
print('test_set shape')
print(test_set.shape) # (2549, 95)
print(freeze0_9.shape) # (30717, 95)

# 학습용 : 비율 균형 
print("train_set 사이즈:",train_set.shape) # (3823, 95)
print("최종 reference 사이즈:",test_set.shape) # (33266, 95)
# [해설] 균형 비율로 학습하여 모델 생성, 검정은 전체 data set  

cols=list(freeze.columns)
y_name=cols.pop(0) # 1칼럼 추출(제거) 
x_name=cols
print('y변수 : ', y_name) # y변수 :  동파유무
print("x변수 개수:",len(x_name)) # x변수 개수: 94

# XGBOOST
XGB = XGBClassifier()
# train data 이용 model 생성 
model = XGB.fit(train_set[x_name], train_set[y_name])
print('XGB model =',model) # refined_XGB= XGBClassifier()

# test data[train외 나머지] 이용 예측치 생성 
pred = model.predict(test_set[x_name]) # 검증데이터

# fscore 중요변수 확인 
fscore = model.get_booster().get_fscore()
print("fscore:",fscore) # {'1달전수도사용': 50, ...}
print('len =', len(fscore)) # len = 46


# 중요변수 시각화
plot_importance(model) # fscore 기준  내림차순 52변수 시각화 
pyplot.show()


# 혼돈매트릭스(confusion matrix) 
con_mat=pd.crosstab(pred, test_set[y_name],
                    rownames=["예측치"],
                    colnames=["관측치"])
#refConNp=np.array(con_mat)
print(con_mat)

print("="*60)
chktime=time.time()-chktime
print("실행시간 : ",chktime)

# 모델 평가 
acc = metrics.accuracy_score(test_set[y_name], pred)
print('분류정확도 =', acc)

report = metrics.classification_report(test_set[y_name], pred)
print('모델 평가 결과')
print(report)

