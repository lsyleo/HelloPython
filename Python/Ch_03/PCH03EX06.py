import turtle

t = turtle.Turtle()
t.shape("arrow")



x1 = int(turtle.textinput("","x1입력"))
y1 = int(turtle.textinput("","y1입력"))
x2 = int(turtle.textinput("","x2입력"))
y2 = int(turtle.textinput("","y2입력"))
distance = ((x1-x2)**2 + (y1-y2)**2)**0.5


t.up()
t.goto(x1,y1)
t.down()
t.goto(x2,y2)



t.write("선의 길이 :"+ str(distance))
