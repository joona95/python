'''
함수(function)
 - 내장함수, 사용자 정의함수
 1. 내장함수 : python 제공
 2. 사용자 정의 함수
  형식)
  def 함수명([인수]
        명령문
        명령문
    [return 값]
 3. 축약함수(lambda)
  - 한줄 함수 의미
  형식)
  함수명 = lambda 인수 : return 값
'''

# 1. 내장함수
import statistics # 방법1
from statistics import mean # 방법2
from _operator import add
from audioop import avg
from math import sqrt

# 기본자료 list
dataset = [5, 9, 1, 7, 4, 6]

# 평균 계산
avg = statistics.mean(dataset) # 방법1
print('avg = ', avg)

avg2 = mean(dataset) # 방법2
print('avg2 = ', avg2)

#실행 : ctrl + F11


# 2. 사용자 정의 함수

# 예문 : 인수, 리턴이 있는 함수
def adder(x, y):  # 매개변수(가인수)
    add = x + y
    return add

# 함수 호출
add = adder(10, 20) # 실인수
print('add = ', add) # add = 30


# 분산, 표준편차 계산 함수
# 분산 = sum((변량-산술평균)**2) / n-1
# 표준편차 = 분산의 양의 제곱근

x = [5, 9, 1, 7, 4, 6]

def var_sd(x):
    diff = [] # 빈 list
    for v in x :
        diff.append((v - avg)**2)
    
    var = sum(diff) / (len(x)-1) # 분산
    sd = sqrt(var)
    
    return var, sd

var, sd = var_sd(x)
print('분산 =', var)
print('표준편차 = ', sd)

'''
분산 =7.466666666666666
표준편차 = 2.7325202042558927
'''

'''
list + for
형식) 변수 = [  실행문    for 변수  in 열거형객체     ]
 - 실행순서 : 1. for -> 2.실행문 -> 3.변수
'''

def var_sd2(x):
    
    diff = [(v-avg)**2 for v in x]
    
    '''
    diff = [] # 빈 list
    for v in x :
        diff.append((v - avg)**2)
    '''
    var = sum(diff) / (len(x)-1) # 분산
    sd = sqrt(var)
    
    return var, sd

var, sd = var_sd2(x)
print('분산 =', var)
print('표준편차 = ', sd)


# numpy : 선형대수 연산 적용
import numpy as np

def var_sd3(x):
    x_arr = np.array(x) # list -> numpy 형변환
    diff = (x_arr - avg)**2
    #diff = [(v-avg)**2 for v in x]
    '''
    diff = [] # 빈 list
    for v in x :
        diff.append((v - avg)**2)
    '''
    var = sum(diff) / (len(x)-1) # 분산
    sd = sqrt(var)
    
    return var, sd

var, sd = var_sd3(x)
print('var=',var)
print('sd=',sd)



# 3. 축약함수(lambda)
'''
def adder(x, y):  # 매개변수(가인수)
    add = x + y
    return add
'''

adder = lambda x, y :x + y
add = adder(10, 20)
print('add=',add)  # add = 30





