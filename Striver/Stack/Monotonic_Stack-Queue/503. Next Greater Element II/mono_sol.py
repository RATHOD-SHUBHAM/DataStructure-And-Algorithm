# Tc and Sc: O(n)

# Circular Array Concept

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)

        nge = [-1] * n

        st = [] # Monotonic Stack

        cn = 2 * n #ciruclar_array_idx

        for i in reversed(range(cn)):
            idx = i % n 
            cur_num = nums[idx]
            
            while st and cur_num >= st[-1]:
                st.pop()
            
            if idx < n:
                if not st:
                    nge[idx] = -1
                else:
                    nge[idx] = st[-1]
            
            st.append(cur_num)
        
        return nge

            