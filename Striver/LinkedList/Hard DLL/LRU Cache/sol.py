# Do not edit the class below except for the insertKeyValuePair,
# getValueFromKey, and getMostRecentKey methods. Feel free
# to add new properties and methods to the class.
class LRUCache:
    def __init__(self, maxSize):
        self.maxSize = maxSize or 1
        self.hash = {}
        self.dll = DoubleLinkedList()
        self.len = 0
        

    def insertKeyValuePair(self, key, value):
        # Write your code here.
        if key not in self.hash:
            if self.len == self.maxSize:
                self.removeLRU()
            else:
                self.len += 1

            # Add to the DLL and Hash Map
            self.hash[key] = ListNode(key, value)
        else:
            # replace the value
            self.replaceKey(key, value)

        self.updateRecentlyUsed(self.hash[key])

    def removeLRU(self):
        # get the tail node value
        nodeToremove = self.dll.tail.key

        del self.hash[nodeToremove]

        self.dll.removeTail()

    def replaceKey(self, key, value):
        if key not in self.hash:
            return 
        self.hash[key].value = value

    def updateRecentlyUsed(self, node):
        self.dll.setHead(node)


    def getValueFromKey(self, key):
        # Write your code here.
        if key not in self.hash:
            return None

        # Make this node as most recently visited
        self.updateRecentlyUsed(self.hash[key])

        return self.hash[key].value

    def getMostRecentKey(self):
        # Write your code here.
        if not self.dll.head:
            return None

        mostRecentKey = self.dll.head.key

        return mostRecentKey
            


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, node):
        # 1. Check if node is already head node
        if self.head == node:
            return
        
        # 2. If there are 0 nodes in DLL
        elif self.head == None:
            self.head = node
            self.tail = node
        
        # 3. If there is 1 node in DLL
        elif self.head == self.tail:
            self.tail.prev = node
            self.head = node
            self.head.next = self.tail
        
        # 4. If there is multiple nodes in DLL
        else:
            if self.tail == node:
                self.removeTail()
            else:
                self.removeNodeBinding(node)

            self.head.prev = node
            node.next = self.head
            self.head = node

    def removeTail(self):
        # 1. If there is 0 nodes
        if not self.tail:
            return 

        # 2. If there is 1 node.
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return

        self.tail = self.tail.prev
        self.tail.next = None

    def removeNodeBinding(self, node):
        if node.prev is not None:
            node.prev.next = node.next

        if node.next is not None:
            node.next.prev = node.prev

        node.prev = None
        node.next = None

        return

class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None