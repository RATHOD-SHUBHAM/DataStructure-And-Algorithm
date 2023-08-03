class ListNode:
    def __init__(self, key, value):
        self.freq = 1 # the frequency of the list
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = ListNode(-1,-1)
        self.tail = ListNode(-10, -10)
        
        self.head.next = self.tail
        self.tail.prev = self.head
        
        self.size = 0 # size of linkedlist
    
    def setHead(self, node):
        # increase size of LL - As a node is getting added
        self.size += 1
        
        # add node bindings
        node.next = self.head.next
        node.prev = self.head 
        self.head.next.prev = node
        self.head.next = node
    
    def removeTail(self):
        # get the node previous to the tail node -
        tail = self.tail.prev
        self.removeNode(tail)
        return tail
    
    def removeNode(self, node):
        if node.prev:
            node.prev.next = node.next
        
        if node.next:
            node.next.prev = node.prev
            
        node.next = None
        node.prev = None
        
        # decrease size of LL : As node got removed
        self.size -= 1
        

class LFUCache:

    def __init__(self, capacity: int):
        self.hash = {} # keep track of nodes
        self.frequence = collections.defaultdict(DoubleLinkedList) # keep track of frequence
        
        self.minFreq = 0
        self.len_dll = 0
        
        self.capacity = capacity     

    def get(self, key: int) -> int:
        if key not in self.hash:
            return -1
        
        # since we are tampering the node - frequency must increase
        self.updateLFU(self.hash[key])
        
        return self.hash[key].value
        

    def put(self, key: int, value: int) -> None:
        if key in self.hash:
            '''
                1. update the cache.
                2. Update the DLL.
            '''
            self.updateCache(key, value)
            self.updateLFU(self.hash[key])
        else:
            if self.len_dll == self.capacity:
                self.removeLFU()
            else:
                self.len_dll += 1
                
            
            # add a new node - since this is the first addition , freq = 1 and minFreq = 1
            newNode = ListNode(key , value)
            '''
                1. Add to hash.
                2. Add to LinkedList with freq 1
            
            '''
            self.hash[key] = newNode
            
            self.frequence[1].setHead(newNode)
            
            self.minFreq = 1
            
    def updateCache(self, key, value):
        self.hash[key].value = value
    
    def removeLFU(self):
        # get the tail node from LinkedList : remove it from hash
        nodeToremove = self.frequence[self.minFreq].removeTail().key
        del self.hash[nodeToremove]
    
    def updateLFU(self, node):
        prevFreq = node.freq # each node will keep track of its freq
        
        # new freq of node
        node.freq += 1
        
        # update the DLL
        '''
            1. Remove from the old DLL : Prev Freq
            2. Add it to new DLL : new Freq
        '''
        
        self.frequence[prevFreq].removeNode(node)
        self.frequence[node.freq].setHead(node)
        
        # now check the size of Linkedlist and see if minFreq hsa changed
        if prevFreq == self.minFreq and self.frequence[self.minFreq].size == 0:
            self.minFreq += 1
    
        

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)