'''
문3) weatherAUS.csv 데이터셋을 이용하여 빈도수와 차트를 그리시오.
    <조건1> 지역(Location)별 빈도수 구하기
    <조건2> 지역(Location) 기준으로  오늘비(RainToday) 유무로 그룹화
    <조건3> 그룹화 결과를 대상으로 테이블 형식으로 변경 
    <조건4> No 칼럼 기준 내림차순 정렬  후 상위 10개 지역 누적막대차트 시각화 
        힌트 : value_counts(),groupby(), 
          size().unstack(), sort_values, plot()이용 
'''
import pandas as pd
import matplotlib.pyplot as plt

