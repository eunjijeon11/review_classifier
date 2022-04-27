from selenium import webdriver
import random
import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

ID = input("ID: ")
PW = input("PW: ")

def ran_sleep(): # 봇으로 오해받지 않기 위해 쉬어주는 코드
    sleep_time = random.randint(2,4)
    time.sleep(sleep_time)

driver = webdriver.Chrome(r'C:\Users\user\Documents\chromedriver_win32\chromedriver') # 가상 드라이버 열기
driver.implicitly_wait(1)

driver.get('https://everytime.kr/login') # 로그인 페이지로 이동
ran_sleep()
driver.find_element(by=By.NAME, value='userid').send_keys(ID)
driver.find_element(by=By.NAME, value='password').send_keys(PW)
driver.find_element(by=By.XPATH, value='//*[@class="submit"]/input').click() # 로그인
ran_sleep()

driver.get('https://everytime.kr/lecture/view/43665') # 43665 강의의 강의평가 페이지로 이동

html = driver.page_source # 강평 페이지의 html 소스 가져옴
soup = BeautifulSoup(html, 'html.parser')

reviews = soup.select('p.text') # p(paragraph에서 class 명이 text인 것만 뽑음(복수 개))
review_list = list(reviews)
print(review_list[-2]) # 뒤에서부터 3개는 강평 아님
for i in range(len(review_list)):
    print(review_list[i].get_text()) # 다 출력해보기
