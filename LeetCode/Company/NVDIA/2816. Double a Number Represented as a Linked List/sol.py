# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # Step 1: Grab the number
        num = 0

        curNode = head
        while curNode:
            val = curNode.val

            num = num * 10 + val

            curNode = curNode.next
        
        
        # Step 2: Double the number
        new_num = num * 2
        
        # Step 3: Convert the number to lst
        sys.set_int_max_str_digits(100000) # this is set just to make this run on leetcode, as leetcode itself will ask to set this
        
        str_num = str(new_num)
        lst_str = [int(i) for i in str_num]


        # Step 4: Add to linked list
        dummy = ListNode(-1)
        curNode = dummy
        
        i = 0
        while i < len(lst_str):
            val = lst_str[i]

            curNode.next = ListNode(val)

            i += 1
            curNode = curNode.next
        
        return dummy.next