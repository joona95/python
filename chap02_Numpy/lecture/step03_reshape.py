'''
 reshape :  
  - 1차원 배열을 여러 크기의 2차원 배열로 변환
  - 2차원 배열을 다른 크기로 변형
 T : 전치행렬(행렬변경) 
 swapaxes : 축 변경
 transpose : 축 번호 순서에 의해서 구조 변경 
'''

import numpy as np

# 1. reshape
lst = range(1,13) # # list 이용  (1~12)
arr2d = np.array(lst).reshape(3, 4)
print(arr2d)
'''
[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]]
'''

# 2. 전치행렬 
print('2차원 전치행렬')
print(arr2d.T)
'''
[[ 1  5  9]
 [ 2  6 10]
 [ 3  7 11]
 [ 4  8 12]]
'''

# 3. swapaxes 
print('축(axis) 변경 ')
# axis=0(행), axis=1(열)
print(arr2d.swapaxes(0,1))
'''
[[ 1  5  9]
 [ 2  6 10]
 [ 3  7 11]
 [ 4  8 12]]
'''

# 4. transpose
print('transpose - 2d') 
# 2차원 축 변형 : 전치행렬
print(arr2d.transpose())
'''
[[ 1  5  9]
 [ 2  6 10]
 [ 3  7 11]
 [ 4  8 12]]
'''

'''
1차원 : 효과없음
2차원 : 행,열 교환 - 전치행렬
n차원 : 축 순서에 의해서 구조변경
'''

arr3d = np.arange(1,25).reshape(4, 2, 3) # (면,행,열)
print(arr3d)
print(arr3d.shape)
'''
[[[ 1  2  3]
  [ 4  5  6]]

 [[ 7  8  9]
  [10 11 12]]

 [[13 14 15]
  [16 17 18]]

 [[19 20 21]
  [22 23 24]]]
(4, 2, 3)
'''

# 3차원 : default(2,1,0) 역순 구조변경 : (0,1,2) -> (2,1,0)

arr3d_def = arr3d.transpose()
print(arr3d_def)
print(arr3d_def.shape) # (4,2,3) -> (3,2,4)

# (0,1,2) -> 축순서 (2,0,1)
arr3d_user = arr3d.transpose(2,0,1)
print(arr3d_user)
print(arr3d_user.shape) # (4,2,3) -> (3,4,2)



