import random

problem1 = random.randint(1,100)
problem2 = random.randint(1,100)

answer = problem1 - problem2


print(problem1,"-",problem2,"=")

ans = int(input("답은?"))

if answer ==  ans:
    print("정답")
else:
    print("오답")

