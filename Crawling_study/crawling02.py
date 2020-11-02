from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome("C:\\Users\\hyurs\\Downloads\\chromedriver_win32\\chromedriver.exe")

driver.maximize_window()

driver.get('https://everytime.kr/login?redirect=%2Flecture')

sleep(10)
driver.find_element_by_name('userid').send_keys('joona95')
sleep(1)
driver.find_element_by_name('password').send_keys('go950502')

sleep(1)
driver.find_element_by_xpath('//*[@id="container"]/form/p[3]').click()
sleep(10)

courseName = '정보보호개론'
profName = '최형기'


###교수님 평점###
driver.get('https://everytime.kr/lecture/search/'+profName)

sleep(10)

lectures = driver.find_elements_by_xpath('//*[@class="lecture"]')

for i in range(0, len(lectures)):
    lectures[i].click()
    sleep(10)

    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    print(soup.find(class_='value').get_text())

    driver.get('https://everytime.kr/lecture/search/'+profName)
    sleep(10)

    lectures = driver.find_elements_by_xpath('//*[@class="lecture"]')


###과목 평점###
driver.get('https://everytime.kr/lecture/search/'+courseName)

sleep(10)

lectures = driver.find_elements_by_xpath('//*[@class="lecture"]')
professors = driver.find_elements_by_xpath('//*[@class="professor"]')

for i in range(0, len(lectures)):
    if professors[i].text==profName:
        lectures[i].click()
        sleep(10)

        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        print(soup.find(class_='value').get_text())

        driver.get('https://everytime.kr/lecture/search/'+profName)
        sleep(10)

        break

