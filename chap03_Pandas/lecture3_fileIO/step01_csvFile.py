'''
기본 파일 입출력 
 1. read_csv()
 2. read_table()
 3. 파일 저장 
'''

import pandas as pd; # 별칭 

# 1. read_csv()
emp_df = pd.read_csv('../data/emp.csv')
print(emp_df)
'''
    No Name  Pay
0  101  홍길동  150
1  102  이순신  450
2  103  강감찬  500
3  104  유관순  350
4  105  김유신  400
'''

# 칼럼명이 없는 경우 
student_df = pd.read_csv('../data/student.csv', header = None)
print(student_df) # 0     1    2   3
'''
     0     1    2   3
0  101  hong  175  65
1  201   lee  185  85
2  301   kim  173  60
3  401  park  180  70
'''

# 칼럼명 지정하여 파일 읽기 
col_name = ['학번', '이름', '키', '몸무게']
student_df = pd.read_csv('../data/student.csv', names = col_name)
print(student_df) # 학번    이름    키  몸무게
'''
    학번    이름    키  몸무게
0  101  hong  175   65
1  201   lee  185   85
2  301   kim  173   60
3  401  park  180   70
'''


# 2. read_table()

# 1개 이상 공백 구분자 
student_txt = pd.read_table('../data/student.txt', sep="\s+")  # sep="\s+" : 1칸 이상의 공백으로 separate된다
print(student_txt)

student_txt2 = pd.read_table('../data/student2.txt', sep="\s+")
print(student_txt2)
'''
    번호    이름    키 몸무게
0  101  hong  175  65
1  201   lee  180  85
2  301   kim  173   -
3  401  park    $  70
'''

# 특수문자 -> NaN 처리(NA) 
conv = {'키' : '$', '몸무게' : '-'}
student_txt3 = pd.read_table('../data/student2.txt', sep='\s+',
                             na_values = conv)
print(student_txt3)
'''
    번호    이름      키   몸무게
0  101  hong  175.0  65.0
1  201   lee  180.0  85.0
2  301   kim  173.0   NaN
3  401  park    NaN  70.0
'''
h = student_txt3['키']
w = student_txt3['몸무게']

print('키의 평균 =', h.mean())
print('가장 큰 키 =', h.max())
print('몸무게의 평균=', w.mean())
'''
키의 평균 = 176.0
가장 큰 키 = 180.0
몸무게의 평균= 73.33333333333333
'''

height = h.mean()
weight = round(w.mean(), 2)

student_txt3['hmean'] = height
student_txt3['wmean'] = weight


# 3. 파일 저장 

# 파일 저장 
student_txt3.to_csv('../data/student_output.csv', index=None, na_rep='NaN',
                    encoding='utf-8')

student_df = pd.read_csv('../data/student_output.csv',
                         encoding='utf-8')
print(student_df)

