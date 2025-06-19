def trailingZeroes(n):
    count = 0
    while n > 5:
        n = n // 5
        count += n
        print(count)
        print(n)
    return count

print(trailingZeroes(100))