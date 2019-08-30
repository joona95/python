'''
1. axis : 행축, 열축 
2. dot() : 행렬곱 
3. ANN에서 행렬곱 
   - 은닉층(h) = 입력(x) * 가중치(w)
'''

import numpy as np

# 1. 축(axis) : ppt. 56
# 행축 : 동일한 열들의 모음(열 단위)
# 열축 : 동일한 행들의 모음(행 단위)

arr = np.arange(1,21).reshape(5, 4) # (5x4)
print(arr)


print('축(axis) 연산')
print('행축 합계 :', arr.sum(axis=0)) 
print('열축 합계 :',arr.sum(axis=1)) 


# 2. np.dot(a, b) : ppt. 57 
a = np.array([[1, 1], [0, 1]]) 
b = np.array([[2, 3], [1, 5]]) 
print(a)
print(b)
'''
[[1 1]
 [0 1]]
[[2 3]
 [1 5]]
'''

print(a.shape, b.shape) # (2, 2) (2, 2)
# 1차원 행렬곱
c = np.dot(a, b) # 행렬 곱의 합 = (1*2) + (1*1) = 3
print('행렬곱 : \n', c)
'''
[[3 8]
 [1 5]]
'''

# 3. ann에서 행렬곱 : ppt. 60 

# 1) x(1,2) * w(2,2) = h(1,2) -> h(x(r), w(c))
x = np.array([0.1, 0.2]) # 1차원
w = np.array([[1,2], [2,3]]) # 2차원

# 차원보기 
print(np.ndim(x), np.ndim(w)) # 1 2
# 모양보기 
print(x.shape, w.shape) # 1차원 : (2,) -> (1,2), 2차원 : (2, 2)

# 행렬곱(행렬 내적)
h = np.dot(x, w)
print('h=', h) # h=[0.5 0.8]
print(h.shape) # (2,) -> (1,2)


# 2) x(2,2) * w(2,3) = h(2,3)
x2 = np.array([[0.1, 0.2],[0.3,0.4]]) # x2(2,2)
w2 = np.array([[1,2,3],[2,3,4]]) # w2(2,3)

h2 = np.dot(x2, w2)
print('hidden node = \n',h2)
'''
 [[0.5 0.8 1.1]
 [1.1 1.8 2.5]]
'''
print(h2.shape) # (2, 3)

# 주의 : 행렬곱 연산 시 수일치 필요(x 칼럼수 = w 행수)



