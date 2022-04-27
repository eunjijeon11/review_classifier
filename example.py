from selenium import webdriver
import random
import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

ID = "eunzee03"
PW = "ehrehrgksdmswl1129^^"

def ran_sleep():
    sleep_time = random.randint(2,4)
    time.sleep(sleep_time)

driver = webdriver.Chrome(r'C:\Users\user\Documents\chromedriver_win32\chromedriver')
driver.implicitly_wait(1)

driver.get('https://everytime.kr/login')
ran_sleep()
driver.find_element(by=By.NAME, value='userid').send_keys(ID)
driver.find_element(by=By.NAME, value='password').send_keys(PW)
driver.find_element(by=By.XPATH, value='//*[@class="submit"]/input').click()
ran_sleep()

driver.get('https://everytime.kr/lecture/view/43665')

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

reviews = soup.select('p.text')
review_list = list(reviews)
print(review_list[-2])
for i in range(len(review_list)):
    print(review_list[i].get_text())
