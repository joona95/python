'''
날씨 데이터 처리와 시각화 
'''

import pandas as pd

# 날씨 데이터 가져오기 
weather = pd.read_csv('../data/weatherAUS.csv')
print(weather.info())
print(weather.head())
print(weather.tail())

# 특정 행 보기 
print(weather.ix[0]) # DF.ix[행] 

# 특정 칼럼 보기 
print(weather['MaxTemp'][:10])
print(weather['Rainfall'][:20])
print(weather['RainTomorrow'][:20])

# 3개 칼럼 보기 
col = ['MaxTemp','Rainfall','WindDir3pm']#최고기온,강수량,오후3시바람방향 
print(weather[col][:20])

# 오후3시바람방향(WindDir3pm) 빈도수 
WindDir3pm_count = weather['WindDir3pm'].value_counts()
print(WindDir3pm_count)

import matplotlib.pyplot as plt

WindDir3pm_count.plot(kind='bar', rot=45, title='WindDir3pm counts')
plt.show()


# 특정 칼럼으로 그룹화 
# 형식) DF.groupby(['그룹기준칼럼', '그룹대상컬럼'])

# # 돌풍방향을 기준으로 내일 비 유무 그룹화 
groupby = weather.groupby(['WindGustDir', 'RainTomorrow']) 
print(groupby) 
print(groupby.size()) # 빈도수    
   
# 테이블 형식 : [1:n] 
result = groupby.size().unstack()
print(result)
