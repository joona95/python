'''
kNN 알고리즘 정의 함수
'''

from lecture2_kNN.step01_kNN_data import data_set
import numpy as np 

know, not_know, cate = data_set()
print(know)
print(not_know)
print(cate)


# 유클리드안 거리 계산식 : 차 -> 제곱(**) -> 합(sum) -> 제곱근(sqrt)
def classify(know, not_know, cate, k): # k = 최근접한 점 중 k번째까지..?
    # 단계 1: 유클리드안 거리 계산식
    diff = know - not_know # 차
    sq_diff = diff ** 2
    sq_sum = sq_diff.sum(axis = 1) # 행 단위 합게
    distance = np.sqrt(sq_sum)
    
    # 단계 2: 가까운 거리 오름차순 정렬 -> index
    sortDist = distance.argsort() # sort -> index
    
    # 단계 3: 최근접 이웃(k=3)
    class_result = {} # 빈 set/dict
    
    for i in range(k) : # 0,1,2
        key = cate[sortDist[i]] # A A B B
        class_result[key] = class_result.get(key, 0) + 1
         
    
    return class_result

result = classify(know, not_know, cate, 3)
print(result)
# [0.47169906 0.61846584 0.20615528 0.40311289]
# [2 3 0 1]
# {'B': 2, 'A': 1}
