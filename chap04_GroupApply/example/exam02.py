'''
step02 관련 문제
 - 2012년도 미국 대통령 선거 후원금 data set 처리 
'''

import pandas as pd
import matplotlib.pyplot as plt

election = pd.read_csv('../data/election_2012.csv', encoding='ms949')
print(election.info())
'''
cand_id : 대선 후보자 id
cand_nm : 대선 후보자 이름
contbr_nm : 후원자 이름 
contbr_occupation : 후원자 직업군 
contb_receipt_amt : 후원금 
'''

# DF 객체 생성 
name = ['cand_nm', 'contbr_occupation', 'contb_receipt_amt']
# subset 생성 
election_df = pd.DataFrame(election, columns= name)
print(election_df.info())
print(election_df.head())
print(election_df.tail())


# 중복되지 않은 대선 후보자 추출 
unique_name = election_df['cand_nm'].unique()
print(len(unique_name)) 
print(unique_name) 

# 중복되지 않은 후원자 직업군 추출 
unique_occ =  election_df['contbr_occupation'].unique()
print(len(unique_occ)) 
print(unique_occ)

#############################################
#  Obama, Barack vs Romney, Mitt 후보자 분석 
#############################################

# 1. 두 후보자 관측치만 추출 : isin()
two_cand_nm=election_df[election_df.cand_nm.isin(['Obama, Barack','Romney, Mitt'])]
print(two_cand_nm.head())
print(two_cand_nm.tail())
print(len(two_cand_nm)) # 700975

'''
문1) two_cand_nm 변수를 대상으로 피벗테이블 생성하기 
    <조건1> 교차셀 칼럼 : 후원금, 열 칼럼 : 대선 후보자,
             행 칼럼 : 후원자 직업군, 적용함수 : sum
    <조건2> 피벗테이블 앞부분 5줄 확인   
문2) 피벗테이블 대상 필터링 : 2백만달러 이상 후원금 대상     
'''

two_cand_nm_table = pd.pivot_table(two_cand_nm,
               values = 'contb_receipt_amt',
               index = 'contbr_occupation',
               columns = 'cand_nm',
               aggfunc = 'sum' )

print(two_cand_nm_table.head())
'''
cand_nm                              Obama, Barack  Romney, Mitt
contbr_occupation                                               
   MIXED-MEDIA ARTIST / STORYTELLER          100.0           NaN
 AREA VICE PRESIDENT                         250.0           NaN
 RESEARCH ASSOCIATE                          100.0           NaN
 TEACHER                                     500.0           NaN
 THERAPIST                                  3900.0           NaN
 '''
 
print(two_cand_nm_table.tail())
'''
cand_nm                Obama, Barack  Romney, Mitt
contbr_occupation                                 
ZEPPOS AND ASSOCIATES         1000.0           NaN
ZONE MANAGER                   135.0           NaN
ZOOKEEPER                       35.0           NaN
ZOOLOGIST                      400.0           NaN
ZOOLOGY EDUCATION               25.0           NaN
'''

print(two_cand_nm_table.ix[10000:10100,:])

# 2백만달러 이상 후원금 대상
over_2mn = two_cand_nm_table[two_cand_nm_table.sum(1) >= 2000000]
print(over_2mn)
'''
cand_nm                                 Obama, Barack  Romney, Mitt
contbr_occupation                                                  
ATTORNEY                                  11126932.97    5302578.82
CEO                                        2069784.79     353310.92
CONSULTANT                                 2459812.71    1404576.94
EXECUTIVE                                  1355161.05    2230653.79
HOMEMAKER                                  4243394.30    8037250.86
INFORMATION REQUESTED                      4849801.96           NaN
INFORMATION REQUESTED PER BEST EFFORTS            NaN   11173374.84
INVESTOR                                    884133.00    1494725.12
LAWYER                                     3159391.87       7705.20
PHYSICIAN                                  3732387.44    1332996.34
PRESIDENT                                  1878009.95    2403439.77
PROFESSOR                                  2163571.08     160362.12
RETIRED                                   25270507.23   11266949.23
'''
