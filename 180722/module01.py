#__main__에 대하여 알아보자
print('모듈시작')
print('module01.py:__name__= {0}'.format(__name__))
print('module01.py:__file__= {0}'.format(__file__))
print('모듈 끝')

if __name__ == "__main__":
    print("메인입니다.: 모듈직접실행이 되었습니다.")
else:
    print("import된 모듈입니다.")