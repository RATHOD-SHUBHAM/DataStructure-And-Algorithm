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
        
        dic = {} # keep a deep copy
        
        curNode = head
        
        # step 1: Mapping
        while curNode:
            newNode_val = curNode.val
            dic[curNode] = Node(newNode_val)
            
            curNode = curNode.next
        
        # assigning pointers
        curNode = head
        
        while curNode:
            nextNode = curNode.next
            randomNode = curNode.random
            
            newNode = dic[curNode]
            
            newNode.next = dic[nextNode] if nextNode else None
            newNode.random = dic[randomNode]  if randomNode else None
            
            curNode = curNode.next
        
        return dic[head]