
import requests
from bs4 import BeautifulSoup
"""
MEMBER_DATA = {
    'lang' : 'ko',
    'userid':'joona95',
    'password':'go950502',
    'saveid' : 'on'
}

with requests.Session() as s:
    request = s.post("https://eportal.skku.edu/wps/portal/!ut/p/z1/04_Sj9CPykssy0xPLMnMz0vMAfIjo8ziDVCAo4FTkJGTsYGBu7OJfrh-lH4UHiUWBlgVICvVL8jODgQAOE1iuw!!/dz/d5/L2dBISEvZ0FBIS9nQSEh/p0/IZ7_2P8CHCG0OG3I50QORS6UV700O4=CZ6_00000000000000A0BR2B300GC4=LA0=/#Z7_2P8CHCG0OG3I50QORS6UV700O4", data=MEMBER_DATA, verify=False, allow_redirects=False)

redirect_cookie= request.headers['Set-Cookie']
redirect_url = request.headers['Location']

headers = {"Cookie": redirect_cookie}

end = s.get(redirect_url, headers=headers)

soup = BeautifulSoup(end.text, "html.parser")

print(soup.find(class_="userInfo"))

#print(request.text)

"""
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome("C:\\Users\\hyurs\\Downloads\\chromedriver_win32\\chromedriver.exe")

driver.get('https://eportal.skku.edu/wps/portal/!ut/p/z1/04_Sj9CPykssy0xPLMnMz0vMAfIjo8zijQIsnD2c3Q38LcxNnQwC_YNMvPy9gwyCnc30w8EKDFCAo4FTkJGTsYGBe7CBfhSGNLJCqH5ToOkeRkAL3E1DTA0CLUL8g51DwwyBSgjrj8KiBOECfyOsClDMgCjA5QZ_Q_1An_z09NQU_9IS_YLc0AiDzIB0ALi2J0A!/')

sleep(0.5)
driver.find_element_by_name('userid').send_keys('joona95')
sleep(0.5)
driver.find_element_by_name('password').send_keys('go950502')

driver.find_element_by_xpath('//*[@id="LoginForm"]/div/button').click()
driver.find_element_by_xpath('//*[@id="mypage"]/form[1]/div/div[1]/div[2]/div/ul/li[2]/a/span[1]/img').click()

"""
html = driver.page_source

soup = BeautifulSoup(html, "html.parser")

print(soup.find(class_="userInfo"))
"""