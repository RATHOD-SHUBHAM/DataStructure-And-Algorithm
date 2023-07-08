#User function Template for python3

'''class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
'''
class Solution:
    def deleteNode(self,head, x):
        
        ptr = head
        
        if x == 1:
            head = head.next
            head.prev = None
            del(ptr)

        else:
            # 1 based index
            
            pos = 1
            while pos != x:
                ptr = ptr.next
                pos += 1
            
            # now ptr is at a position that needs to be deleted
            if ptr.next:
                ptr.next.prev = ptr.prev
            if ptr.prev:
                ptr.prev.next = ptr.next
            
            ptr.prev = None
            ptr.next = None
            del(ptr)
            
        return head