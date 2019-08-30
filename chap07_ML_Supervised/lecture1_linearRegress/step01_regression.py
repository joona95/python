'''
scipy 패키지 이용 선형회귀모형
'''

from scipy import stats
import pandas as pd

score_ip = pd.read_csv('../data/score_iq.csv')
print(score_ip.info())
'''
RangeIndex: 150 entries, 0 to 149
Data columns (total 6 columns):
'''
print(score_ip.head())
'''
     sid  score   iq  academy  game  tv
0  10001     90  140        2     1   0
1  10002     75  125        1     3   3
2  10003     77  120        1     0   4
3  10004     83  135        2     3   2
4  10005     65  105        0     4   4
'''

# x(iq) -> y(score) 벡터화
x = score_ip.iq # 독립변수
y = score_ip.score # 종속변수

# 1) 단순선형회귀모형
mode1 = stats.linregress(x,y)
print(mode1)
# LinregressResult(slope=0.6514309527270075, intercept=-2.8564471221974657, rvalue=0.8822203446134699, pvalue=2.8476895206683644e-50, stderr=0.028577934409305443)
print('x 기울기 : ', mode1.slope)
print('y 절편 : ', mode1.intercept)
print('설명력 : ', mode1.rvalue)
'''
x 기울기 :  0.6514309527270075
y 절편 :  -2.8564471221974657
설명력 :  0.8822203446134699
'''

# 회귀방정식 : Y = X * 기울기 + 절편
X = 140
Y = (X * mode1.slope) + mode1.intercept
print('y 예측치=', Y)
# y 예측치= 88.34388625958358

print('error = ', 90-Y)
# error =  1.6561137404164157


# 2) 다중선형회귀모형 : 독립변수 2개 이상
import statsmodels.formula.api as sm

# 상관분석
cor = score_ip.corr()
print(cor) # 상관계수 행렬
'''
              sid     score        iq   academy      game        tv
sid      1.000000 -0.014399 -0.007048 -0.004398  0.018806  0.024565
score   -0.014399  1.000000  0.882220  0.896265 -0.298193 -0.819752
iq      -0.007048  0.882220  1.000000  0.671783 -0.031516 -0.585033
academy -0.004398  0.896265  0.671783  1.000000 -0.351315 -0.948551
game     0.018806 -0.298193 -0.031516 -0.351315  1.000000  0.239217
tv       0.024565 -0.819752 -0.585033 -0.948551  0.239217  1.000000
'''
# x(score ~ iq + academy) -> y(score)
model = sm.ols(formula = 'score ~ iq + academy', data = score_ip).fit()

print(model.params) # 계수값 = 기울기, 절편
'''
Intercept    25.229141 : y절편
iq            0.376966 : x1 기울기
academy       2.992800 : x2 기울기
'''

# 모델 결과
print(model.summary())
'''
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                  score   R-squared:                       0.946
Model:                            OLS   Adj. R-squared:                  0.946
Method:                 Least Squares   F-statistic:                     1295.
Date:                Sat, 28 Jul 2018   Prob (F-statistic):           4.50e-94
Time:                        16:20:46   Log-Likelihood:                -275.05
No. Observations:                 150   AIC:                             556.1  
Df Residuals:                     147   BIC:                             565.1
Df Model:                           2                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept     25.2291      2.187     11.537      0.000      20.907      29.551
iq             0.3770      0.019     19.786      0.000       0.339       0.415
academy        2.9928      0.140     21.444      0.000       2.717       3.269
==============================================================================
Omnibus:                       36.342   Durbin-Watson:                   1.913
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               54.697
Skew:                           1.286   Prob(JB):                     1.33e-12
Kurtosis:                       4.461   Cond. No.                     2.18e+03
==============================================================================
'''