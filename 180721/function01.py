#함수 사용하기







# def pat(): #작성.....
#     pass
#
# def hello_korean():
#     print("안녕하세요")
#
# def hello_english():
#     print("hello")
#
# def get_greeting(where):
#     if where == 'K':
#         return hello_korean()
#     else:
#         return hello_english()
#
# get_greeting('K')







#딕셔너리 형식 가변 매개변수 : **

def print_team(**player):
    for k in player.keys():
        print("{0} = {1}".format(k, player[k]))



#print_team(카시야스="GK", 호날두="FW", 페페="DF")










#가변 매개변수: 입력개수가 달라질 수 있는 매개변수
#*를 이용하여 정의된 가변 매개변수는 튜플

def merge_string(*text_list):
    result=""

    for s in text_list:
        result = result + s
    return result
#
#
# rs = merge_string("오늘은 ","무지 ","더운 날입니다.")
# print(rs)
#
# print(type(rs))







#매개변수 이용한 입력
# def print_personel(name, position="staff", nationality="Korea"):
#     print('name={0}'.format(name))
#     print('position={0}'.format(position))
#     print('nationality={0}'.format(nationality))
#
#
# print_personel(name="홍길동1")
# print_personel(name="홍길동2", nationality="북")
# print_personel(name="홍길동3",nationality="북",position="ROx")
# print_personel(name="홍길동4",nationality="korea")







#문자열받아서 횟수반복출력
# def print_string(text, count=1): #기본값줄수 있음
#     for i in range(count):
#         print(text, end=" ")
#
#
#
# def my_abs(arg):
#     if(arg<0):
#         result = arg* -1
#     else:
#         result = arg
#     return result
#
#
# #실행부분
# print_string("안녕하세요", 5)
# print_string("안녕")
#
#
# num = my_abs(-20)
# print(num)

