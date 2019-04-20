def circleArea(r):
    area = PI * r**2
    print("반지름이",r,"인 원의 면적은",area)

def circleCircumfererence(r):
    area = 2 * PI * r
    print("반지름이",r," 인 원의 면적은",area)

PI = 3.14
radi = int(input("반지름을 입력하거라 :"))
a = circleArea(radi)
b = circleCircumfererence(radi)

