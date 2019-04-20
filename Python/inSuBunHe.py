

isGood = False
fNum = 0
sNum = 0
tNum = 0
divNum = [1,0]
wasNeg = False

while True:
    
    fNum = int(input("이차항의 계수 :"))
    #이차항 계수 입력
    if fNum <0:
        wasNeg = True

    if fNum == 0:

        while True:
            
            print("이차항의 계수는 0이 될 수 없습니다")
            fNum = int(input("이차항의 계수 :"))

    #이차항 계수 입력 완료
    sNum = int(input("일차항의 계수 :"))
    #일차항 계수 입력

    tNum = int(input("상수항의 계수 :"))
    #상수항 계수 입력

    #합차 공식 일때
    if sNum == 0 and fNum ==1:
        print("(x+"+str(tNum**0.5)+")(x-"+str(tNum**0.5)+")")
        
    #완전 제곱식 일때    
    elif fNum == 1 and sNum / 2 ** 2 == tNum and tNum > 0:

        if fNum < 0:
            print("x"+str(int(tNum))+")²")
        else:
            print("x+"+str(int(tNum))+")²")

    #ax²+ (a+b)x + ab꼴의 식
    elif fNum == 1:
        if wasNeg == True:

            tNum *= -1

        while divNum[0] + divNum[1] != sNum or isGood ==True :

            if tNum % divNum[0] == 0:

                divNum[1] = tNum / divNum[0]

            else:

                divNum[0] += 1
           

            if tNum <= divNum[0] :

                isGood = True

    #출력
        if divNum[0] < 0:

            print("(x"+str(divNum[0])+")(x+"+str(divNum[1])+")")
                
        elif divNum[1] < 0:

            print("(x+"+str(divNum[0])+")(x"+str(divNum[1])+")")

        elif divNum[0] < 0 and divNum[1] < 0:

            print("(x"+str(divNum[0])+")(x"+str(divNum[1])+")")

        elif divNum[0] < 0 and divNum[1] < 0:

            print("(x+"+str(divNum[0])+")(x+"+str(divNum[1])+")")
            
    

        
        
        
    
               
