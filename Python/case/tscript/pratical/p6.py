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