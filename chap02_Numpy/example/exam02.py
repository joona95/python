'''
 step02_indexing 관련문제
 문1) 6행6열의 다차원 zero 행렬 객체를 생성한 후 다음과 같이 indexing 하시오.
   조건1> 36개의 셀에 1~36까지 정수 채우기
   조건2> 2번째 행 전체 원소 출력하기  
              출력 결과 : 7.   8.   9.  10.  11.  12.
   조건3> 5번째 열 전체 원소 출력하기 
              출력결과 : 5. 11. 17. 23. 29. 35.            
   조건4> 15~29까지 블럭으로 출력하기
              출력결과 :  
       15.  16.  17.
       21.  22.  23
       27.  28.  29.
 
 문2) 6행 4열의 다차원 zero 행렬 객체를 생성한 후 다음과 같이 처리하시오.
     조건1> 20~100 사이의 난수 정수를 발생하여 각 행의 시작열에 난수 정수를 저장하고,
            두번째 열 부터는 1씩 증가시켜 원소 저장
     조건2> 첫번째 행과 마지막 행의 복사본 생성 후,첫번째 행에 1000,마지막 행에 6000으로 수정 

<<출력 예시>>
1. zero 다차원 배열 객체 
[[ 0.  0.  0.  0.]
 [ 0.  0.  0.  0.]
 [ 0.  0.  0.  0.]
 [ 0.  0.  0.  0.]
 [ 0.  0.  0.  0.]
 [ 0.  0.  0.  0.]]
 
2. 난수 정수 발생 
random.randint(20, 100, 6)
90
40
100
22
52
71

3. zero 다차원 배열에 난수 정수 초기화 결과 
[[  90.   91.   92.   93.]
 [  40.   41.   42.   43.]
 [ 100.  101.  102.  103.]
 [  22.   23.   24.   25.]
 [  52.   53.   54.   55.]
 [  71.   72.   73.   74.]] 

4. 첫번째 행에 1000,마지막 행에 6000으로 수정
 [[ 1000.  1000.  1000.  1000.]
  [   40.    41.    42.    43.]
  [  100.   101.   102.   103.]
  [   22.    23.    24.    25.]
  [   52.    53.    54.    55.]
 [ 6000.  6000.  6000.  6000.]] 
'''


