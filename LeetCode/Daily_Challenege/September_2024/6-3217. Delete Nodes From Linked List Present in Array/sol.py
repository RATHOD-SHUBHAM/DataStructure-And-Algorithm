# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        num_set = set(nums)

        dummy = prev_node = ListNode(-1)
        
        cur_node = head

        prev_node.next = cur_node

        while cur_node:
            next_node = cur_node.next

            if cur_node.val in num_set:
                prev_node.next = next_node
                cur_node.next = None
            else:
                prev_node = cur_node
            
            cur_node = next_node
        
        return dummy.next