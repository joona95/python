'''
numpy 함수 이용 k Mean 알고리즘 구현 
'''

from numpy import *
import matplotlib.pyplot as plt

# data set 생성 함수
def loadDataSet(fileName):      
    dataMat = []                
    fr = open(fileName)
    for line in fr.readlines():
        curLine = line.strip().split('\t')        
        
        blankList = [] # 빈 list
        for data in curLine :        
            # float casting -> list append      
            fltCasting = float(data)
            blankList.append(fltCasting)      
            
        dataMat.append(blankList) 
    return dataMat

# data set 생성 
dataSet = mat(loadDataSet('../data/testSet.txt'))
print(dataSet); print(type(dataSet))

# 유클리드안 거리 계산 함수 
def distEclud(vecA, vecB):
    return sqrt(sum(power(vecA - vecB, 2))) 

# # cluster 중심 생성 함수 
def randCent(dataSet, k):
    n = shape(dataSet)[1] # data set column 수 
    centroids = mat(zeros((k,n)))#create centroid mat->(2,2)
     
    # cluster 중심 생성 : random으로 군집의 중심 생성 
    for j in range(n):
        minJ = min(dataSet[:,j]) 
        rangeJ = float(max(dataSet[:,j]) - minJ)
        r = random.rand(k,1) 
        centroids[:,j] = mat(minJ + rangeJ * r)
         
    return centroids

'''     
centroids = randCent(dataSet, 4) # k=4 : 군집수 
 
# 초기 random cluster centroid 산점도 그리기 
x_data = [x[:,0] for x in dataSet] # 첫번째 칼럼 전체 
y_data = [x[:,1] for x in dataSet] # 두번째 칼럼 전체 
 
flg = plt.figure() # 차트 플롯 생성 
chart = flg.add_subplot(1,1,1) # 행,열,위치
chart.scatter(x_data, y_data, c='b')
 
x_cent = [x[:,0] for x in centroids] # 첫번째 칼럼 전체 
y_cent = [x[:,1] for x in centroids] # 두번째 칼럼 전체 
chart.scatter(x_cent, y_cent, c='r')    
plt.show()
'''

# k 평균 군집화 알고리즘 
def kMeans(dataSet, k):    
    m = shape(dataSet)[0] # 80    
    # data point의 centroid를 저장을 위한 mat 생성 
    clusterAssment = mat(zeros((m, 2))) # (80, 2)
    centroids = randCent(dataSet, k) # cluster 중심 생성(0~3)
    clusterChanged = True
    
    while clusterChanged:
        clusterChanged = False
        # 각 점을 가장 가까운 중심에 assign 
        for i in range(m):
            minDist = inf; minIndex = -1
            for j in range(k):
                # cluster 중심과 모든 point와 거리 계산 
                distJI = distEclud(centroids[j,:], dataSet[i,:])
                # 가장 거리가 가까운 값으로 minDist, minIndex 수정     
                if distJI < minDist:
                    minDist = distJI
                    minIndex = j

            # i번째행의 첫번째 칼럼과 minIndex가 다르면 반복              
            if clusterAssment[i,0] != minIndex : 
                clusterChanged = True 
                
            # cluster의 centroid 저장 : [minIndex, 최소거리제곱]    
            clusterAssment[i, :] = minIndex, minDist**2
        
        # cluster 중심 다시 계산         
        for center in range(k): # 0 ~ 3
            # 현재 cluster의 모든 point data 가져오기
            ptsInClust = dataSet[nonzero(clusterAssment[:,0]==center)[0]]
    
            centroids[center,:] = mean(ptsInClust, axis=0) 
    return centroids, clusterAssment

centroids, clusterAssment = kMeans(dataSet, 4) # k=4 : k 중심 생성  


# k 평균 군집화 cluster 산점도 그리기
flg = plt.figure() # 차트 플롯 생성 
chart = flg.add_subplot(1,1,1) # 행,열,위치 
 
x_data = [x[:,0] for x in dataSet] # 첫번째 칼럼 전체 
y_data = [x[:,1] for x in dataSet] # 두번째 칼럼 전체 
chart.scatter(x_data, y_data, c='b')

x_cent = [x[:,0] for x in centroids] # 첫번째 칼럼 전체 
y_cent = [x[:,1] for x in centroids] # 두번째 칼럼 전체 
chart.scatter(x_cent, y_cent, c='r')    
plt.show()


####################################
# k=4인 경우 dataSet 4개 영역 구분 
####################################
# clusterAssment의 첫번째 칼럼 이용 

k = 4
flg = plt.figure() # 차트 플롯 생성 
chart = flg.add_subplot(1,1,1) # 행,열,위치
colors = ['r', 'g', 'b', 'purple']

for idx in range(k) :
    temp = dataSet[nonzero(clusterAssment[:,0]== idx)[0]]
    
    x_cent = [x[:,0] for x in temp] # 첫번째 칼럼 전체 
    y_cent = [x[:,1] for x in temp] # 두번째 칼럼 전체 
    chart.scatter(x_cent, y_cent, c=colors[idx])    

plt.show() 