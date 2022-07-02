# move p1 to k position.
# now move p1 to end, and make p2 follow, Beacuse p1 will be k value ahead of p2
# when p1 reaches the end, p2 will be at n-k node
from re import L


class ListNode:
    def __init__ (self, val = 0 , next = None):
        self.val = val
        self.next = next

class Solution:
    def swapnodes(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        prev_p1, prev_p1 = dummy

        p1 = p2 = head


        # move to k node
        for _ in range(1, k):
            prev_p1 = p1
            p1 = p1.next

        curNode = p1
        

        # move to n-k ndoe
        while curNode:
            curNode = curNode.next
            prev_p2 = p2
            p2 = p2.next


        # swap the pointers
        prev_p1.next, prev_p2.next = p2, p1
        p1.next , p2.next = p2.next , p1.next

        return dummy.next

def main():
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    k = 2
    print(Solution().swapnodes(head, k))

