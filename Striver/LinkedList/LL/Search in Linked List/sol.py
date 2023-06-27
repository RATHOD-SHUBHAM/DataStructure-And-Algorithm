#  Node of a linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def searchKey(self, n, head, key):
        #Code here
        ptr = head
        node_cnt = 0
        
        while ptr and node_cnt < n:
            if ptr.data == key:
                return 1
            
            ptr = ptr.next
        
        return 0