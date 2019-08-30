
#2
def sort_dictionary(dic):
    return sorted(tuple(dic.items()))
    
print(sort_dictionary({"김철수":78, "이하나":97, "정진원":88}))


#3
def string_middle(str):
    if len(str) % 2 ==0 :
        index = len(str)//2
        return str[index-1:index+1]
    else :
        index = len(str)//2
        return str[index]

print(string_middle("people"))


#4
#return sorted(strings,key=lambda strings:strings[n])
def strange_sort(strings,n):
    return sorted(strings,key=lambda strings:strings[n])

print(strange_sort(["sun","bed","car"], 1))


#5
#for in , if not
def no_continuous(s):
    result=[]
    result.append(s[0])
    for i in range(len(s)-1):  # 요소, 목록 0부터 시작
        if not s[i] == s[i+1]:  # 중복하지 않으면
            result.append(s[i+1])  #문자열 연결
    return result

print(no_continuous("133330333331"))


#6
def digit_reverse(n):
    result=[]
#     n=str(n)
#     n=n[::-1]
#     for i in n:
#         result.append(int(i))
    n=str(n)
    for i in range(len(n)-1,0,-1):
        result.append(int(n[i]))
    result.append(int(n[0]))
    return result

print(digit_reverse(12345))



#7
def Harshad(n):
    result = sum(map(int, str(n)))
    if(n % result ==0):
        return True
    else:
        return False


print(Harshad(20))



#8
def alpha_string46(s):
    return s.isdigit() and (len(s)==4 or len(s)==6)

print(alpha_string46("a234"))
print(alpha_string46("1234"))


#9
def rm_small(mylist):
    mylist.remove(min(mylist))
    return mylist


my_list = [4,3,2,1]
print("결과 {}".format(rm_small(my_list)))


#10
def strToint(str):
    result=int(str)
    return result

print(strToint("-1234"))



