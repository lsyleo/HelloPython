isGood = 0
tryPassword = 0
password = 0
angle = 10
distence = 20
color = "black"
width = 1

password = input("비밀번호 설정")

while isGood == 0:
    tryPassword = input("비밀번호")
    if tryPassword ==  password:
        isGood = 1
  
while isGood == 1:
    import turtle

    t = turtle.Turtle()
    t.shape("turtle")

    running = 1
    isUP = 0
    command =""

    while running == 1:
        command = input("")
        if command == " ":
            if isUP == 0:
                t.up()
                print(isUP)
                isUP = 1
            if isUP == 1:
                t.down()
                print(isUP)
                isUP = 0
        if command == "w":
            t.forward(distence)
        if command == "s":
            t.backward(distence)
        if command == "a":
            t.left(angle)
        if command == "d":
            t.right(angle)
        if command == "clear":
            t.clear()
        if command == "goto":
            gotoX = int(input("이동할x좌표"))
            gotoY = int(input("이동할y좌표"))
                        
            t.goto(gotoX,gotoY)
        if command == "distence":
            distence = int(input("변경할 길이를 입력하세요"))
        if command == "angle":
            angle = int(input("변경할 각도를 입력하세요"))
        if command == "color":
            color = input("변경할 색상를 입력하세요")
            t.color(color)
        if command == "width":
            width = int(input("변경할 두께를 입력하세요"))
            t.width(width)
        if command == "exit_":
            running = 2
        if command == "clone":
            t.clone()
        
            
                           
            
        
        
        
            
    
    
    




