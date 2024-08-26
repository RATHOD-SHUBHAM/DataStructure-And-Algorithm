# Tc: O(n) | Sc: O(n)

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m = len(nums1)
        n = len(nums2)

        dic = collections.defaultdict(int)
        for idx, val in enumerate(nums1):
            dic[val] = idx
        
        nge = [-1] * m

        stack = [] # monotonic stack

        for i in reversed(range(n)):
            cur_num = nums2[i]

            while stack and cur_num >= stack[-1]:
                stack.pop()
            
            if cur_num in dic:
                idx = dic[cur_num]
                if not stack:
                    nge[idx] = -1
                else:
                    nge[idx] = stack[-1]
            
            stack.append(cur_num)
        
        return nge

