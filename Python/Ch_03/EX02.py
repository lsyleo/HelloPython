ame_price = 2000
latte_price = 300
capu_price = 3500


ame_cups = int(input("아메리카노 판매수를 입력하세요"))

latte_cups = int(input(",카페라떼의 판매수를 입력하세요"))

capu_cups = int(input("카푸치노의 판매수를 입력하세요"))

sum_all = 0

sum_all = ame_price * ame_cups
sum_all += latte_price * latte_cups
sum_all += capu_price * capu_cups

print("총 매출은",sum_all,"\ 입니다")
