'''
1. dict structure
2. 열거형 함수
'''

# 1. dict
person = {'name' : '홍길동', 'age' : 35, 'addr' : '서울시'}
print(person)
print(type(person))
'''
{'name': '홍길동', 'age': 35, 'addr': '서울시'}
<class 'dict'>
'''

for key in person :
    print(key) # key
    print(person[key]) # value
'''
name
홍길동
age
35
addr
서울시
'''

# word count 예문
count = {}  # 빈 set
charset = ['a','b','a','c','b','a'] # list

for key in charset :
    count[key] = count.get(key,0) +1
    
print(count)
#{'a': 3, 'b': 2, 'c': 1}

# 2. 열거형 함수
print(charset) # ['a', 'b', 'a', 'c', 'b', 'a']

for idx, cont in enumerate(charset) :
    print('index=',idx)
    print('content=', cont)
    
    

