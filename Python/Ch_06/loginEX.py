userName="미래"
password = "1234"
Good = False

while True:
    while Good == False:
        name = input("ID : ")
        if name != userName:
            print("ID가 맞지 않습니다")
        else:
            Good = True
        
    Good = False
        
    while Good == False:
        pas = input("password : ")
        if pas == password:
            Good = True
    break
        
            

    
