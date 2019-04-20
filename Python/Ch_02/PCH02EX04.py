import turtle

radius = 50

t = turtle.Turtle()
t.shape("turtle")

t.circle(radius)
t.up()
t.goto(100,0)

t.down()
radius += 20
t.circle(radius)
t.up()
t.goto(200,0)

t.down()
radius += 20
t.circle(radius)

