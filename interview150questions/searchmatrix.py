matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 3





def searchMatrix(matrix, target):
    isFound = False
    for row in matrix:
        for num in row:
            if num == target:
                isFound = True
                break
            else:
                continue

    if isFound:
        return True
    else:
        return False


print(searchMatrix(matrix, target))
