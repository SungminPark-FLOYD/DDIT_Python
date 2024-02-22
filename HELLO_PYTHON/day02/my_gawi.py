from random import random

ran = random()

answer = input("가위, 바위, 보 를 입력하세요")

if answer == "가위":
    if ran < 0.3 :
        print("비겼습니다")
    elif ran < 0.6:
        print("졌습니다")
    else:
        print("이겼습니다")
elif answer == "바위":
    if ran < 0.3 :
        print("이겼습니다")
    elif ran < 0.6:
        print("비겼습니다")
    else:
        print("패배")
elif answer == "보":
    if ran < 0.3 :
        print("패배")
    elif ran < 0.6:
        print("승리")
    else:
        print("비김")