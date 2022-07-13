# TC: O(n^3)
'''
The outer loop runs exactly n times, 
and because currentNum increments by 1 during each iteration of the while loop, it runs in O(n) time. 
Then, on each iteration of the while loop, an O(n) lookup in the array is performed. 
Therefore, this brute force algorithm is really three nested O(n) loops, 
which compound multiplicatively to a cubic runtime.
'''
# sc: O(1)

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_seq = 0
        
        for num in nums:
            cur_num = num
            cur_streak = 1
            
            while cur_num + 1 in nums:
                cur_num += 1
                cur_streak += 1
                
            longest_seq = max(longest_seq , cur_streak)
            
        return longest_seq