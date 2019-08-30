




#랜덤함수
from random import *

for x in range(10):
    # i = randint(1,100)   # 1부터 100까지의 임의의 정수
    # print(i, end=", ")
    f = random()
    f = f * 45
    print(f)
    lotto= int(f*45) + 1
    print(lotto, end=", ")    # 0부터 1사이의 임의의 실수





#
# import turtle as t
# from random import *
#
# col=["green", "red", "yellow", "white"]
# #거북이 모양으로 변경
# t.shape("turtle")
#
# n=100
# t.bgcolor("black")
#
# t.speed(0)
#
# for x in range(n):
#     r = randint(0, 3)
#     t.color(col[r])
#     t.circle(80)
#     t.left(360/n)
#     # t.forward(15)








# import matplotlib.pylab as plt
#
# plt.plot([10,20,30,40],[1,4,9,16], 'bs--')
# plt.xlabel('data')
# plt.ylabel('result')
# plt.show()










# table = {"B4" : "before",
#          "TX" : "Thanks",
#          "BBL" : "back back late",
#          "HAND" : "Have a nice Day"
#          }
#
# value = list(table.values())
# print(value)
#
# for i in range(0,4):
#     print(value[i])
#
#
# num = int(input("0~3 중에 숫자를 입력하세요. : "))
#
# words = list(table.values())[num]
# print(words)
#
# if num in (1,2,3,4):
#     print(value[num-1])
# else:
#     print("입력하신 문자가 1~4에 해당하지 않습니다.")



