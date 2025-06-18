def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    if x < 0 or (x != 0 and x % 10 == 0):
        return False

    half = 0
    while half < x:
        half = (half * 10) + (x % 10)
        print(half, x)
        x = x // 10
        print(x)

    return x == half or x == half // 10


print(isPalindrome(121))
print(isPalindrome(12122))
print(isPalindrome(12321))