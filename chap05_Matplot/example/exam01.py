'''
문1) iris.csv 파일을 이용하여 다음과 같이 차트를 그리시오.
    <조건1> iris.csv 파일을 iris 변수명으로 가져온 후 파일 정보 보기
    <조건2> 1번 칼럼과 3번 칼럼을 대상으로 산점도 그래프 그리기
    <조건3> species 칼럼을 제외한 나머지 4개 칼럼으로 산점도 matrix 그리기
             힌트) pd.scatter_matrix(data)
    <조건4> 1번 칼럼과 3번 칼럼을 대상으로 산점도 그래프 그린 후  5번 칼럼으로 색상 적용 
'''

import pandas as pd
import matplotlib.pyplot as plt

