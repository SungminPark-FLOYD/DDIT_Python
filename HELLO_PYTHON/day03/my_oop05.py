class dog:
    def __init__(self):
        self.name = "바둑이"
        print("생성자")
        
    def bark(self):
        print("멍멍")
        
    def __del__(self):
        print("소멸자")
      
    # def __str__(self):
    #     return "Dog" + self.name
        
if __name__ == '__main__':
    dog = dog()
    print(dog.name)
    dog.bark()
    print(dog)