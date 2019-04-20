def circle_area (r):
    global area
    area = 3.14 * r **2
    return
   

area = None
ban = float(input("반지름을 입력하세요"))
circle_area(ban)

print(area)


    

