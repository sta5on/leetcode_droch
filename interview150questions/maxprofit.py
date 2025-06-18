prices = [7, 1, 5, 3, 6, 4]

def maxProfit(prices):
    minim = 1
    tempminim = 1
    profit = 0
    temp = 0
    for num in prices:
        print(num)
        if num > temp:
            temp = num
        print("temp", temp)
        if num < temp:
            tempminim = num
            if tempminim < minim:
                minim = tempminim
            print("MIN:", minim)

    minPrice = minim
    position = prices.index(minPrice) + 1
    print(minPrice, position)
    print(len(prices))
    if position < len(prices) and position != len(prices):
        for num in range(position, len(prices)):
            if prices[num] > minPrice:
                temp = prices[num] - minPrice
                if temp > profit:
                    profit = temp
                print("for now", temp, "profit ", profit)
            else:
                continue
        return profit
    else:
        return 0



maxProfit(prices)

# print("final profit: ", maxProfit(prices))