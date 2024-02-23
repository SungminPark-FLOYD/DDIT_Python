from day03.my_oop01 import Animal

class Human(Animal):
    
    def __init__(self):
        super().__init__()
        self.skill_cook = 0
        
    def element(self):
        self.skill_cook += 1
        

if __name__ == '__main__':           
    hum = Human();
    
    print(hum.x);
    print(hum.y);
    print(hum.skill_cook)
    
    hum.moveX(5)
    hum.moveY(5)
    hum.element()
    
    print(hum.x);
    print(hum.y);
    print(hum.skill_cook)