import turtle
turtle.screensize(600, 600,'white')
turtle.setup(width=600, height=600)
turtle.shape('turtle')
turtle.colormode(255.0)
turtle.pencolor(79,79,79)
turtle.pensize(1)
turtle.goto(0,0)
turtle.pendown()
turtle.speed(20)
for i in range(100):
    turtle.forward(i*4)
    turtle.left(120)
turtle.done()