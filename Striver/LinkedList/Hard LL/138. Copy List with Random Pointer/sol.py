# Tc: O(N) | Sc:O (1)

"""
Step 
1: Create a copy of node and add it beside the original node
2: Map the random pointers of the copied node.
3: Bring back the original pointers

"""

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        
        # Step 1: Clone the current node
        curNode = head

        while curNode:
            newNode = Node(curNode.val)

            # change pointers - add the cloned node in btn curnode and next node
            nxtNode = curNode.next

            curNode.next = newNode
            newNode.next = nxtNode

            # move current node
            curNode = nxtNode
        
        # Step 2: Assign random nodes
        curNode = head

        while curNode:

            # assign pointers
            randomNode = curNode.random
            newNode = curNode.next

            newNode.random = randomNode.next if randomNode else None

            # move pointer
            curNode = curNode.next.next

        # Step 3: Assign next node
        curNode = head
        
        # pointer to head of cloned node
        dummy = Node(-1)
        dummy.next = curNode.next

        while curNode:
            newNode = curNode.next
            nxtNode = curNode.next.next if curNode.next.next else None

            # assigning pointers
            newNode.next = nxtNode.next if nxtNode else None
            curNode.next = nxtNode

            # move pointer
            curNode = curNode.next
        
        return dummy.next