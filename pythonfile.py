print("hello world")

hi = "hi"
print(hi)

def hi_muthaphucka():
    print("hi muthaphucka")

hi_muthaphucka()

class Pet():
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def show_age(self):
        print(self.age)

    def show_name(self):
        print(self.name)
    

doggie = Pet("Oliver", 4)
doggie.show_age()
doggie.show_name()
