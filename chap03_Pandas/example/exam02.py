'''  lec1_ds.step02 관련 문제
문2) 다음 df를 대상으로 ix 속성을 이용하여 행과 열을 선택하시오.
   조건1> 1,3행 전체 선택    
   조건2> 1~4열 전체 선택 
   조건3> 1,3행 1,3,5열 선택
'''
import pandas as pd
import numpy as np

data = np.arange(1, 16).reshape(3,5) # 3x5
df = pd.DataFrame(data, index = ['one', 'two', 'three'],
                  columns = [1,2,3,4,5])
print(df)
