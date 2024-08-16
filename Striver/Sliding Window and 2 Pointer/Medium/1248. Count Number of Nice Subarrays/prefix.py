class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)

        dic = {0:1}

        cur_sum = total = 0

        for i in range(n):
            if nums[i] % 2 != 0:
                cur_sum += 1
            
            diff = cur_sum - k

            if diff in dic:
                total += dic[diff]
            
            if cur_sum in dic:
                dic[cur_sum] += 1
            else:
                dic[cur_sum] = 1
        
        return total