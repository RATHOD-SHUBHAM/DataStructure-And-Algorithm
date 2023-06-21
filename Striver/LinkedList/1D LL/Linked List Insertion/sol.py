class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Solution:
    #Function to insert a node at the beginning of the linked list.
    def insertAtBegining(self,head,x):
        new_node = Node(x)
        if head == None:
            head = new_node
            return head
        
        new_node.next = head
        head = new_node
        
        return head
    
    #Function to insert a node at the end of the linked list.
    def insertAtEnd(self,head,x):
        new_node = Node(x)
        
        if head == None:
            head = new_node
            return head
        
        ptr = head
        while (ptr.next != None):
            ptr = ptr.next
        
        ptr.next = new_node
        
        return head