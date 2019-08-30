'''
sklearn 제공 dataset
'''

from sklearn import datasets
import numpy as np

# 1. 선형회귀분석에 적합한 dataset 

# 1) iris
iris = datasets.load_iris()
print(iris) # x, y

iris_x = iris.data # 4개 변수(독립변수, 설명변수)
iris_y = iris.target # 1개 변수(종속변수, 반응변수)

# <class 'numpy.ndarray'>
print(type(iris_x))
print(np.shape(iris_x)) # (150, 4) : 2차원
print(np.shape(iris_y)) # (150,) : 1차원


# 2) 당뇨병
diabetes = datasets.load_diabetes()
print(diabetes)

# 3) boston
boston = datasets.load_boston()
print(boston)


# 2. 분류분석에 적합한 dataset

# 4) wine
wine = datasets.load_wine()
print(wine)

# 5) breast cancer
cancer = datasets.load_breast_cancer()
print(cancer)