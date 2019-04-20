import random


dice = random.randint(1,6)
isGood = False

while isGood == False:
    
    bet = int(input("찍으세요"))

    if dice == bet:
        print("맞음")
        isGood = True
    
    else:
        print("안 맞음")
        
    
           
