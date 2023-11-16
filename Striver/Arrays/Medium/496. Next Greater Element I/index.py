class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1 = len(nums1)
        n2 = len(nums2)

        nextGreater = []

        for i in range(n1):
            idx_in_nums2 = nums2.index(nums1[i])

            if idx_in_nums2 == n2 - 1:
                nextGreater.append(-1)
                continue

            for j in range(idx_in_nums2, n2):
                if j == n2 - 1 and nums2[j] < nums1[i]:
                    nextGreater.append(-1)
                    break
                if nums2[j] > nums1[i]:
                    nextGreater.append(nums2[j])
                    break

        print(nextGreater)

        return nextGreater