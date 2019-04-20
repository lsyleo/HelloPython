import random

position =["가운데","왼쪽","오른쪽"]

com_pos = random.choice(position)

kick = input("찰 곳을 정하세요(왼쪽|가운데|오른쪽)")

if kick == com_pos:
    print("No goal")
elif kick != com_pos:
    print("Goal")
    
           
