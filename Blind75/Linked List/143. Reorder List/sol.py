'''
    This problem is a combination of these three easy problems:

        1. Middle of the Linked List.

        2. Reverse Linked List.

        3. Merge Two Sorted Lists.
'''
# Tc: O(n) | Sc: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        dummy = ListNode()
        dummy.next = head

        LL = head

        # 1. Get the center of LinkedList
        centerNode = self.tortiseHare(LL)

        # 2. Rotate Second half of LinkedList
        reversedLL = self.reversed(centerNode.next)

        centerNode.next = None
        
        # 3. Merge LinkedList
        mergedLL = self.mergeLL(LL, reversedLL)

        return dummy.next
        
    # Middle of LinkedList
    def tortiseHare(self, LL):
        slow = LL
        fast = LL.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow

    # Reverse a LinkedList
    def reversed(self, LL):
        prev = None
        curNode = LL

        while curNode:
            nxtNode = curNode.next

            curNode.next = prev

            prev = curNode
            curNode = nxtNode
        
        return prev

    # Merge 2  List
    def mergeLL(self, LL, reversedLL):
        l1 = LL
        l2 = reversedLL

        while l1 and l2:
            nxt_l1 = l1.next
            nxt_l2 = l2.next

            l1.next = l2
            l2.next = nxt_l1

            l1 = nxt_l1
            l2 = nxt_l2
        
        return LL