from random import random


user = input("홀,짝을 입력하시오")
com = ""
res = ""
ran = random()
if ran > 0.5 :
    com = "홀"
else:
    com = "짝"
    
if user == com:
    res = "이김"
else :
    res = "짐"

print("나 :" + user)
print("com :" + com)
print("결과 :" + res)
