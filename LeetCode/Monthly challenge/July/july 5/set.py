# Tc = O(n)
'''
Although the time complexity appears to be quadratic due to the while loop nested within the for loop, 
closer inspection reveals it to be linear. 
Because the while loop is reached only when currentNum marks the beginning of a sequence (i.e. currentNum-1 is not present in nums), 
the while loop can only run for nn iterations throughout the entire runtime of the algorithm. 
This means that despite looking like O(n⋅n) complexity,
 the nested loops actually run in O(n + n) = O(n) time. 
 All other computations occur in constant time, so the overall runtime is linear.
'''

# sc = O(n)

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        longest_seq = 1
        num_set = set(nums)
        # print(num_set)
        
        for num in num_set:
            
            if num - 1 not in num_set: # check the start of sequence
                # this is the start
                cur_num = num
                cur_streak = 1
                
                while cur_num + 1 in num_set:
                    cur_num += 1
                    cur_streak += 1
                    
                longest_seq = max(longest_seq , cur_streak)
                
        return longest_seq
                