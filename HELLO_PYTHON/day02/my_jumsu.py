from random import random

jumsu = random()*100 + 1

print(int(jumsu))

for i in range(2000+1):
    res = int(random()*101)
    print(res)
    if res == 0:      
        break
    elif res == 99:
        break