class Animal:
    def __init__(self,name):
        self.name = name

    def run(self):
        print(self.name+" is running")

class Dog(Animal):
    def bark(self):
        print(self.name+" is barking")

dog = Dog("Dog")
dog.run()
dog.bark()