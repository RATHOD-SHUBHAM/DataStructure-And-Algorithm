# Do not edit the class below except for the insertKeyValuePair,
# getValueFromKey, and getMostRecentKey methods. Feel free
# to add new properties and methods to the class.
class LRUCache:
    def __init__(self, maxSize):
        self.maxSize = maxSize or 1
        self.hash = {}
        self.len = 0
        self.dll = DoubleLinkedList()

    def insertKeyValuePair(self, key, value):
        # Write your code here.
        if key not in self.hash:
            if self.maxSize == self.len:
                self.removeRecentlyUsed()
            else:
                self.len += 1

            self.hash[key] = DoubleLinkedListNode(key, value)
        else:
            self.replaceValue(key, value)
            
        self.updeteRecentlyUsed(self.hash[key])

    def removeRecentlyUsed(self):
        nodeToremove = self.dll.tail.key
        self.dll.removeTail()
        del self.hash[nodeToremove]

    def replaceValue(self, key, value):
        if key not in self.hash:
            return -1

        # update the value of DLL node
        self.hash[key].value = value

    def updeteRecentlyUsed(self, node):
        self.dll.setHead(node)

    def getValueFromKey(self, key):
        # Write your code here.
        if key not in self.hash:
            return None

        self.updeteRecentlyUsed(self.hash[key])

        return self.hash[key].value

        

    def getMostRecentKey(self):
        # Write your code here.
        if not self.dll.head:
            return None
        return self.dll.head.key

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def setHead(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        elif self.head == node:
            return
        elif self.head == self.tail:
            node.next = self.tail
            self.tail.prev = node
            self.head = node
        else:
            # if node is tail or somewhere in btn - remove the node and make it head
            if self.tail == node:
                self.removeTail()
            self.removeBinding(node)
            node.next = self.head
            self.head.prev = node
            self.head = node
    
    def removeTail(self):
        if self.tail == None:
            return
        elif self.head == self.tail:
            self.head = None
            self.tail = None
            return
        else:
            self.tail = self.tail.prev
            self.tail.next = None

    def removeBinding(self, node):
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        node.prev = None
        node.next = None


class DoubleLinkedListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
