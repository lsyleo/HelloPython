import time

seconds = time.time()
hour = seconds / 60 % 24
min_ = seconds / 60 % 60

print("현제 시간" + str(int(hour)) +"시" + str(int(min_)) +"분")
