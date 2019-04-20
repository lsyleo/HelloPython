#count = 1
#sum_all = 0
#while count <= 10:
 #   sum_all += count
  #  count += 1
#print("합계",sum_all)

count = 1
sum_all = 0


while True:
    num = int(input("숫자를 입력하세요"))
    sum_all += num
    no = input("계속?(yes|no)")
    if no == "no" :
        break
    count += 1
avg = sum_all / count
print("합계",sum_all)
print("평균",avg)
    
    

