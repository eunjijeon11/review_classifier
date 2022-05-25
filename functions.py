# NOTE: THis file is module.

from re import U
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from konlpy.tag import Okt
import time
import random
import re


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
    correct_spell = []
    okt = Okt()

    kor_dict = { "ㅈㄴ" : "진짜", "ㄱㅊ" : "귀찮", "ㅈㅂ" : "제발", "개꿀" : "진짜좋다", "역씌" : "역시", "느님": "", "꼽" : "눈치", "deadline" : "마감일", "강평" : "강의평가"}
    dict_keys = kor_dict.keys()

    for i in range(len(review_list)):
        review = review_list[i]
        for key in dict_keys:
            review = review.replace(key, kor_dict[key])
        review = re.compile('[^ㄱ-ㅎ가-힣]').sub(' ', review)
        review = ' '.join(review.split())
        checked = okt.normalize(review)
        # print(checked)

        correct_spell.append(checked)

    return correct_spell


def get_token(reviews):
    okt = Okt() # konply okt 객체 선언

    token = [] # return 할 token list

    user_dict = ["질의응답", "QnA|Q&A", "큐앤에이", "pf", "피에프", "패스패일", "강의력", "성균"]
    p = re.compile('[A-Za-z+]+') # 영어부분만 빼냄
    for i in range(len(reviews)):
        token.append([])        

        for k in range(len(user_dict)):
            user_word = re.compile(user_dict[k]).findall(reviews[i])
            if len(user_word):
                reviews[i] = reviews[i].replace(user_dict[k], ' ')
                if k<3:
                    token[i] = token[i] + [user_dict[0]] * len(user_word)
                elif k<6:
                    token[i] = token[i] + [user_dict[3]] * len(user_word)
                else:
                    token[i] = token[i] + user_word

        reviews[i] = reviews[i].replace("에이쁠", "a+")
        reviews[i] = reviews[i].replace("비쁠", "b+")
        reviews[i] = reviews[i].replace("씨쁠", "c+")
        reviews[i] = reviews[i].replace("에프", "f")

        result = p.findall(reviews[i])
        for alphabet_word in result:
            if re.compile('[Aa|Bb|Cc|Dd|Ff][+]?').fullmatch(alphabet_word):  # 성적에 해당하면 token에 추가
                token[i].append(alphabet_word.lower())

    checked = correct_review(reviews) # 맞춤법 검사

    file = open("stopwords.txt", 'r', buffering=-1, encoding='utf-8')
    stopwords = file.readline().split(" ")
    for i in range(len(checked)):
        msg = okt.morphs(checked[i], stem=True) # 토큰화
        for word in msg:
            if word in stopwords:
                msg.remove(word)
        token[i] = token[i] + msg

    file.close()
    return token

def bow_and_dict(review):
    bow = []
    dict = {}

    for word in review:
        if word in dict:
            bow[dict[word]] = bow[dict[word]] + 1
        else:
            dict[word] = len(bow)
            bow.append(1)
    
    return bow, dict


