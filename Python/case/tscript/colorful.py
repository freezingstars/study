class Car:
    def __init__(self, color,speed):
        self.color = color
        self.speed = speed
    def run(self):
        print("{}None!{}".format(self.color, self.speed))
car = Car("red",100)
car.run()
car.color = "blue"
car.speed = 80
car.run()

