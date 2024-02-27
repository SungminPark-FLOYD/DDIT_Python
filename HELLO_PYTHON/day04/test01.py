from day04.my_oop import Trump, Biden
class Ji(Trump,Biden):
    def __init__(self):
        Trump.__init__(self)
        Biden.__init__(self)
    
    def fire_alz(self):
        self.alz()
        self.you_fire()
        
        print("Ji : ", self.money)
        print("Ji : ",self.memory)
        


ji = Ji()
print(ji.money)
print(ji.memory)

ji.alz()
ji.you_fire()

print(ji.money)
print(ji.memory)

ji.fire_alz()
