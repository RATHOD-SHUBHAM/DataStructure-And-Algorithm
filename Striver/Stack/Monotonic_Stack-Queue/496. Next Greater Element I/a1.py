# ----------------------  Dictionary ----------------------

# Tc: O(m + n) | Sc: O(m + n)

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m = len(nums1)
        n = len(nums2)

        dic= collections.defaultdict(int)

        for idx, val in enumerate(nums2):
            dic[val] = idx

        op = [-1] * m

        for i in range(m):
            max_val = nums1[i]

            idx_2 = dic[max_val]

            # Look on right for every element
            for j in range(idx_2 + 1, n):
                cur_val = nums2[j]

                if cur_val > max_val:
                    max_val = cur_val
                    break
            
            if max_val != nums1[i]:
                op[i] = max_val
        
        return op
    
# ----------------------  Index ----------------------

# Tc: O(m + n) | Sc: O(m + n)

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m = len(nums1)
        n = len(nums2)

        op = [-1] * m

        for i in range(m):
            max_val = nums1[i]

            idx_2 = nums2.index(max_val)

            # Look on right for every element
            for j in range(idx_2 + 1, n):
                cur_val = nums2[j]

                if cur_val > max_val:
                    max_val = cur_val
                    break
            
            if max_val != nums1[i]:
                op[i] = max_val
        
        return op
    

# ----------------------  Monotonic Stack ----------------------

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


