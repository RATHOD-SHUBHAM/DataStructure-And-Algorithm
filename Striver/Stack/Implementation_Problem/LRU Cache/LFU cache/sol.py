class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = None
        self.next = None
        
class DLL:
        
    def __init__(self):
        self.head = ListNode(0, 0)
        self.tail = ListNode(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
            

    def setHead(self, node):
        self.size += 1
        
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

        
    def removeTail(self):
        tail = self.tail.prev
        self.removeNode(tail)
        return tail
        
    def removeNode(self, node):
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev
        
        self.size -= 1
        node.next = None
        node.prev = None

        
    

class LFUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.freqTable = collections.defaultdict(DLL)
        self.capacity = capacity
        self.minFreq = 0
        self.len = 0
        
    
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        self.updateCache(self.cache[key])
        return self.cache[key].val

        

    def put(self, key: int, value: int) -> None:
        if not self.capacity:
            return
        
        if key in self.cache:
            self.replaceValue(key, value)
            self.updateCache(self.cache[key])
        else:
            if self.len == self.capacity:
                self.removeLFU()
            else:
                self.len += 1
                
            node = ListNode(key, value)
            self.cache[key] = node
            self.freqTable[1].setHead(node)
            self.minFreq = 1 # since this is a new node the minimum freq will be one
        
    def removeLFU(self):
        nodeToremove = self.freqTable[self.minFreq].removeTail().key
        del self.cache[nodeToremove]
        
    
    def replaceValue(self, key, value):
        node = self.cache[key]
        node.val = value
        
        
    def updateCache(self, node):
        # increase the freq
        prevFreq = node.freq # get the previous freq
        node.freq += 1 # increse it by one
        
        # update freq table
        self.freqTable[prevFreq].removeNode(node) # from the prev freq remove the node
        self.freqTable[node.freq].setHead(node) # add new freq or update
        
        # remove the prev freq if there is nothing in it
        if prevFreq == self.minFreq and self.freqTable[prevFreq].size == 0:
            self.minFreq += 1
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)