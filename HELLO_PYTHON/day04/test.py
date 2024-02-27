class Trump:
    def __init__(self):
        self.money = 1000
        
    def you_fire(self):
        self.money += 1
        
class Biden:
    def __init__(self):
        self.memory = 100
        
    def alz(self):
        self.memory /= 2
        

class Jihun(Trump, Biden):
    def __init__(self):
        Trump.__init__(self)
        Biden.__init__(self)
        
    def fire_alz(self):
        self.alz()
        self.you_fire()
        
        print("Ji : ", self.money)
        print("Ji : ",self.memory)

ji = Jihun()
print(ji.money)
print(ji.memory)

ji.alz()
ji.you_fire()

print(ji.money)
print(ji.memory)

ji.fire_alz()


