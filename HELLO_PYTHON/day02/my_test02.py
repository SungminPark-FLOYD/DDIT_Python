#숫자를 입력하시오 5
#입력하신 숫자 5 는 3의 배수가 아닙니다.
#입력하신 숫자 6은 3의 배수 입니다.

num = ""
num = int(input("숫자를 입력하시오"))

if num%3 == 0:
    print("입력하신 숫자 {}는 3의 배수입니다".format(num))
else:
    print("입력하신 숫자 {}는 3의 배수가 아닙니다".format(num))

