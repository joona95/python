import os
import matplotlib as mat


data = []  # 값 저장
url = "c:\\data\\data.txt"
fout= "c:\\data\\data2.txt"

if os.path.exists(url):
    f=open(url,"r")  #파일읽기
    #f=open(url,"r",encoding="utf-8")  #파일읽기 오류발생(ANSI)
    fw=open(fout, "w")  #파일쓰기

    #파일에 저장된 모든 줄을 읽는다
    for line in f.readlines():
        data.append(line.strip()) #줄을 읽어서 data연결하여 저장
        fw.writelines(line) #읽은 줄을 fw에 쓰기

    print(data)
    f.close()

else:
    print("{0}파일이 없습니다.".format(url))

