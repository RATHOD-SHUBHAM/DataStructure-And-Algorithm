class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
        
        
class MyLinkedList:

    def __init__(self):
        self.len = 0
        self.head = Node(-1) # sentinel node
        self.tail = Node(-1)
        
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, index: int) -> int:
        if index < 0 or index >= self.len:
            return -1
        
        dist_from_back = self.len - index # check if traversing from back is more optimal
        
        if index + 1 < dist_from_back:
            node = self.head
            
            for _ in range(index + 1):
                node = node.next
        
        else:
            node = self.tail
            
            for _ in range(dist_from_back):
                node = node.prev
                
        return node.val
        

    def addAtHead(self, val: int) -> None:
        return self.addAtIndex(0, val)
        

    def addAtTail(self, val: int) -> None:
        return self.addAtIndex(self.len, val)
        

    # insert before
    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.len:
            return -1
        
        if index < 0:
            index = 0
            
        dist_from_back = self.len - index
        
        if index + 1 < dist_from_back:
            
            parent = self.head
            
            for _ in range(index):
                parent = parent.next
                
            child = parent.next
            
        else:
            child = self.tail
            
            for _ in range(dist_from_back):
                child = child.prev
                
            parent = child.prev
            
        newNode = Node(val)
        newNode.prev = parent
        newNode.next = child
        parent.next = newNode
        child.prev = newNode
        
        self.len += 1        

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.len:
            return -1
        
        dist_from_back = self.len - index
        
        if index + 1 < dist_from_back:
            node = self.head
            
            for _ in range(index+1):
                node = node.next
                
        else:
            node = self.tail
            
            for _ in range(dist_from_back):
                node = node.prev
                
        parent = node.prev
        child = node.next
        
        parent.next = child
        child.prev = parent
        
        node.next = None
        node.prev = None
        
        self.len -= 1
            

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)