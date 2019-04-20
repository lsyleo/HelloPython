import turtle

t = turtle.Turtle()
t.speed(10000000000000000)
shape = int(input("몇각형 입니까?"))
forw = 0
angle = 360 / shape
t.shape("turtle")

if shape <= 10 :
    forw = 100
else :
    forw = 50
    
for shape in range(shape):
    t.forward(forw)
    t.left(angle)
