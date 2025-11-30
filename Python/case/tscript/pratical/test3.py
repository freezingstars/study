class Person:
    def __init__(self, name):
        self.name = name
    def show(self):
        print("姓名：", self.name)

class Student(Person):   # 继承 Person
    def study(self):
        print(f"{self.name} 正在学习")

stu = Student("Tom")
stu.show()   # 调用父类方法
stu.study()