def add(a,b,sym):

    if sym == "+":
        print(a,sym,b,"=",a+b)

    if sym == "-":
        print(a,sym,b,"=",a-b)

    if sym == "*":
        print(a,sym,b,"=",a*b)

    if sym == "/":
        print(a,sym,b,"=",a/b)

first = int(input("첫번째 정수를 입력해보거라 :"))
sym = input("기호를 입력해 보거라 :")
secon = int(input("두번째 정수를 입력해보거라 :"))

add(first,secon,sym)
