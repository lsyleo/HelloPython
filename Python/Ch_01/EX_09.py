import turtle

t = turtle.Turtle()
t.shape("turtle")

num1 = 1

location = 150

while num1 <= 3 :
    t.circle(100)
    t.up()
    t.goto(location,0)
    t.down()
    location += 150
    num1 += 1

t.up()
t.goto(75,-150)
t.down()
t.circle(100)
t.up()
t.goto(225,-150)
t.down()
t.circle(100)

