# Time = O(n^4) Space = O(n)

class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        res = []
        count = 0

        for i in range(len(nums)- 3):
            for j in range(i+1, len(nums)-2):
                for k in range(j+1, len(nums) - 1):
                    for d in range(k+1, len(nums)):
                        if ( nums[i] + nums[j] + nums[k] == nums[d] ):
                            count += 1

        return count