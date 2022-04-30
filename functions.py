# NOTE: THis file is for functions.

from re import U
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from hanspell import spell_checker
import time
import random

def ran_sleep():
    sleep_time = random.randint(2,4)
    time.sleep(sleep_time)

def login(id, pw):
    driver = webdriver.Chrome(r'C:\Users\user\Documents\chromedriver_win32\chromedriver') # 가상 드라이버 열기
    driver.implicitly_wait(1)

    driver.get('https://everytime.kr/login') # 로그인 페이지로 이동
    ran_sleep()
    driver.find_element(by=By.NAME, value='userid').send_keys(id)
    driver.find_element(by=By.NAME, value='password').send_keys(pw)
    driver.find_element(by=By.XPATH, value='//*[@class="submit"]/input').click() # 로그인
    ran_sleep()

    return driver

def get_review(driver, class_num):
    while True:
        driver.get('https://everytime.kr/lecture/view/'+ class_num)

        html = driver.page_source # 강평 페이지의 html 소스 가져옴
        soup = BeautifulSoup(html, 'html.parser')
        #print(soup.prettify)
        reviews = soup.select('p.text') # p(paragraph)에서 class 명이 text인 것만 뽑음(복수 개))
        print(reviews)

        if len(reviews) == 0:
            continue
        else:
            break
        
    review_list = list(reviews)
    review_list = [review_list[i].get_text() for i in range(len(review_list))]
    # review_list = correct_review(review_list) # 맞춤법 검사

    return review_list

def correct_review(review_list):
    correct_spell = [spell_checker.check(i).checked for i in review_list]

    return correct_spell

"""
if __name__ == "__main__":
    main()
"""


