year = int(input("년도를 입력하세요"))

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("윤년 입니다")
else :
    print("평년 입니다")


