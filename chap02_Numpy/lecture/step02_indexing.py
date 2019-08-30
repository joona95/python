'''
numpy 객체 
 - indexing/slicing
 - 3차원 indexing
 - view/copy
 - boolean indexing
'''

import numpy as np 

# 1. indexing : 
'''
1차원 : obj[index]
2차원 : obj[행index, 열index]
3차원 : obj[면index, 행index, 열index]
'''
# list 객체 
ldata = [0,1,2,3,4,5]
print(ldata[3]) # 4번째 원소 - 3
print(ldata[:]) # 전체 원소 - [0, 1, 2, 3, 4, 5]
print(ldata[:3]) # 0 ~ n-1까지 - [0, 1, 2]

# np 객체 
arr= np.arange(10) # 0 ~ 9
print(arr[3]) 
print(arr[:]) 
print(arr[:3]) 
'''
list vs numpy 공통점
 - 1차원 배열에서 indexing 동일
 - 결과는 list 반환
'''


# 2. slicing

# list
li_sclicing = ldata[1:4] # [0,1,2,3,4,5]
print(li_sclicing) # [1, 2, 3]
li_sclicing[2] = 300 # 수정 
#li_sclicing[:] = 300 # 수정X
print(li_sclicing) # [1, 2, 300]

# np
arr_sclicing = arr[5:8] # 0 ~ 9
print(arr_sclicing) # [5 6 7]
arr_sclicing[:] = 500 # 전체 원소 수정 가능
print(arr_sclicing) # [500 500 500]
print(arr) 


# 3. 3차원 indexing
arr2d = np.array([ [1,2,3], [4,5,6], [7,8,9] ]) # 중첩list(2) 
print(arr2d) # 3행3열 

arr3d = np.array([ [[1,2,3], [4,5,6]], [[7,8,9], [10,11,12]] ]) # 중첩list(3) 
print(arr3d) # 2면2행3열
'''
[[[ 1  2  3]
  [ 4  5  6]]

 [[ 7  8  9]
  [10 11 12]]]
'''

# 면 접근 
print(arr3d[0]) 
'''
[[1 2 3]
 [4 5 6]]
 '''
# 면,행 접근 
print(arr3d[0,1]) 
'''
[4 5 6]
'''
# 면,행,열 접근 
print(arr3d[0,1,1]) 
'''
5
'''
print(arr3d[1,:,:2])
'''
[[ 7  8]
 [10 11]]
 '''



# 4. view & copy 

print(arr3d)
'''
[[[ 1  2  3]
  [ 4  5  6]]

 [[ 7  8  9]
  [10 11 12]]]
'''
# (1) view
print('(1) view ')
arr_view = arr3d[1] # 2면 복제(new object) 
print(arr_view) 
'''
[[ 7  8  9]
 [10 11 12]]
 '''
print(id(arr_view), id(arr3d)) # 주소 다름 

arr_view[:] = 1000 # 전체 수정 
print(arr_view) # 사본 수정
'''
[[1000 1000 1000]
 [1000 1000 1000]]
 ''' 
print(arr3d) # 원본 수정
'''
[[[   1    2    3]
  [   4    5    6]]

 [[1000 1000 1000]
  [1000 1000 1000]]]
'''

# (2) copy 
print('(2) copy ')
arr_copy = arr3d[0].copy() # 2면 복사(new object) 
print(arr_copy) 
'''
[[1 2 3]
 [4 5 6]]
 '''

arr_copy[:] = 1000 # 전체 수정 
print(arr_copy) 
'''
[[1000 1000 1000]
 [1000 1000 1000]]
 '''
print(arr3d) # 원본 : copy는 원본 수정 안됨 
'''
[[[   1    2    3]
  [   4    5    6]]

 [[1000 1000 1000]
  [1000 1000 1000]]]
'''

# 5. boolean indexing: data[조건식]

data = np.random.randn(3, 4) # 12개 
print(data)

# 부울리언 색인 
print(data[data >= 0.7]) # list 반환 

# 0.1 ~ 0.5
# print(data[data>=0.1 and data <= 0.5]) 실행안됨

re = data[np.logical_and(data>=0.1, data<=0.5)]
print('re=', re)
# re= [0.26106486 0.40365104 0.46998321 0.27007336]

'''
numpy 논리식 함수
np.logical_and()
np.logical_or()
np.logical_xor()
np.logical_not()
'''
