import math

n = 100

def trailingzero(n):
    count = 0
    n1 = n
    while n > 5:
        n = n // 5
        count += n
    # print(f"count of 0 in factoril {n1} is {count}")
    return count


for n in range(1, 100):
    print(f"factrial from {n}, is {math.factorial(n)}")
print(math.factorial(10))
trailingzero(n)
