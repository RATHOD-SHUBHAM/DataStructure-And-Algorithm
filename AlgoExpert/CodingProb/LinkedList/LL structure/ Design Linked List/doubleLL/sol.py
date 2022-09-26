class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.size = 0
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, index: int) -> int:
        
        if index < 0 or index >= self.size:
            return -1
        
        # identify from which side to traverse
        # which side distance will be small
        dist_from_back = self.size - index
        
        if index  < dist_from_back:
            # traverse from front
            curNode = self.head
            for _ in range(index + 1):
                curNode = curNode.next    
        else:
            # traverse from back
            curNode = self.tail
            for _ in range(dist_from_back):
                curNode = curNode.prev
                
        return curNode.val
            

    def addAtHead(self, val: int) -> None:
        # pred is sentinal node
        pred = self.head
        suc = pred.next
        
        headNode = Node(val)
        headNode.next = suc
        headNode.prev = pred
        pred.next = headNode
        suc.prev = headNode
        
        # increse the size of LL
        self.size += 1
        

    def addAtTail(self, val: int) -> None:
        # add node before sentinal node
        suc = self.tail
        pred = suc.prev
        
        tailNode = Node(val)
        tailNode.next = suc
        tailNode.prev = pred
        pred.next = tailNode
        suc.prev = tailNode
        
        self.size += 1
        
        
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return -1
        
        if index < 0:
            index = 0
            
        # find succ and pred
        if index < self.size - index:
            pred = self.head
            
            for _ in range(index):
                pred = pred.next
                
            suc = pred.next
        else:
            suc = self.tail
            for _ in range(self.size - index):
                suc = suc.prev
                
            pred = suc.prev
            
        newNode = Node(val)
        newNode.next = suc
        newNode.prev = pred
        pred.next = newNode
        suc.prev = newNode
        
        self.size += 1
                
            
            
    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return -1
        
        if index < self.size - index:
            pred = self.head
            for _ in range(index):
                pred = pred.next
            succ = pred.next.next
        else:
            succ = self.tail
            for _ in range(self.size - index - 1):
                succ = succ.prev
            pred = succ.prev.prev
            
        self.size -= 1
        pred.next = succ
        succ.prev = pred
        

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)