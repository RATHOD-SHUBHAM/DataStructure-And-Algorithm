# both solution are same --  this is written a bit clean


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class doubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, node):
        # if node is already head
        if node == self.head:
            return
        # if first node
        elif self.head == None:
            self.head = node
            self.tail = node
        # if there is already one node
        elif self.head == self.tail:
            self.tail.prev = node
            self.head = node
            self.head.next = self.tail
        else:
            # check if node is tail
            if node == self.tail:
                self.removeTail()
            # remove node binding
            self.removeNodeBinding(node)

            # change pointers
            self.head.prev = node
            node.next = self.head
            self.head = node

    def removeTail(self):
        if self.tail == None:
            return
        elif self.tail == self.head:
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

        node.next = None
        node.prev = None

        
class LRUCache:
    def __init__(self, maxSize):
        self.maxSize = maxSize or 1
        self.len = 0
        self.hashMap = {}
        self.dll = doubleLinkedList()

    def insertKeyValuePair(self, key, value):
        # if key is not present in hashmap
        if key not in self.hashMap:

            # if maxsize full
            if self.maxSize == self.len:
                self.removeLRU()
            else:
                self.len += 1

            # create a new entry
            self.hashMap[key] = Node(key, value)

        # if key is present
        else:
            self.replaceKeyValue(key,value)

        # since i visited that node -- update it to recently accessed
        self.updateRecentlyAccessed(self.hashMap[key])

    def removeLRU(self):
        # get the key from tail
        nodeTopop = self.dll.tail.key
        # remove from dictionary
        del self.hashMap[nodeTopop]
        # remove taik
        self.dll.removeTail()

    def replaceKeyValue(self, key, value):
        if key not in self.hashMap:
            return
        self.hashMap[key].value = value

    def updateRecentlyAccessed(self, node):
        self.dll.setHead(node)

    def getValueFromKey(self, key):
        if key not in self.hashMap:
            return
        # since i am visiting this -- update this as recently accessed
        self.updateRecentlyAccessed(self.hashMap[key])

        # return the key
        return self.hashMap[key].value
 

    def getMostRecentKey(self):
        if self.dll.head is None:
            return
        return self.dll.head.key