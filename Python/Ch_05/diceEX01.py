import random


dice = random.randint(1,6)

bet = input("찍으세요")

if bet == dice:
    print("맞음")
else:
    print("안 맞음")
    
           
