from function01 import print_team, merge_string
import parser as pd




print_team(카시야스="GK", 호날두="FW", 페페="DF")


rs = merge_string("오늘은 ","무지 ","더운 날입니다.")
print(rs)

print(type(rs))


# import sys
#
# for path in sys.path:
#     print(path)




# my_list=[1,2,3]  #['da', 'bb', 'ddd']
#
# try:
#     print("첨자를 입력")
#     index = int(input())
#     print(my_list[index]/2)
#
# except ZeroDivisionError as err:
#     print("0으로 나눌 수 없습니다.{0}".format(err))
#
# except IndexError as err:
#     print("범위가 벗어났습니다.{0}".format(err))
#
# except:
#     print("이외의 예외처리")
#
# else:
#     print("출력에 성공하였습니다.")
#
# finally:
#     print("어떤일이 있어도 마무리합니다.")




#try 안의 문장을 실행하고 오류발생시 except
# try:
#     print(1/0)
#
# except:
#     print("0으로 나누고 있어")






#문자열을 키보드 입력받아서 문자개수, 숫자개수 파악하기


# sentence = input("문자열을 입력하세요")
#
# table = {"alpha":0, "digits":0, "space":0} #선언
#
# for i in sentence:
#     if i.isalpha():
#         table["alpha"] +=1
#
#     if i.isdigit():
#         table["digits"] +=1
#
#     if i.isspace():
#         table["space"] +=1
#
#
# print(table)



# scors = {'Korean':50, 'Math':90, 'English':20}  #()->튜플    []->리스트  ""->문자열
# for item in scors.items():
#     print(item)
#
#
# address = input('이메일주소 입력')  #abc@naver.com
#
# (id, domain)=address.split("@")
# print(address)
# print(id)
# print(domain)



# i = 1
# while i<=9:
#     #print("3*%d = %d" % (i, 3*i))
#     print("3*{0}= {1}".format(i,3*i))
#     i +=1





# s=input("문자열을 입력하세요:")
# vowels = "aeiouAEIOU"  #금지어
#
# result = ""
# for letter in s :
#     if letter not in vowels:
#         result += letter
#
# print(result)




# fruit = "apple"
# index = 0
# while index < len(fruit): #0<5
#     letter = fruit[index]
#     print(letter, end="-------------")
#     index +=1






# import turtle
# import math
#
#
# polygon = turtle.Turtle()
#
# num_sides=6
# side_length = 70 #선이 길이
#
# angle = 360.0 / num_sides
#
# for i in range(num_sides):
#     polygon.forward(side_length)
#     polygon.right(angle)
#
#



# t=turtle.Turtle()
# t.pendown()
#
# for angle in range(360) :
#     y= math.sin(math.radians(angle))
#     scaledX=angle
#     scaledY=y*100
#     t.goto(scaledX,scaledY)
#
#
# t.penup()






# for i in range(3):
#     turtle.left(20) #왼쪽으로 20도 회전
#
#     turtle.forward(50)
#     turtle.left(90)
#     turtle.forward(50)
#     turtle.left(90)
#     turtle.forward(50)
#     turtle.left(90)
#     turtle.forward(50)
#     turtle.left(90)


# window = turtle.Screen()
# window.bgcolor("lightgreen")
#
# t= turtle.Turtle()
# t.shape("turtle")
# t.color("blue")
#
#
# #리스트에 색상
# colors = ["yellow", "red", "purple", "blue"]
#
# for c in colors :
#     t.color(c)
#     t.forward(200)
#     t.left(90)
#

