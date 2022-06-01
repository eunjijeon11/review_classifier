from functions import*
Id=input("id:")
Pw=input("pw:")
driver = login(Id,Pw)
classnum=input("강평번호를 입력하세요:")
login(Id,Pw)
get_review(driver,classnum)
get_token(get_review)
review=get_token(get_review)
dict,bow=review
print('dict :',dict)
print('bow:' ,bow)