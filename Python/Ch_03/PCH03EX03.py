num = int(input("정수를 입력하세요"))
num1 = num % 10

num2 = (num //10) % 10

num3 = (num //100) % 10

num4 = (num //1000) % 10


print("자릿수의 합",num1 + num2 + num3 + num4)
