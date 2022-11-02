'''
Singly linked list is the simplest one, it provides addAtHead in a constant time, and addAtTail in a "linear time". 
Though doubly linked list is the most used one, because it provides both addAtHead and addAtTail in a "constant time".
'''
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.len = 0 # get the length of linkedlist
        self.head = Node(0) #dummy node
        

    def get(self, index: int) -> int:
        if index >= self.len or index < 0:
            return -1
        
        curNode = self.head
        
        for _ in range(index + 1):
            curNode = curNode.next
            
        return curNode.val
        

    def addAtHead(self, val: int) -> None:
        return self.addAtIndex(0, val)
        

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.len , val)
        

    def addAtIndex(self, index: int, val: int) -> None:
        # if len of LL is 0 and its asking to insert at pos 3 -  return 
        # but ask interviewer if you can insert at last 
        if index > self.len:
            # index = self.len
            return
        
        # if the node is less than 0, add it at 0
        if index < 0:
            index = 0
            
        # since we are adding a node - lets increase the size
        self.len += 1
        
        # find the previous node
        prevNode = self.head
        for _ in range(index):
            prevNode = prevNode.next
        
        # create a node of current value
        newNode = Node(val)
        newNode.next = prevNode.next
        prevNode.next = newNode

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.len:
            return -1
        
        # decrese the len of linkedlist
        self.len -= 1
        
        # identify the pred node
        predNode = self.head
        for _ in range(index):
            predNode = predNode.next
            
        delNode = predNode.next
        predNode.next = delNode.next
        delNode.next = None


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)