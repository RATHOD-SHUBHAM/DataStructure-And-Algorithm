# Tc: O(1)
# Sc: O(capacity)

class LRUCache:

    def __init__(self, capacity: int):
        self.max_size = capacity
        self.len = 0
        
        self.hash = {}
        self.dll = DoubleLinkedList()
    
    def insertKeyValue(self, key, value):
        if key not in self.hash:
            if self.max_size == self.len:
                self.removeLeastRecentlyUsed()
            else:
                self.len += 1
            
            self.hash[key] = DoubleLinkedListNode(key, value)
        else:
            self.put(key, value)
        
        self.updateRecentlyUsed(self.hash[key])

    def get(self, key: int) -> int:
        if key not in self.hash:
            return -1
        
        self.updateRecentlyUsed(self.hash[key])

        return self.hash[key].value
        

    def put(self, key: int, value: int) -> None:
        if key not in self.hash:
            self.insertKeyValue(key, value)
        else:
            self.hash[key].value = value
            self.updateRecentlyUsed(self.hash[key])

    
    def removeLeastRecentlyUsed(self):
        nodeToremove = self.dll.tail.key
        self.dll.removeTail()
        del self.hash[nodeToremove]

    
    def updateRecentlyUsed(self, node):
        self.dll.setHead(node)

    
    def getRecentlyUsed(self):
        if self.dll.head is None:
            return -1

        return self.dll.head.key
        



class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def setHead(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        
        elif self.head == self.tail:
            node.next = self.tail
            self.tail.prev = node
            self.head = node
        
        elif self.head == node:
            return
        
        else:
            if self.tail == node:
                self.removeTail()
            
            self.removeBindings(node)

            node.next = self.head
            self.head.prev = node
            self.head = node
    

    def removeTail(self):
        if self.tail is None:
            return
        
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        
        else:
            self.tail = self.tail.prev
            self.tail.next = None
    
    def removeBindings(self, node):
        if node.prev:
            node.prev.next = node.next
        
        if node.next:
            node.next.prev = node.prev
        
        node.next = None
        node.prev = None



class DoubleLinkedListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)