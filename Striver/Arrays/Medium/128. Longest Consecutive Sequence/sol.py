'''
    Set + reverse search
'''
# Sc: O(n) | Tc : O(n)

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)

        if n < 1:
            return 0

        set_nums = set(nums)

        max_sequence = 0
        cur_sequence = 1

        for i in range(n):
            cur_num = nums[i]

            if cur_num - 1 not in set_nums:
                start_num = cur_num
                cur_sequence = 1

                while start_num + 1 in set_nums:
                    start_num = start_num + 1
                    cur_sequence += 1
            
            max_sequence = max(max_sequence, cur_sequence)

        return max_sequence 