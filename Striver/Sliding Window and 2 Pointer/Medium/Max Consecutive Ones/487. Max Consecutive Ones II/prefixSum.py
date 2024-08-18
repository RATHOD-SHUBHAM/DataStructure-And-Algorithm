class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)

        cur_sum = 0 # total running sum
        prev_sum = 0 # Sum upto the previous zero

        cur_sum = max_sum = 0

        for num in nums:
            cur_sum += 1

            if num == 0:
                '''
                a + b = X
                b = X - a
                '''
                cur_sum = cur_sum - prev_sum # Window sum between 2 0s
                prev_sum = cur_sum
            
            max_sum = max(max_sum , cur_sum)
        
        return max_sum