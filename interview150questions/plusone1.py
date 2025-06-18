digits1 = [1, 2, 3]
digits2 = [1, 2, 9]
digits3 = [9, 9, 9]
digits4 = [9]
digits5 = [9, 9]

def plusOne(digits):
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0
    return [1] + digits

print(plusOne(digits1))
print(plusOne(digits2))
print(plusOne(digits3))
print(plusOne(digits4))
print(plusOne(digits5))