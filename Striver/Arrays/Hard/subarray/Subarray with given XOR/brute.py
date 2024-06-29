from typing import List
class Solution:
    def subarray_xor(nums: List[int] , k : int) -> int:
        n = len(nums)

        count = 0

        for i in range(n):
            xor_sum = 0

            for j in range(i, n):
                xor_sum ^= nums[j]

                if xor_sum == k:
                    count += 1
            
        return count


if __name__ == '__main__':
    nums = [4, 2, 2, 6, 4]
    k = 6
    ans = Solution.subarray_xor(nums=nums, k = k)
    
    print("The number of subarrays with XOR k is:", ans)