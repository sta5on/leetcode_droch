nums1 = [0, 1,3]
nums2 = [2,4,5,6,7,8,9]


def medianInTwoSorted(nums1, nums2):
    matrix = sorted(nums1 + nums2)
    print(f"matrix is: {matrix}, and this len is {len(matrix)}, {len(matrix) // 2}, {matrix[len(matrix) // 2]}")
    if len(matrix) % 2 == 1:
        medianis = matrix[len(matrix) // 2]
        return medianis
    else:
        mid1 = matrix[(len(matrix) // 2) - 1]
        mid2 = matrix[len(matrix) // 2]
        mid = (mid1 + mid2) / 2
        return mid

print(f"function, {medianInTwoSorted(nums1, nums2)}")