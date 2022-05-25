import functions
import csv

file = open('review_data_labeled.csv', 'r', buffering=-1, encoding='utf-8')
reader = csv.reader(file)

review, label = [], []
for row in list(reader)[1:]:
    review.append(row[1])
    label.append(row[2])
file.close()

tokenized_review = functions.get_token(review)

pos_word = []
neg_word = []
for i in range(len(tokenized_review)):
    if label[i] == '0':
        neg_word = neg_word + tokenized_review[i]
    elif label[i] == '1':
        pos_word = pos_word + tokenized_review[i]

pos_bow, pos_dict = functions.bow_and_dict(pos_word)
neg_bow, neg_dict = functions.bow_and_dict(neg_word)

train_data = open('train_data.csv', 'w', newline='', buffering=-1, encoding='utf-8')
wr = csv.writer(train_data)
wr.writerow(['positive bow', str(pos_bow)])
wr.writerow(['positive dict', str(pos_dict)])
wr.writerow(['negative bow', str(neg_bow)])
wr.writerow(['negative dict', str(neg_dict)])

train_data.close()
