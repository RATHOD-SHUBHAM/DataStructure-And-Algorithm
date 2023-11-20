# Dictionary ----------------------------------------------------------------------

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
    

# Copy Next Node ----------------------------------------------------------------------

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
        
        # Step 1:
        curNode = head
        
        while curNode:
            newNode = Node(curNode.val)
            
            newNode.next = curNode.next
            curNode.next = newNode
            
            curNode = newNode.next
            
        # Step 2:
        curNode = head
        
        while curNode:
            newNode = curNode.next

            newNode.random = curNode.random.next if curNode.random else None
            
            curNode = newNode.next
        
        # Step 3:
        dummy = Node(-1)

        curNode = head
        newNode = curNode.next
        
        dummy.next = newNode
        
        
        while curNode:
            curNode.next = newNode.next if newNode.next else None
            newNode.next = newNode.next.next if newNode.next else None
            
            curNode = curNode.next
            newNode = newNode.next
        
        return dummy.next