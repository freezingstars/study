<<<<<<< HEAD
# import math
# for i in range(100,1000):
#     a = math.floor(i / 100)
#     b = math.floor((i / 10) % 10)
#     c = math.floor(i % 10)
#     result = pow(a,3) + pow(b,3) + pow(c,3)
#     if i == result:
#         print(i)

for i in range(100, 1000):
    a = i // 100  # 百位
    b = (i // 10) % 10  # 十位
    c = i % 10  # 个位

    if a ** 3 + b ** 3 + c ** 3 == i:
        print(i)
=======
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def showScore(self):
        print(self.name+"考了",self.score)

P1 = Student("Tom", 80)
P1.showScore()
P1.score = 85
P1.showScore()
>>>>>>> c4c609fc246df5474980b41646a2acdf3db812f8
