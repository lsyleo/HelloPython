col1 = input("색상 #1 :")
col2 = input("색상 #2 :")
col3 = input("색상 #3 :")

import turtle

t = turtle.Turtle()
t.shape("turtle")

t.fillcolor(col1)
t.begin_fill()
t.circle(50)
t.end_fill()
t.up()
t.forward(100)
t.down()

t.fillcolor(col2)
t.begin_fill()
t.circle(50)
t.end_fill()
t.up()
t.forward(100)
t.down()

t.fillcolor(col3)
t.begin_fill()
t.circle(50)
t.end_fill()
t.up()

