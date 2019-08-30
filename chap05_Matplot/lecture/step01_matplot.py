'''
matplotlib API 사용 차트 그리기
    형식) plt.plot(data); plt.show()
  1. 기본 차트 그리기
  2. 산점도 그리기
  3. 차트 플롯으로 여러 개 차트 그리기
  4. 차트 플롯으로 한 개 차트 그리기
'''

import matplotlib.pyplot as plt
# 차트에서 한글 지원
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)
# 음수 부호 지원
import matplotlib
matplotlib.rcParams['axes.unicode_minus'] = False


import numpy as np

help(plt.plot)
'''
plot(x, y)        # plot x and y using default line style and color
plot(x, y, 'bo')  # plot x and y using blue circle markers
plot(y)           # plot y using x as index array 0..N-1
plot(y, 'r+')     # ditto, but with red plusses
'''

# 1. 기본 차트 그리기
data = np.arange(10) # 0~9
plt.plot(data, 'r+') # 차트 생성
plt.show() # 차트 보이기

# 2. 산점도 그리기
data2 = np.random.randn(10)
plt.plot(data, data2, 'ro')
plt.show()

# 3. 차트 플롯으로 여러 개 차트 그리기
fig = plt.figure()
x1 = fig.add_subplot(2,2,1)
x2 = fig.add_subplot(2,2,2)
x3 = fig.add_subplot(2,2,3)
x4 = fig.add_subplot(2,2,4)

# data 생성
data3 = np.random.randint(1,100,100) # 난수 정수 생성
data4 = np.random.randint(10,110,100) # 난수 정수 생성

# 첫번째 영역
x1.hist(data3) # 히스토그램

# 두번째 영역
x2.scatter(data3, data4) # 산점도

# 세번째 영역
x3.plot(data3) # 직선 

# 네번째 영역
x4.plot(data3, 'g--') # 색상, 선 스타일
plt.show()


# 4. 차트 플롯으로 한 개 차트 그리기
fig2 = plt.figure()
chart = fig2.add_subplot(1,1,1)

# data 생성
data5 = np.random.randn(50) # 정규분포 난수
data6 = np.random.randn(50).cumsum() # 누적합

# 계단형 차트
chart.plot(data5, color='r', label ='step', drawstyle='steps-post')

# 선스타일 차트
chart.plot(data6, color='b', label = 'line')


#plt.title('step vs line chart')
plt.title('계단형과 선 그래프')
plt.xlabel('y data 인덱스')
plt.ylabel('정규분포 난수, 누적합')
plt.legend(loc='best') # 범례
plt.show()
