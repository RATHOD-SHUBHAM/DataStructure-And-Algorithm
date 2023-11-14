# Mode calculation

# Tc and Sc: O(n)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = {}

        n = len(nums)

        for i in range(n):
            cur_num = nums[i]

            if cur_num in dic:
                dic[cur_num] += 1
            else:
                dic[cur_num] = 1
        
        return max(dic)
        