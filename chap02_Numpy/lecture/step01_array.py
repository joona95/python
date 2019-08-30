'''
Numpy 패키지
 - 선형대수(벡터, 행렬) 연산에 효과적인 함수 제공
 - list 차이점 : 다차원 배열, 처리속도 고속
 - n차원 배열 제공
 - 주요 함수
   -> random.randn() : 표준정규분포 난수 생성
   -> array() : n차원 배열 생성
   -> arange(n) : 0~n-1개 정수 생성(range함수 동일)
'''

import numpy as np # 별칭

# numpy 1차원 자료구조
ar = np.array([1,2,3]) # list -> array형 변환
print(ar) # [1 2 3]
print(type(ar)) # <class 'numpy.ndarray'>

ar = np.array([1, 'two', 3])
print(ar) # ['1' 'two' '3']
print(ar.shape) # 차원 모양 : (3,)


# numpy 2차원 자료구조
first = [[1,2,3], [4,5,6]]
print(first) # [[1, 2, 3], [4, 5, 6]]

ar2d = np.array([[1,2,3], [4,5,6]]) # 2행3열
print(ar2d) 
print(ar2d.shape) 
'''
[[1 2 3]
 [4 5 6]]
(2, 3)
'''


# 1. random.randn(row, column)
# help(np.random.randn)

data = np.random.randn(3, 4) # package.module.function()
print(data)
'''
[[-0.10050843  0.43774154  0.39567052 -0.73425792]
 [-1.57753986  0.1825018  -1.31111493  0.56315202]
 [ 1.39212965 -0.9878454   0.45149457 -1.00951152]]
'''
print(type(data)) # <class 'numpy.ndarray'>

# 1) 수학/통계 관련 함수 제공
# 평균/표준편차
print('평균=', data.mean())
print('표준편차=', data.std())
'''
평균= -0.49728730965866497  (자료많을수록 0에 가까운 숫자)
표준편차= 1.1491949002335384  (자료많을수록 1에 가까운 숫자)
'''

result = []
row = 0
for i in data : # 행 단위 넘김
    row += 1 # 카운터 변수
    print(row, '행 단위 평균 = ', i.mean())
    print(row, '행 단위 표준편차 = ', i.std())
    result.append(i.mean())

print(result)
# [0.4274881488743937, -0.43379640277117004, -0.3373434170793546]

# 2) 블록 연산
print(data + data) # 2배
print(data - data) # 0

#브로드캐스트 연산
print(data * 0.5)
print(data ** 0.5) # sqrt
print(np.sqrt(data)) #sqrt


# 2. array([list]) : 다차원 배열 생성

# 1) 단일 list - 1차원
lst1 = [3, 5.6, 4, 7, 8]
print(lst1)
arr1 = np.array(lst1)
print(arr1)
'''
[3, 5.6, 4, 7, 8]
[3.  5.6 4.  7.  8. ]
'''

# 유니버셜 함수(수학/통계 함수)
# print(lst1.mean()) #Error
print('평균:',arr1.mean()) # 5.5200000000000005
print('합계:',arr1.sum())
print('최댓값:',arr1.max())
print('최솟값',arr1.min())
print('분산',arr1.var())
print('표준편차',arr1.std())
'''
평균: 5.5200000000000005
합계: 27.6
최댓값: 8.0
최솟값 3.0
분산 3.4016000000000006
표준편차 1.8443427013437608
'''

x = [5, 9, 1, 7, 4, 6]
ar = np.array(x)
# 모집단에 대한 분산/표준편차
print(ar.var())
print(ar.std())
'''
6.222222222222221
2.494438257849294
'''

# 2) 이중 list - 2차원
lst2 = [[1,2,3,4,5], [6,7,8,9,10]]
arr2 = np.array(lst2)

print(arr2)
print(arr2.shape)
'''
  0열
[[ 1  2  3  4  5]  -> 0행
 [ 6  7  8  9 10]] -> 1행
(2, 5)
'''
print(arr2[1, 1]) # [행index, 열index] -> 7
print(arr2[:,1:4])
'''
[[2 3 4]
 [7 8 9]]
'''

# broadcast 연산(선형대수)
# - 작은 차원이 큰 차원으로 늘어남

# 1) scala(0차원) vs vector(1차원)
print(arr1 * 0.5)

# 2) scala(0) vs matrix(2)
print(arr2 * 0.5)

# 3) vector(1) vs matrix(2)
print(arr1.shape)
print(arr2.shape)
print(arr1 + arr2)
'''
(5,)
(2, 5)
[[ 4.   7.6  7.  11.  13. ]
 [ 9.  12.6 12.  16.  18. ]]
'''

# 3. arange(n)
zerr = np.zeros( (3, 5) ) # ( (r, c) )
print(zerr) # 0 행렬

cnt = 0
for i in range(3) : # 행 : 0~n-1 (0,1,2)
    for j in range(5) : # 열 : 0-n-1 (0,1,2,3,4)
        cnt += 1 # 카운터 변수
        zerr[i, j] = cnt
        
print(zerr)


cnt = 0
for i in np.arange(3) : # 행 : 0~n-1 (0,1,2)
    for j in np.arange(5) : # 열 : 0-n-1 (0,1,2,3,4)
        cnt += 1 # 카운터 변수
        zerr[i, j] = cnt
        
print(zerr)
'''
[[ 1.  2.  3.  4.  5.]
 [ 6.  7.  8.  9. 10.]
 [11. 12. 13. 14. 15.]]
'''        
