from collections import defaultdict
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1 = len(nums1)
        n2 = len(nums2)

        op = []

        # keep track of the index
        dic = defaultdict(int)
        for i in range(n2):
            dic[nums2[i]] = i
        
        # print(dic)

        # Get the next greatest
        for i in range(n1):
            val = nums1[i]
            idx = dic[nums1[i]]

            for j in range(idx+1, n2):
                if nums2[j] > val:
                    op.append(nums2[j])
                    break
                
                if j == n2 - 1:
                    op.append(-1)
            
            if idx == n2 - 1:
                op.append(-1)
        
        # print(op)
        return op