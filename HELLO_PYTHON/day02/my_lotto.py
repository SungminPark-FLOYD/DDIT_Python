from random import random


aa = [
    1,2,3,4,5, 6,7,8,9,10,
    11,12,13,14,15, 16,17,18,19,20,
    21,22,23,24,25, 26,27,28,29,30,
    31,32,33,34,35, 36,37,38,39,40,
    41,42,43,44,45
    ]

for i in range(1000):
    ran = int(random()*45)
    a = aa[0]
    aa[0] = aa[ran]
    aa[ran] = a


# print(aa[0],end=" ")
print(aa[0], aa[1],aa[3],aa[4],aa[5],aa[6])