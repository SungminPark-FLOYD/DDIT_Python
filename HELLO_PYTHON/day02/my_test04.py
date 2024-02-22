#가위, 바위, 보를 입력하시오 
# 나 : 가위
# com : 바위
# 결과 : 짐
from random import random

user = ""
com = ""
res = ""

user = input("가위, 바위, 보를 입력하시오 ")
ran = random()

if ran > 0.66:
    com = "보"
    if user == "가위":
        res = "이김"
    elif user == "바위":
        res = "짐"
    elif user == "보" :
        res = "비김"
elif ran > 0.33:
    com = "바위"
    if user == "가위":
         res = "짐"
    elif user == "바위":
        res = "비김"
    elif user == "보" :
        res = "이김"
else:
    com = "가위"
    if user == "가위":
        res = "비김"
    elif user == "바위":
        res = "이김"
    elif user == "보" :
        res = "짐"
        
print("나 : " + user)
print("com : " + com)
print("결과 : " + res)
    
