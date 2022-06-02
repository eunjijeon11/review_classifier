from functions import*
import csv
import ast


Id = input("id:")
Pw = input("pw:")
classnum = input("강평번호를 입력하세요:")

driver = login(Id,Pw)
review = get_review(driver,classnum)
token_list = get_token(review)
#print(token_list[:10])

file = open("train_data.csv", 'r', newline='', buffering=-1, encoding='utf-8')
reader = csv.reader(file)

data = []
for line in reader:
    data.append(ast.literal_eval(line[1]))

pos_bow = data[0]
pos_dict = data[1]
neg_bow = data[2]
neg_dict = data[3]

pos = 0
neg = 0

for token_review in token_list:
    pos_p = 1
    for token in token_review:
        if token in pos_dict:
            pos_p *= (pos_bow[pos_dict[token]] + 1) / (sum(pos_bow) + 1)
        else:
            pos_p *= 1 / (sum(pos_bow) + 1)
    neg_p = 1
    for token in token_review:
        if token in neg_dict:
            neg_p *= (neg_bow[neg_dict[token]] + 1) / (sum(neg_bow) + 1)
        else:
            neg_p *= 1 / (sum(neg_bow) + 1)

    pos_p *= 230 / 314
    neg_p *= 84 / 314

    if pos_p >= neg_p:
        pos += 1
    else:
        neg += 1

print("="*15, "분석 결과", "="*15)
print("긍정적 강의평", round(pos * 100 / (pos + neg), 2), "% (", pos, "개 )")
print("부정적 강의평", round(neg * 100 / (pos + neg), 2), "% (", neg, "개 )")
 
file.close()
