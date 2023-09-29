# Tc: O(n^3) | Sc: O(1)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_sequence = -math.inf

        # O(n)
        for n in nums:
            cur_ele = n
            next_ele = cur_ele + 1

            cur_sequence = 1

            '''
                Loop runs through all the input everytime we increase the next element count
                O(n^2)
            '''
            while next_ele in nums:
                cur_sequence += 1
                next_ele += 1

            max_sequence = max(max_sequence , cur_sequence)
        
        return max_sequence

                