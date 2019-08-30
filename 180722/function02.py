#파일읽어서, 기준으로 처리해보기 split()
#파일 오픈
#url = "c:\\workpython\\student.txt"

def choi(url):
    import os
    if os.path.exists(url):
        f=open(url,"r")
        #파일의 각 줄에 대하여 반복
        for line in f.readlines():
            #공백문자제거
            line = line.strip()
            #줄을 출력한다
            print(line)
            #줄을 단어로 분리
            words = line.split(",")
            #줄의 단어 출력
            for word in words:
                print("    ", word)
    else:
        print("{0}파일이 없습니다.".format(url))

choi("c:\\workpython\\student.txt")


#B4 =>>Before, TX =>> Thanks
# message, words, result = "", "", ""  #변수 선언
#
# table = {"B4" : "before",
#          "TX" : "Thanks",
#          "BBL" : "back back late",
#          "HAND" : "Have a nice Day"
#          }
#
# message = input("번역할 문장을 입력하세요 (B4, TX, BBL, HAND) : ")
# words = message.split()
#
# for w in words:
#     if w in table :
#         result += table[w] + " "
#     else:
#         result += w + " "
#
# print(result)      #"before Have a nice Day"





# phrase = input("문자열을 입력하세요:")
# acr = ""  #대문자
#
# #acr = phrase.upper().split()
# for word in phrase.upper().split():
#     acr += word[2]
#
# print(acr)



#파이썬의 내장함수가 있으나 pandas, numpy 모듈을 이용해서 보통 분석
#빅데이터 / 머시러닝

# partA = set(["Park", "Kim", "Lee"])
# partB = set(["Park", "choi"])
#
# print("2개의 파티에 모두 참석한 사람은?")
# print(partA.intersection(partB))


