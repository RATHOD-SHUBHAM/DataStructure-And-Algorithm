# from typing import List
# class Solution:
#     def subarray_xor(nums: List[int] , k : int) -> int:
#         n = len(nums)
#         dic = {0 : 1}
#         xor = 0
#         count = 0

#         for i in range(n):
#             xor ^= nums[i]

#             diff = k ^ xor

#             if diff in dic:
#                 count += dic[diff]
            
#             if xor in dic:
#                 dic[xor] += 1
#             else:
#                 dic[xor] = 1
        
#         return count




# if __name__ == '__main__':
#     nums = [4, 2, 2, 6, 4]
#     k = 6
#     ans = Solution.subarray_xor(nums=nums, k = k)
    
#     print("The number of subarrays with XOR k is:", ans)


# ----------------------------------------------------------------

from typing import List
from collections import defaultdict

class Solution:
    def subarray_xor(nums: List[int] , k : int) -> int:
        n = len(nums)

        dic = defaultdict(int)
        dic[0] = 1

        xor = 0
        count = 0

        for i in range(n):
            xor ^= nums[i]

            diff = k ^ xor

            if diff in dic:
                count += dic[diff]
            
            dic[xor] += 1
        
        return count




if __name__ == '__main__':
    nums = [4, 2, 2, 6, 4]
    k = 6
    ans = Solution.subarray_xor(nums=nums, k = k)
    
    print("The number of subarrays with XOR k is:", ans)