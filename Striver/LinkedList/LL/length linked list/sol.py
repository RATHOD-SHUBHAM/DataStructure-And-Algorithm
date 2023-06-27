

#Linked list class
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

 
        
class Solution:
    
    #Function to count nodes of a linked list.
    def getCount(self, head_node):
        ptr = head_node
        count = 0
        
        while ptr:
            count += 1
            ptr = ptr.next
            
        return count