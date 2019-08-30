'''
DataFrame 자료구조 특징
 - 2차원 행렬구조 (DB의 table과 유사)
 - 칼럼 단위 상이한 자료형
 - DataFrame 구성 요소
   -> Series : 1차원(vector)
   -> numpy : n차원
'''

import pandas as pd # pd.DataFrame()
from pandas import DataFrame # DataFrame()

# 1. DataFrame 생성

# 1) list 이용
name = ['hong', 'lee', 'kang','yoo']
age = [35, 45, 55, 25]
pay = [350, 200, 400, 250]
addr = ['서울시', '부산시', '대전시', '인천시']

frame = pd.DataFrame({'name' : name, 'age' : age, 'pay' : pay, 'addr' : addr}, 
                     columns=['name', 'age', 'pay', 'addr'])
print(frame)
'''
   name  age  pay addr
0  hong   35  350  서울시
1   lee   45  200  부산시
2  kang   55  400  대전시
3   yoo   25  250  인천시
'''

# 2) dict 이용
d = {'name' : name, 'age' : age, 'pay' : pay, 'addr' : addr}
frame2 = DataFrame(d, index = ['a', 'b', 'c','d'],
                   columns=['name', 'age', 'pay', 'addr'])
print(frame2)
'''
   name  age  pay addr
a  hong   35  350  서울시
b   lee   45  200  부산시
c  kang   55  400  대전시
d   yoo   25  250  인천시
'''


# 2. Series 객체 -> DF 칼럼 추가
gender = pd.Series(['M', 'M', 'F', 'F'], index = ['a', 'b', 'c','d'])
frame2['gender'] = gender # 성별 칼럼 추가
print(frame2)
'''
   name  age  pay addr gender
a  hong   35  350  서울시      M
b   lee   45  200  부산시      M
c  kang   55  400  대전시      F
d   yoo   25  250  인천시      F
'''


# 3. numpy 객체 -> DF 객체
import numpy as np
frame3 = pd.DataFrame(np.arange(12).reshape(3,4), 
                      columns = ['a', 'b', 'c', 'd'])
print(frame3)
'''
   a  b   c   d
0  0  1   2   3
1  4  5   6   7
2  8  9  10  11
'''


# 4. index 지정
print(frame3.index)
print(frame3.columns)
'''
RangeIndex(start=0, stop=3, step=1)
Index(['a', 'b', 'c', 'd'], dtype='object')
'''

# 1) 특정 칼럼으로 index 지정
setIdx = frame3.set_index('a')
print(setIdx) # 해당 칼럼 제외
'''
   b   c   d
a           
0  1   2   3
4  5   6   7
8  9  10  11
'''

# 2) index 재지정
resetIdx = setIdx.reset_index() # default index : 0~n
print(resetIdx)
'''
   a  b   c   d
0  0  1   2   3
1  4  5   6   7
2  8  9  10  11
'''


# 5. DF 칼럼 참조

# 1) 단일 칼럼 참조
print(frame3.a) # obj.column
print(frame3['a']) # obj['column']
'''
0    0
1    4
2    8
'''
print(frame3['a'][2]) # obj['column'][n] : 8

# 2) 복수 참조
print(frame3[['a', 'c']])

cols = ['a', 'c']
print(frame3[cols])
'''
   a   c
0  0   2
1  4   6
2  8  10
'''

iris = pd.read_csv('../data/iris.csv')
print(iris.info())
'''
RangeIndex: 150 entries, 0 to 149
Data columns (total 5 columns):
Sepal.Length    150 non-null float64
Sepal.Width     150 non-null float64
Petal.Length    150 non-null float64
Petal.Width     150 non-null float64
Species         150 non-null object
'''

print(iris.columns)
iris_cols = list(iris.columns)
print(iris_cols)
# ['Sepal.Length', 'Sepal.Width', 'Petal.Length', 'Petal.Width', 'Species']

iris_x = iris_cols[:4]
iris_y = iris_cols[-1]
print(iris_x) # ['Sepal.Length', 'Sepal.Width', 'Petal.Length', 'Petal.Width']
print(iris_y) # Species

X = iris[iris_x] # [[4]]
Y = iris[iris_y]
print(X) # 150x4
print(Y) # 150


wdbc = pd.read_csv('../data/wdbc_data.csv')
print(wdbc.info())
'''
RangeIndex: 569 entries, 0 to 568
Data columns (total 32 columns):
'''

# Y:2(1), X:3~32(30)

cols = list(wdbc.columns)
col_x = cols[2:] # radius_mean ~
col_y = cols[1] # diagnosis

wdbc_x = wdbc[col_x] # [['col1', 'col2', ...]]
wdbc_y = wdbc[col_y] # ['diagnosis']

print(wdbc_x.shape) # (569, 30)
print(wdbc_y.shape) # (569,)


# 6. DF 행렬 참조 : df[row, column]
'''
ix 속성
 형식) DF.ix[행index or label, 열index or label]
 - DF를 대상으로 행과 열의 (숫자)index or (문자)label 이용 참조
 - 연속 데이터 참조 시 콜론(:) 사용 가능
 - label이 숫자이면 label-based index만 가능
      만약 열/행 이름이 숫자이면 숫자로 참조
'''

print(frame3)
'''
   a  b   c   d
0  0  1   2   3
1  4  5   6   7
2  8  9  10  11
'''

# 단일 행/열 참조
print(frame3.ix[1]) # 행 기본
print(frame3.ix[1, 2]) # 행, 열(index) 참조 - 6
print(frame3.ix[1, 'c']) # 행, 열(label) 참조 - 6

# 복수 행/열 참조(콜론)
print(frame3.ix[:,1:3])


# iris data random 선택
print(len(iris)) # 150 -> 105(70%)

# 1~10 -> 5개 선택
idx = np.random.choice(10, 5, replace = False) # 비복원 추출 : 비복원추출에서는 한 개체가 두 번 이상 뽑힐 수 없음
print(idx)# [4 1 6 7 9]

iris_idx = np.random.choice(len(iris), int(len(iris)*0.7), replace = False)
print(iris_idx)
print(len(iris_idx)) # 105

train_set = iris.ix[iris_idx, :]
print(train_set.head())
print(train_set.shape) # (105, 5)


# 칼럼 dummy값 생성
name = ['a', 'b', 'c', 'd', 'e']
gender = [1,2,1,2,3] # 1 -> 0('no'), 2 -> 1('yes'), other -> NA

df = pd.DataFrame({'name' : name, 'gender' : gender})
print(df)
'''
   gender name
0       1    a
1       2    b
2       1    c
3       2    d
4       3    e
'''

for idx in range(len(name)) : # 0~4
    if df.ix[idx,'gender'] == 1 :
        df.ix[idx,'gender'] = 0 # 수정
    elif df.ix[idx, 'gender'] == 2 :
        df.ix[idx,'gender'] = 1 # 수정
    else : # other
        df.ix[idx,'gender'] = np.nan # NA
        
print(df)
'''
   gender name
0     0.0    a
1     1.0    b
2     0.0    c
3     1.0    d
4     NaN    e
'''
