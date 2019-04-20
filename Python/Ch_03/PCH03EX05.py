




x1 = int(input("x1입력"))
y1 = int(input("y1입력"))
x2 = int(input("x2입력"))
y2 = int(input("y2입력"))
distance = ((x1-x2)**2 + (y1-y2)**2)**0.5


import turtle

t = turtle.Turtle()
t.shape("arrow")



t.up()
t.goto(x1,y1)
t.down()
t.goto(x2,y2)

t.goto(x1,y1)
t.forward(x2)
t.left(90)
t.forward(y2)





