def checkLuhn(cardNo):
    nDigits = len(cardNo)
    nSum = 0
    isSecond = False
     if len(cardNo) != 16 or not cardNo.isdigit():
        print("invalid input. Card number must be a 16-digit numeric string")
        return False
    for i in range(nDigits - 1, -1, -1):
        d = ord(cardNo[i]) - ord('0')
        if (isSecond == True):
            d = d*2
        
        nSum += d//10
        nSum += d%10
        
        isSecond = not isSecond
    return nSum % 10 == 0
            

if __name__ == "__main__":
    cardNo = input('Enter Card Number')
    if (checkLuhn(cardNo)):
        print("this is valid card")
    else:
        print("this is not a valid card")



