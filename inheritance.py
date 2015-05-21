class Animals:
    def eat(self):
        print('I can eat')
    def talk(self):
        print('I can talk')

class Cat(Animals):
    def talk(self):
        print('Meow')
    def move(self):
        print('I can move')
        
class Dog(Animals):
    def talk(self):
        print('Woof')
        
muffin = Cat()
sky = Dog()
sky.talk()
super(Dog, sky).talk()
muffin.eat()
muffin.talk() # The talk method in the parent Class 'Animals' has been overridden by the talk method in the child Class 'Cat'.
muffin.move()
super(Cat,muffin).talk() # If you want to instead use the parent method that had been overridden, this is how you use super().

# For what it's worth, the Python documentation on super() might be a bit advanced for this lecture, but basically the muffin.super().talk() call can never work 
# because super() is not a Cat class method; the fact that "super" is reserved does not change this. From the interpreter's perspective--which is just the top-level 
# module--super() needs to be run with the proper arguments so that it knows which class to track back through and through which instance/object. 
# The right way to execute the above expression from the interpreter's context is:
# 
# >>> super(Cat,muffin).talk()