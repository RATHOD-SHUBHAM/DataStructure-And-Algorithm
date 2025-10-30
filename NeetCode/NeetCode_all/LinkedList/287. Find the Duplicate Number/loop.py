'''
Consider the problem to be similar to Linked List
    - Index can be considered as node of linked list
    - Values can be considered as pointer to next node
'''

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        
        fast = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow