'''
Anaconda Prompt
> conda install -c conda-forge scikit-surprise
'''

import surprise
import pandas as pd

# 1. data set load
ratings = pd.read_csv('../data/movie_rating.csv')
print(ratings) 
# critic(user)   title(movie)   rating(평점)


# 2. Reader -> Dataset 
from surprise import Reader, Dataset

reader = Reader(rating_scale=(1,5))
data = Dataset.load_from_df(ratings, reader)

trainset = data.build_full_trainset()
testset = trainset.build_testset()

# 3. model 생성 : train 이용
sdv = surprise.SVD()
model = sdv.fit(trainset) # model 생성

# 4. 예측치 생성
pred = model.test(testset)

# 5. model 평가
surprise.accuracy.rmse(pred) # 평균제곱근오차
surprise.accuracy.mae(pred) # 평균절대값오차
'''
RMSE: 0.5685
MAE:  0.4136
'''

# 6. Toby 사용자 미관람 영화 추천 예측
userid = 'Toby'
itemid = ['Just My','Lady','The Night']
actual_rating = 0

for item in itemid :
    print(model.predict(userid, item, actual_rating))
'''
user: Toby       item: Just My    r_ui = 0.00   est = 2.89   {'was_impossible': False}
user: Toby       item: Lady       r_ui = 0.00   est = 3.08   {'was_impossible': False}
user: Toby       item: The Night  r_ui = 0.00   est = 3.22   {'was_impossible': False}
'''

