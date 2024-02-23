from day03.my_oop01 import Animal
from day03.my_oop02 import Human


ani = Animal()
print("T",ani.x)
print("T",ani.y)

ani.moveX(5)
ani.moveY(5)

print("T",ani.x)
print("T",ani.y)

hum = Human()
print(hum.x)
print(hum.y)
print(hum.skill_cook)

hum.moveX(5)
hum.moveY(5)
hum.element()

print(hum.x)
print(hum.y)
print(hum.skill_cook)



