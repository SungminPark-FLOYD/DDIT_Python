#첫수를 입력하시오 1
#끝수를 입력하시오 4
#1에서 4까지의 합은 10입니다

f = ""
e = ""
res = 0

f = input("첫수를 입력하시오")
e = input("끝수를 입력하시오")

fir = int(f)
end = int(e)

for i in range(fir, end+1) :
    res += i
    
print("{}에서 {}까지의 합은 {}입니다".format(fir, end, res))
