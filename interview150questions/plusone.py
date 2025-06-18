digits1 = [1, 2, 3]
digits2 = [1, 2, 9]
digits3 = [9, 9, 9]
digits4 = [9]
digits5 = [9, 9]

def plusOne(digits):
    lenOfDigits = len(digits) - 1
    if 0 <= digits[lenOfDigits] <= 8:
        digits[lenOfDigits] = digits[lenOfDigits] + 1
    if digits[lenOfDigits] == 9:
        for i in range(lenOfDigits + 1):
            print(digits[i])
            if digits[i] == 9:
                digits[i] = 0
                digits[i - 1] = digits[i - 1] + 1
                if lenOfDigits == 0:
                    digits.append(0)
                    print(digits)
                print(digits)
            if digits[i] == 10:
                digits[i] = 0
                digits[i - 1] += 1
                # if digits[i - 1]:
                #     digits[i - 1] += 1
                digits.append(0)
                print(digits)

    print(digits)

plusOne(digits1)
plusOne(digits2)
plusOne(digits3)
print("hu")
plusOne(digits4)
plusOne(digits5)