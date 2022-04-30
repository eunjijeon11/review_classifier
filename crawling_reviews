from functions import *
import csv

userId = input("id: ")
userPw = input("pw: ")

review_id = ["2087283", "2010087", "103698", "2376753", "2249415", "2249336"]
# review_id = ["43666"]

driver = login(userId, userPw)
file = open('review_data.csv', 'w', newline='', buffering=-1, encoding='utf-8')
writer = csv.writer(file)
writer.writerow(["_id", "review", "rabel"])

_id = 1

for id in review_id:
    review_list = get_review(driver, id)
    for review in review_list:
        if "이 정보를 확인하기 위해" in review:
            print("remove", review)
            review_list.remove(review)

    review_row = [[_id + i, review_list[i]] for i in range(len(review_list))]
    writer.writerows(review_row)
    _id += len(review_list)

    ran_sleep()
file.close()