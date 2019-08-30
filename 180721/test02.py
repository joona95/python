#작성내용
#작성일: 2018.07.15
#작성자: 최준아


x=input("문자열입력")
print('h :'+x)
input('press Enter')

print('next')


#논리형 boolean type
#bool 은 true, false 2개의 값만 가짐

#not true (!true) => false


#if문 elif문


a=3

if a==3:
    print('삼')
    print('三')
    print('Three')
else:
    print('누구냐넌!')


import sys

print('수를 입력하세요: ')
a=int(input())

if a==0 :
    print('0은 나눗셈에 이용할 수 없습니다.')
    sys.exit(0)

print('3/', a, '=', 3/a)





print('요일(월~일)을 입력하세요 :')
dow=input()

if dow == '월':
    print('Monday')
elif dow == '화':
    print('Tuesday')
elif dow == '수':
    print('Wednesday')
elif dow == '목':
    print('Thursday')
elif dow == '금':
    print('Friday')
elif dow == '토':
    print('Saturday')
elif dow == '일':
    print('Sunday')
else:
    print('잘못 입력된 요일입니다.')



print('수를 입력하세요: ')
a=int(input())

if a >10 and a%2 ==0:
    print('10보다 큰 짝수')
elif a >10 and a%2 !=0:
    print('10보다 큰 홀수')
elif a%2 == 0:
    print('10이하의 짝수')

else:
    print('10이하의 홀수')


    
if a>10:
    if a%2 ==0:
        print('10보다 큰 짝수')
    else:
        print('10보다 큰 홀수')
else:
    if a%2 ==0:
        print('10이하의 짝수')
    else:
        print('10이하의 홀수')
    



#반복구문  for문, while문


print("몇 번 반복할까요?:")
limit=int(input())

count=1
while count<=limit:
    print("{0}회 반복.".format(count))
    count=count+1

print("반복 종료")


count=1

while True:

    print("{0}회 반복.".format(count))
    if count>=limit:
        break
    count=count+1

print("반복 종료")



'''
done=False
count=0

while !done:
    count=count+1
    if count>limit:
        done=True
'''


for i in (1,2,3):
    print(i)


for s in ("뇌를", "자극하는", "파이썬"):
    print(s)


print("-----------------")


for i in range(0,5,1):
    print(i)

    

#1부터 10까지의 합 구하기
sum=0  #합
for i in range(1,11,1):
    sum += i  #sum=sum+i

print(sum)


