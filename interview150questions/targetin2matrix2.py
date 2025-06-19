matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
matrix2 = [[1, 3]]
target = 3

def findtarget(matrix, target):
    isFound = False
    for row in matrix:
        for num in row:
            if num == target:
                isFound = True
                break
            else:
                continue
        if isFound:
            return isFound
        else:
            return False



print(f"is found? - {findtarget(matrix2, target)}")