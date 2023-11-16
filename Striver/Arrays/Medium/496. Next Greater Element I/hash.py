class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1 = len(nums1)
        n2 = len(nums2)

        nextGreater = []

        idx_dict = collections.defaultdict()

        for i in range(n2):
            idx_dict[nums2[i]] = i
        
        for i in range(n1):
            idx_of_nums2 = idx_dict[nums1[i]]
            
            if idx_of_nums2 == n2 - 1:
                nextGreater.append(-1)
                continue


            for j in range(idx_of_nums2 + 1, n2):
                if nums2[j] > nums1[i]:
                    nextGreater.append(nums2[j])
                    break

                if j == n2 - 1:
                    nextGreater.append(-1)
                    break

        return nextGreater