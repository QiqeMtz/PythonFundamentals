class Shark:
    def __init__(self, name, age):
        print("This is the constructor method")
        self.name = name
        self.age = age
    def swim(self):
        print(self.name, "The shark is swimming")
    def be_awesome(self):
        print(self.name,"The shark is being awesome")
    def info(self):
        print(self.name, "has", self.age, "years old")