from typing import List

class Solution:
    def nse(self, nums: List[int]) -> List[int]:
        n = len(nums)

        stack = []

        op = [-1] * n

        for i in reversed(range(n)):
            cur_ele = nums[i]

            while stack and cur_ele < stack[-1]:
                stack.pop()
            
            if not stack:
                op[i] = -1
            else:
                op[i] = stack[-1]
            
            stack.append(cur_ele)
        
        return op

        

if __name__ == '__main__':
    obj = Solution()

    # nums = [4, 8, 5, 2, 25]
    nums = [13, 7, 6, 12]

    print(obj.nse(nums=nums))