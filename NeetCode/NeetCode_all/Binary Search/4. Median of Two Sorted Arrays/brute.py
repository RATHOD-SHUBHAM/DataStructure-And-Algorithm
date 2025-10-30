class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = nums1 + nums2

        merged.sort()

        n = len(merged)

        left = 0
        right = n - 1
        mid = left + (right - left) // 2

        if n % 2 == 1:
            return merged[mid]
        else:
            median = (merged[mid] + merged[mid + 1]) / 2
            return median