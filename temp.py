class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
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