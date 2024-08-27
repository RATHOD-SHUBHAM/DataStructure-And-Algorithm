from typing import List

class Solution:
    def prevSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)

        stack = []

        op = [-1] * n

        for i in range(n):
            cur_ele = nums[i]

            while stack and cur_ele <= stack[-1]:
                stack.pop()
            
            if not stack:
                op[i] = -1
            else:
                op[i] = stack[-1]
            

            stack.append(cur_ele)
        
        return op

if __name__ == '__main__':
    obj = Solution()

    # nums = [4, 5, 2, 10, 8]
    # nums = [3,2,1]
    nums = [1,1,2,2,3,3]

    print(obj.prevSmaller(nums=nums))