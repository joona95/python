'''
Series 객체 특징
 - pandas 제공 1차원 자료구조 (2차원 불가하므로 중첩리스트 사용 불가)
 - DataFrame의 칼럼 구성요소
 - numpy 공통점
   -> 수학/통계 함수
   -> 범위 수정, 블록 연산
   -> indexing/slicing 기능
   -> DataFrame 칼럼 구성
'''
 
import pandas as pd # pd.Series()
from pandas import Series # Series()
import numpy as np

# 1. Series 특징

# 1) list 이용
price = Series([4000, 3000, 3500, 2000])
print(price)
'''
0    4000
1    3000
2    3500
3    2000
'''
print(price.index)
print(price.values)
'''
RangeIndex(start=0, stop=4, step=1)
[4000 3000 3500 2000]
'''
print(price[1]) # 3000

# index 적용
fruit = pd.Series([4000, 3000, 3500, 2000], 
                  index = ['apple', 'melon', 'orange', 'kiwi'])
print(fruit)
'''
apple     4000
melon     3000
orange    3500
kiwi      2000
'''
print(fruit['melon']) # 3000

# boolean 조건식
print(fruit[fruit >= 3000])
'''
apple     4000
melon     3000
orange    3500
'''

# 2) dict 이용 : key = index, value = value
person = pd.Series({'name' : '홍길동', 'age' : 35, 'addr' : '서울시'})
print(person)
'''
addr    서울시
age      35
name    홍길동
'''
print(person['name']) # 홍길동


# 2. indexing : list 동일
ser = pd.Series([4, 4.5, 6, 8, 10.5])
print(ser[0]) # 4.0
print(ser[:3])
'''
0    4.0
1    4.5
2    6.0
'''
print(ser[3:])
'''
3     8.0
4    10.5
'''
print(ser[:])
'''
0     4.0
1     4.5
2     6.0
3     8.0
4    10.5
'''


# 3. Series 결합과 NA(결측치) 처리
fruit2 = pd.Series([4000, None, 3500, 2000], 
                  index = ['apple', 'melon', 'orange', 'kiwi'])

fruit3 = pd.Series([4000, 3000, 3500, 2000], 
                  index = ['apple', 'orange', 'kiwi', 'melon'])

# Series 결합(join) : index 기준
result = fruit2 + fruit3
print(result)
'''
apple     8000.0
kiwi      5500.0
melon        NaN -> 결측치
orange    6500.0
'''

# NA 처리 (평균, 0)
result2 = result.fillna(result.mean())
print(result2)
'''
apple     8000.000000
kiwi      5500.000000
melon     6666.666667
orange    6500.000000
'''

result3 = result.fillna(0)
print(result3)
'''
apple     8000.0
kiwi      5500.0
melon        0.0
orange    6500.0
'''

# NA 제외 subset 생성
# pd.isnull(obj)
# pd.notnull(obj)

print(pd.notnull(result))
'''
apple      True
kiwi       True
melon     False
orange     True
'''

subset = result[pd.notnull(result)]
print(subset)
'''
apple     8000.0
kiwi      5500.0
orange    6500.0
'''


# 4. Series vs numpy 공통점
print(ser)
'''
0     4.0
1     4.5
2     6.0
3     8.0
4    10.5
'''

# 1) 블럭 수정, 부분 수정
ser[1:4] = 50
print(ser)
'''
0     4.0
1    50.0
2    50.0
3    50.0
4    10.5
'''

# 2) 수학/통계 함수
print(ser.mean()) # 32.9
print(ser.sum()) # 164.5
print(ser.max()) # 50.0

# 3) 블럭 연산, 브로드캐스트 연산
print(ser * 0.5)
'''
0     2.00
1    25.00
2    25.00
3    25.00
4     5.25
'''
