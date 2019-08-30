

a=3470

b=a//500 #500원짜리 몇개??

c=a%500  #500원짜리 바꾼 후에 나머지

d=c//100 #나머지에서 100원짜리 몇개??

e=c%100 #100원짜리 바꾼 후 나머지

f=e//50 #나머지에서 50원짜리 몇개?

g=e%50 #50원짜리 바꾼 후 나머지

h=g//10 #나머지에서 10원짜리 몇개?


print("3470원을 동전으로 교환하기")
print("500원짜리 몇 개?")
print(b)
print("100원짜리 몇 개?")
print(d)
print("50원짜리 몇 개?")
print(f)
print("10원짜리 몇 개?")
print(h)


print("--동전교환--")


#변수선언
#money
#c500 , c100, c50, c10  각 동전수

money, c500, c100, c50, c10 = 0,0,0,0,0


money= int(input("교환할 돈 : ")) 



c500 = money//500  #500원 개수

money = money % 500  #500원 개수 나눈 나머지 : 잔돈

c100 = money//100  #100원 개수

money = money % 100 #잔돈

c50 = money//50 #50원 개수

money = money%50 #잔돈

c10 = money//10  #10원 개수

money = money%10 #잔돈
   

print("500원",c500, "개")
print("100원", c100, "개")
print("50원", c50, "개")
print("10원", c10, "개")
print("바꾸지 못한 잔돈은", money, "원")


#index 0부터 시작
s="01234567890123456"
print(s[0:4])  #0부터 4앞까지  "0123"
print(s[2:7])  #2부터 7앞까지   "23456"
print(s[0:10:2])  #0부터 10앞까지 2칸씩 뛰어서 추출 "02468"
print(s[0:15:3])  # "03692"



a='Good Morning'
print('Good' in a)
print('문자열의 길이:',len(a)) 



a='Hello'
#시작문자열 검색
a.startswith('He')
#true

#마지막문자열
a.endswith('lo')
#true

#문자열 찾기 -> index
a.find('H')  #0
a.find('K')  #-1

a.rfind('H')  #0

#수량
a.count('l')  #2



#strip()  양쪽으로 공백제거


#isalpha()  알파벳으로만 있느냐
a='asdf'
b='332abc'
a.isalpha()  #true
b.isalpha()  #false
#isnumeric()  숫자로만 있느냐
#isalnum() 알파벳과 수로만 있느냐
b.isalnum()  #true



#replace()
a="Hello World"
b=a.replace("World", "Korea")
print (b)   # Hello Korea


#list 배열
#split()
a="감나무, 배, 사과, 오렌지"
b=a.split(',')
print(b)  #['감나무', '배', '사과', '오렌지']
type(b)  #class 'list'
type(a)  #class 'str'


#upper() : a97->A65
#lower() : A->a


#format()

a='abc'
a*20  #문자열복사해서 20번붙여넣기




a='20180714free'

#year, day, weather 를 찾아서 출력하세요


print("year:", a[0:4])
print("month:",a[4:6])
print("day:", a[6:8])
print("weather:", a[8:12])



