nums1 = [1,2]
nums2 = [3,4]

def findMedianSortedArrays(nums1, nums2):
    merged = sorted(nums1 + nums2)
    lenght = len(merged)
    # print(merged, len(merged), len(merged) % 2, "ssss", merged[(lenght // 2)])

    if lenght % 2 == 1:
        return merged[(lenght // 2)]
    else:
        mid1 = merged[(len(merged) // 2) - 1]
        # print("!!!", mid1)
        mid2 = merged[len(merged) // 2]
        # print(mid1, mid2, "mid1 and mid2")
        return (mid1 + mid2)/2

findMedianSortedArrays(nums1, nums2)
print(findMedianSortedArrays(nums1, nums2))


# print(merged, len(merged), len(merged) % 2)
#
# # print(findMedianSortedArrays(nums1, nums2))
# print(len(nums1))
# print(len(nums1) % 2)
# print(len(nums1) // 2)
# print(len(nums2) % 2)
# print(len(nums2) // 2)
# print("govno", len(nums1) / 2)