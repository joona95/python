'''
1. DataFrame 객체 생성 
2. json 데이터 처리 
3. excel 데이터 처리
'''

import pandas as pd # 패키지 임포트 
from pandas import DataFrame # class 임포트 


# 1. DataFrame 객체 생성
help(DataFrame)
# dict -> DataFrame 
# 형식) {'key' : ['value1', 'value2'] } -> DataFrame(column, 내용)

data = {'name' : ['홍길동', '이순신'], 'age' : [35, 45],
        'address' : ['한양시', '해남시'] }
print(data)

# DataFrame 객체 생성 
data_df = DataFrame(data, columns=['name', 'age', 'address'])
print(data_df.info())
print(data_df)


# 2. json 데이터 처리 

# 1) 간단한 json 형식 데이터 처리 
obj = """
{
   "name" : ["홍길동","유관순"],
   "age" : [35, 25],
   "gender" : ["남자","여자"],
   "address" : ["서울시", "충남시"]
}
"""

import json # json 데이터 -> dict 객체 

# (1)json -> dict
result = json.loads(obj)
print(result)
 
# (2) dict -> DataFrame 
result_df = DataFrame(result, columns=['name','age','gender','address'])
print(result_df)
print(result_df['name'])
print(result_df[['name', 'gender']])

# 3. excel 데이터 처리
ex = pd.ExcelFile('../data/student.xlsx')
print(ex)

result = ex.parse('student')
print(result)


