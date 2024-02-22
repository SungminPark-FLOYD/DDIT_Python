from random import random
arr = [1,2,3,4,5]

for i in range(10):
    ran = int(random()*5)
    f = arr[0]
    arr[0] = arr[ran]
    arr[ran] = f
    
print(arr[0], arr[1], arr[2])


