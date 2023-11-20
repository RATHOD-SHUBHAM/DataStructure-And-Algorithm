# Dictionary

# Tc: O(N) | Sc:O(N)

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

        dic = {}

        curNode = head

        # Clone node and add to dictionary
        while curNode:
            newNode = Node(curNode.val)

            dic[curNode] = newNode

            curNode = curNode.next
        
        # Assigning pointers
        curNode = head

        while curNode:
            # clone of current node
            newNode = dic[curNode]

            # Get the cloned node
            nextNode = curNode.next
            nextNewNode = dic[nextNode] if nextNode in dic else None

            randomNode = curNode.random
            randomNewNode = dic[randomNode] if randomNode in dic else None

            # assign pointers
            newNode.next = nextNewNode
            newNode.random = randomNewNode

            # move the pointer
            curNode = curNode.next
        
        return dic[head]