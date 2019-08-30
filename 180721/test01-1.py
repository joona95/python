#작성내용 : 형변환
#작성일 : 2018.07.14
#작성자 : 최준아
#두 수를 입력받아서 곱한 후 출력

print("첫 번째 수를 입력하세요. :")
a=input()
print("두 번째 수를 입력하세요. :")
b=input()


result=int(a)*int(b)

print(result)


print(type(a))


#float() 실수형


dic = {}
dic['파이썬']='www.python.org'
dic['마이크로소프트']='www.microsoft.com'
dic['애플']='www.apple.com'
print(dic['파이썬'])
print(dic['마이크로소프트'])
print(dic['애플'])
print(type(dic))
print(dic)
print(dic.keys())
print(dic.values())
print(dic.items())
print(type(dic.items()))


print('애플' in dic.keys())
print('사과' in dic.keys())
print('www.microsoft.com' in dic.values())
print('www.seanlab.net' in dic.values())
