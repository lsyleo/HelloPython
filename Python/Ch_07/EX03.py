def sum_all (s):
    sum_result = 0
    for i in s:
        sum_result += i
   
    return sum_result
a = [1,3,5,6]

result = sum_all(a)

print(result)

b = []
import random

for i in range(10):
    num = random.randint(1,100)
    b.append(num)
result_b = sum_all(b)
print("리스트의 합",result_b)
   



    

