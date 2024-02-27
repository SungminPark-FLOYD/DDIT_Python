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
        

class Me(Trump, Biden):
    def __init__(self):
        Trump.__init__(self)
        Biden.__init__(self)
    
    

if __name__ == '__main__':
    
    me = Me()
    print(me.memory)
    print(me.money)
    
    me.you_fire()
    me.alz()
    
    print(me.memory)
    print(me.money)
