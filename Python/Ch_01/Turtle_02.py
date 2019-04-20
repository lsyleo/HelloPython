import turtle
run = 1
t = turtle.Turtle()
t.shape("arrow")
pen = 1

while run == 1:
    command = input("")
    d = t.degrees
    

    
    if command == "w":
        
        t.forward(10)
    if command == "s":
        t.backward(10)
    if command == "d":
        
        t.right(20)
    if command == "a":
        t.left(20)
    if command == " " & pen == 1:
        t.up()
        pen = 0
    if pen == 0:
        if command == " " & pen == 0:
            t.down
            pen = 1
    
    
    
