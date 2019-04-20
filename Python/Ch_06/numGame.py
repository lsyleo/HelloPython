import random

com_num = random.randint(10,99)
us_num = 0
count = 0

while True:
    count += 1
    us_num = int(input("숫자를 입력하세요"))

    if us_num == com_num:
        print("정답")
        break
    elif us_num < com_num:
        print("적습니다 큰수를 입력하세요")
    else :
        print("큽니다 작은수를 입력하세요")

print(count,"만에 맞에 맞추셨네요")
    
                 

