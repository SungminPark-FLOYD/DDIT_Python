#첫수를 입력하세요 1
#끝수를 입력하세요 10
#배수를 입력하시오 5
#1에서 10까지 5의 배수의 합은 15입니다.

f = ""
e = ""
d = ""
res = 0;
f = int(input("첫수를 입력하세요"))
e = int(input("끝수를 입력하세요"))
d = int(input("배수를 입력하시오"))

for i in range(f, e+1):
    if i%d == 0:
        res += i
        

print("{}에서 {}까지 {}의 배수의 합은 {}입니다.".format(f, e, d, res))