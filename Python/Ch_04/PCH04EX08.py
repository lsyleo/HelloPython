import turtle
t= turtle.Turtle()
t.shape("turtle")

loca = [ 0 , 0 , 0 , 0 , 0 , 0 ]

loca[0] = int(input("x1 :"))
loca[1] = int(input("y1 :"))
loca[2] = int(input("x2 :"))
loca[3] = int(input("y2 :"))
loca[4] = int(input("x3 :"))
loca[5] = int(input("y4 :"))

t.goto(loca[0],loca[1])
t.goto(loca[2],loca[3])
t.goto(loca[4],loca[5])
