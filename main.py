from functions import*
Id=input("id:")
Pw=input("pw:")
classnum=input("강평번호를 입력하세요:")
driver = login(Id,Pw)
review=get_review(driver,classnum)
token=get_token(review)
print(token[:10])
