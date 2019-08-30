#작성내용:IfTest01~03
#작성일:2018.07.15
#작성자:최준아


#나이를 키보드로 입력받아 아래와 같이 처리하는 구문을 완성하세요
#숫자 999 입력받기전까지 1번문장을 반복하세요.
#총 몇회 반복했는지 출력하세요.



age, count=0, 0

while True:
    
    print("나이를 입력하세요 : ")
    age=int(input())
    
    if age==999:
        break
    else:        
        if age>=70:
            print("경로카드")
        elif age>=20:
            print("성인카드")
        else:
            print("유치카드")
        count+=1
        
print("종료합니다.")


print("반복한 횟수: {0}번".format(count))
print("종료합니다.")
    





#나이를 키보드로 입력받아 아래와 같이 처리하는 구문을 완성하세요


print("나이를 입력하세요.")
age=int(input())


if age>=70:
    print("경로카드")
elif age>=20:
    print("성인카드")
else:
    print("유치카드")





#두 수를 입력받아 합을 구하세요

print("두 수를 입력하세요: ")
a=int(input())
b=int(input())

print("입력한 두 수의 합:")
print(a+b)




#두 수를 입력받아 합을 구하세요
#숫자 999 입력받기전까지 1번문장을 반복하세요.
#총 몇회 반복했는지 출력하세요.

a,b,count=0,0,0

while True:
    print("두 수를 입력하세요: ")
    a=int(input())
    b=int(input())
    
    if (a or b) == 999 :
        break
    else:
        print("입력한 두 수의 합: ")
        print(a+b)
        count+=1

print("종료합니다")

print("반복한 횟수:{0}".format(count))
        


#두수와 연산자를 입력받아 처리하세요

A,B,C=0,0,0

print("두 수를 입력하세요.")

A=int(input())
B=int(input())

print("연산자를 입력하세요.(+,-,*,/)")
C=input()

if C=="+":
    print(A,"+",B,"=", A+B)
elif C=="-":
    print(A,"-",B,"=",A-B)
elif C=="*":
    print(A,"*",B,"=",A*B)
elif C=="/":
    print(A,"/",B,"=",A/B)
else:
    print("입력된 값이 연산자가 아닙니다.")
    


#두수와 연산자를 입력받아 처리하세요
#숫자 999 입력받기전까지 1번문장을 반복하세요.
#총 몇회 반복했는지 출력하세요.

A,B,C,count=0,0,"",0
C_check=['+','-','*','/']

while True:
    print("두 수를 입력하세요:")
    A=int(input())
    B=int(input())

    print("연산자를 입력하세요.(+,-,*,/)")
  
    C=input()

    if (A or B) ==999:
        break
    else:
        if C not in C_check:
            print("입력한 값이 연산자가 아닙니다.")
            
        else:    
            if C=="+":
                print(A,"+",B,"=", A+B)
            elif C=="-":
                print(A,"-",B,"=",A-B)
            elif C=="*":
                print(A,"*",B,"=",A*B)
            elif C=="/":
                print(A,"/",B,"=",A/B)
            

        count+=1


print("종료되었습니다.")

print("반복된 횟수:{}".format(count))        




#구구단

for j in range(2,10,1): 
    for i in range(1,10,1):
        print("{0}*{1}={2}".format(j,i,j*i))




