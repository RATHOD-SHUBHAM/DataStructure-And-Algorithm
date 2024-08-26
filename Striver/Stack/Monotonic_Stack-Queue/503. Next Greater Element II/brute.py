# Tc: O(n^2) | Sc: O(n)

# Circular Array Concept

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)

        nge = [-1] * n

        for i in range(n):
            cur_num = nums[i]

            for j in range(i + 1, i + n):
                idx = j % n # Circular array index
                nxt_num = nums[idx]

                if nxt_num > cur_num:
                    nge[i] = nxt_num
                    break
        
        return nge