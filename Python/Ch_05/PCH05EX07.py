import random

lottNum = random.randint(10,99)
lottN_1 = lottNum // 10
lottN_2 = lottNum & 10

userN = int(input("복권 번호를 입력하세요(0~99)"))


if lottNum == userN :
    print("당첨입니다")
    print("상금 100")
elif (lottN_1 == userN % 10 or lottN_1 == userN // 10) or (lottN_2 == userN // 10 or lottN_2 == userN % 10):
    print("당첨입니다")
    print("상금 50")
else:
    print("탈락")


    
