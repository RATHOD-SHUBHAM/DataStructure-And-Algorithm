# Tc and Sc: O(n)

from typing import List
class Solution:
    def nextGreaterElement(self, nums : List[int]) -> List[int]:
        n = len(nums)

        nge = [-1] * n

        st = [] # Monotonic Stack

        for i in reversed(range(n)):
            cur_num = nums[i]

            # Search for NGE in stack
            while st and cur_num >= st[-1]:
                st.pop()
            
            
            if not st:
                # We did not find NGE
                nge[i] = -1
            else:
                # We found NGE
                nge[i] = st[-1]
            
            # Append the cuurent value to stack
            st.append(cur_num)
        
        return nge
    

if __name__ == '__main__':
    obj = Solution()

    nums = [4, 12, 5, 3, 1, 2, 5, 3, 1, 2, 4, 6]

    print(obj.nextGreaterElement(nums=nums))
