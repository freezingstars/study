class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def showinfo(self):
        print(self.name, self.age)


P1 = Person("Tom", 20)
P1.showinfo()  # 调用方法
