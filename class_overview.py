class Person:
    def __init__(self,gender,name):
        self.gender = gender
        self.name = name
    def display(self):
        print("You're a ", self.gender ,", and you're name is:", self.name)
        
man = Person('Male', 'Alex')
woman = Person('Female', 'Joan')
man.display()
woman.display()