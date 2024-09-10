# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def len_of_ll(self, head):
        cur_node = head
        ll_len = 0

        while cur_node:
            ll_len += 1
            cur_node = cur_node.next
        
        return ll_len

    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        # get the len of LL
        ll_len = self.len_of_ll(head)

        split_size = ll_len // k
        # Remaining nodes after splitting the k parts evenly.
        # These will be distributed to the first (size % k) nodes
        distribute_split = ll_len % k

        op = [None] * k

        if ll_len < 1:
            return op

        cur_node = head
        prev_node = None

        for x in range(k):
            reference_node = cur_node # maintain a reference to starting node

            cur_size = split_size
            if distribute_split > 0:
                cur_size += 1
                distribute_split -= 1
            
            # traverse to the end of cur size
            i = 0
            while i < cur_size:
                prev_node = cur_node
                cur_node = cur_node.next

                i += 1
            
            # break the LL
            prev_node.next = None


            op[x] = reference_node
        
        return op