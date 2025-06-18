x = 2
n = -2

def myPow(x, n):
    t = x
    if n < 0:
        n = n * -1
        for i in range(1, n):
            t = t * x
            print(t)
        print(t)
        t = 1 / t
        return t
    for i in range(1, n):
        t = t*x
    return t

print(pow(2, -200000000))

myPow(x, n)
print(myPow(x, n))
# print("result:", myPow(x, n))

twoin2 = 2*2
twoin5 = 2*2*2*2*2
# twoin10 = 2*
print(twoin2, twoin5)
print(pow(2, 2), pow(2, 5))